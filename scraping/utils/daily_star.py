import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import datetime

from django.db import IntegrityError, DatabaseError

from scraping.models import News

top_news_url = "https://www.thedailystar.net/top-news/rss.xml"
front_page_url = "https://www.thedailystar.net/frontpage/rss.xml"


def single_news(url):
    """
    :param url: link of a news
    :return: news obj as dict
    """
    src = rq.get(url)

    soup = bs(src.text, 'lxml')
    detailed_content = soup.find('div', class_='detailed-content')
    author = detailed_content.find('div', class_='author-name')
    body = detailed_content.find('article', class_='article')
    news = {
        'author': author.text if author is not None else "",
        'body': body.text if body is not None else ""
    }

    return news


def items_to_object_list(items):
    """
    :param items: list of bs4 tag
    :return: python dict representation of items
    """

    ob_items = []
    for item in items:
        it = {
            'title': item.title.text,
            'link': item.link.text,
            'description': item.description.text,
            'pubDate': item.pubDate.text
        }
        mc = item.find('media:content')
        if mc is not None:
            attr = dict()
            attr['url'] = mc['url']
            attr['fileSize'] = mc['fileSize']
            attr['type'] = mc['type']
            attr['medium'] = mc['medium']
            attr['width'] = mc['width']
            attr['height'] = mc['height']
            it['mediaContent'] = attr

        mt = item.find('media:thumbnail')
        if mt is not None:
            attr = dict()
            attr['url'] = mt['url']
            attr['width'] = mt['width']
            attr['height'] = mt['height']
            it['mediaThumbnail'] = attr

        ob_items.append(it)
    return ob_items


def top_news():
    """
    :return: top news as list of item dictionary
    """
    rssc = rq.get(top_news_url)
    soup = bs(rssc.text, features='xml')
    items = soup.find_all('item')
    return items_to_object_list(items)


def front_page():
    """
    :return: front page news as list of item dictionary
    """
    rssc = rq.get(front_page_url)
    soup = bs(rssc.text, features='xml')
    items = soup.find_all('item')
    return items_to_object_list(items)


def scrape():
    newses = top_news() + front_page()
    for index, news in enumerate(newses):
        title = news['title']
        pubdate = datetime.strptime(news['pubDate'], "%a, %d %b %Y %H:%M:%S %z")
        description = news['description']
        language = 'en'
        url = news['link']
        image_url = news['mediaContent']['url']

        single_n = single_news(url)
        author = single_n['author'].rstrip().lstrip()
        body = single_n['body'].rstrip().lstrip()

        n = News(
            title=title,
            pubdate=pubdate,
            description=description,
            author=author,
            language=language,
            url=url,
            image_url=image_url,
            body=body
        )

        if n.is_positive:
            try:
                n.save()
                print(f'No. {index + 1} saved.')
            except (IntegrityError, DatabaseError) as e:
                print(e.args)
                print(f'No. {index + 1} failed to save.')
        else:
            print(f'No. {index+1} rejected.')
    return True
