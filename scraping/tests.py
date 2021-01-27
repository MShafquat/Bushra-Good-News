from django.test import TestCase
from scraping.models import News
import datetime


class NewsTestCase(TestCase):
    def setUp(self):
        pass

    def test_negative_sentiment(self):
        """Negative news sentiment is correctly classified"""
        # Collected from The Daily Star
        title = "Rape at MC College: Probe body finds negligence of hostel superintendents, guards"
        pubdate = datetime.datetime.strptime("09:45 PM, January 27, 2021", "%I:%M %p, %B %d, %Y")
        author = "Star Online Report"
        language = "English"
        url = "https://www.thedailystar.net/crime/news/rape-mc-college-probe-body-finds-negligence-hostel-superintendents-guards-2034933"
        image_url = "https://assetsds.cdnedge.bluemix.net/sites/default/files/styles/big_2/public/feature/images/2021/01/17/mc_college_0.jpg?itok=LT-Bhrvs&c=d4e1597bf4c957765a6122e796ceeb57"
        body = """The probe committee has found negligence of two hostel-superintendents and five guards at Sylhet's 
                MC College in ensuring security resulting in the gang-rape of a woman in the hostel in September last year, 
                Supreme Court lawyer Md Mesbah Uddin told The Daily Star while disclosing details of the report today.

                The probe body also said in the enquiry report that the principal of the college, Prof Md Saleh Ahmed, 
                as the head of the institution, cannot avoid responsibility of the incident. 

                Some former and current students of MC College had occupied rooms of the hostel. Former student Saifur Rahman had 
                occupied the residence of a hostel super when the college was closed. As such they dared commit this heinous offence 
                on campus, the report added. 

                A HC bench led by Justice Md Mozibur Rahman Miah is scheduled to deal with the probe report on February 4.

                The four-member committee placed the 176-page report to the HC through its Registrar Md Golam Rabbani on 
                October 20 last year in line with its September 29 directive. 

                The members are Sylhet's District and Sesions Judge Md Bazlur Rahman, head of the committee, Additional 
                Metropolitan Sessions Judge of Sylhet Mominun Nesa, its Chief Metropolitan Magistrate Md Abul Kashem and 
                Additional Deputy Commissioner Sharmin Sultana. 

                The committee has made 15 recommendations in order to ensure security of the college campus so that such 
                incidents do not take place in future, lawyer Mesbah Uddin said. 

                The HC bench recently held a hearing in part on the rule involving the issue.

                Lawyer Md Mesbah Uddin placed The Daily Star reports under the headlines "Rape in MC College: 6 accused BCL 
                men moved with impunity" and "Unpublished crimes led to horror like this" before the HC bench for necessary 
                orders.
                """
        neg_news = News.objects.create(title=title, pubdate=pubdate, author=author, language=language, url=url,
                                       image_url=image_url, body=body)
        self.assertEqual(neg_news.is_positive(), False)

    def test_positive_news(self):
        """Positive news sentiment is correctly classified"""
        # Collected from The Daily Star
        title = "Covid vaccination kicks off today"
        pubdate = datetime.datetime.strptime("12:00 AM, January 27, 2021", "%I:%M %p, %B %d, %Y")
        description = "PM to inaugurate the piloting"
        author = "Staff Correspondent"
        language = "English"
        url = "https://www.thedailystar.net/frontpage/news/covid-vaccination-kicks-today-2034413"
        image_url = "https://assetsds.cdnedge.bluemix.net/sites/default/files/styles/big_2/public/feature/images/2021/01/07/covishield.jpg?itok=g3GB0jQ5&c=a8f0d50482055276ca2d0e43d68f1ff7"
        body = """
        Bangladesh joins the world today in the vaccination campaign against Covid-19 pandemic with a robust stock of vaccine doses in hand.
Of the south Asian countries, Bangladesh has the highest number of vaccines in hands -- 70 lakh doses -- after India.
Covid-19 has already claimed more than 8,000 lives in the country and over 2.14 million in the world.
Prime Minister Sheikh Hasina is expected to inaugurate the pilot vaccination virtually from Kurmitola General Hospital at 3:30pm.
She is also expected to launch the registration app called "Surokkha" for mass inoculation, scheduled to start on February 7.
The government has targeted vaccinating 60 lakh people in the first month and another 50 lakh the following month. The pilot will start with the vaccination of a nurse of Kurmitola hospital.
According to government officials, 20-30 people will get vaccinated on the opening day. The first recipients will include nurses, doctors, freedom fighters, media personnel and other frontline workers from different professional groups.
The pilot vaccination will take place in five public hospitals of Dhaka. The Directorate General of Health Services (DGHS) has already completed all the procedures to that end.
"From tomorrow [today] vaccination [pilot] will start in Dhaka and then it will be expanded across the country. By that time, all preparations for smooth vaccination will be completed," Prof Abul Bashar Mohammad Khurshid Alam, director general of DGHS, told The Daily Star yesterday.
He also said they have prepared a list of 20 to 30 people to
inoculate on the opening day.
"Each vial has 10 doses. So, once we open a vial, we have to administer all 10 doses. Accordingly, the number of recipients should be either 20 or 30," Khurshid Alam said.
He also said, except India, none of the South Asian countries has more vaccines than Bangladesh right now.
Meanwhile, the Directorate General of Drug Administration (DGDA) has given the usage permission of 50 lakh purchased vaccines, which arrived in Dhaka on
Monday, after examining the samples from each batch.
Major General Md Mahbubur Rahman, director general of the DGDA, told journalists that the piloting of the vaccine will start with the government purchased vaccines.
Bangladesh purchased 3 crore doses of Oxford-AstraZeneca vaccine from Serum Institute of India (SII). The first consignment of 50 lakh arrived on January 25. Bangladesh also received 20 lakh doses of the Oxford vaccine produced in SII as gift from the Indian government on January 21.
MANAGING SIDE EFFECTS
Healthcare officials said the Oxford-AstraZeneca vaccine is safe and has minimal side effects.
Prof Khurshid Alam, in a recent press conference, said, "The data we have on the Oxford vaccine suggest the side effects are minimal. If any vaccine recipient faces severe allergic shock, we have arrangements to treat them. For this, we have set up vaccination centres only in hospitals."
The DGHS has published advertisements on the media which said the vaccine is safe. But some vaccine recipients may face a few physical complexities, such as pain or swelling on the arm where the shot is given, mild fever, nausea, body pain and headaches.
These side effects may sustain one or two days, according to the DGHS.
Health officials also said side effects may arise if the purity of the vaccine is damaged due to improper storage. Faulty syringes and needles may cause side effects.
The vaccination guideline for healthcare workers said that in some cases side effects like eye and face swelling, mild breathing issues, low blood pressure, nausea or unconsciousness might occur after vaccination.
In such instances, healthcare workers have been advised about what medical intervention has to be taken.
According to the vaccination plan, all recipients have to stay at the vaccination centre for 15-30 minutes after the vaccination. There will be arrangement for this in the hospital.
A medical team will also be present to tackle such adverse event in every vaccination centre. All civil surgeons, deputy civil surgeons and other district level trainers have been trained in this regard recently in Dhaka.
During the next few days, the local vaccination team will also do follow ups and keep updates of the recipients.
Officials said training for other teams in upazila health complexes and hospitals in city corporation areas will also be completed within the next few days.
On Monday, some 124 doctors and nurses from five hospitals in Dhaka city, where the first-run of the vaccine will start the day after the PM's inauguration, received training.
During a visit to Dhaka Medical College Hospital, Mugda Medical College Hospital and the Bangabandhu Sheikh Mujib Medical University, officials said they have formed multiple medical teams and arranged hospitals beds to tackle any adverse situation.
                        """
        positive_news = News.objects.create(title=title, description=description, pubdate=pubdate, author=author,
                                            language=language, url=url,
                                            image_url=image_url, body=body)
        self.assertEqual(positive_news.is_positive(), True)

    def test_neutral_news(self):
        """Neutral news sentiment is correctly classified as Positive"""
        # Collected from The Daily Star
        title = "Primary schools may also reopen next month"
        pubdate = datetime.datetime.strptime("12:00 AM, January 27, 2021", "%I:%M %p, %B %d, %Y")
        description = "Says state minister"
        author = "Asifur Rahman"
        language = "English"
        url = "https://www.thedailystar.net/frontpage/news/primary-schools-may-also-reopen-next-month-2034421"
        image_url = "https://assetsds.cdnedge.bluemix.net/sites/default/files/styles/big_2/public/feature/images/2021/01/23/school-open-after-covid.jpg?itok=OTNbKjRo"
        body = """
                In line with the resumption of secondary-level schools and colleges, the government is also planning to reopen primary schools and kindergartens after 10 months of shutdown.
The Directorate of Primary Education (DPE) has already sent a guideline to all primary schools to prepare for reopening by February 4.
Zakir Hossain, state minister for primary and mass education, yesterday said, "We are planning to reopen primary schools on any day of February.
"Schools may reopen on the first or second week of February with the permission of the prime minister."
About the primary schools, he said, the authorities would operate classes from the first to fifth grades in multiple shifts.
"Students of fifth grade will get priority. The rest will visit schools in person once a week," he said.
Asked about the kindergarten schools, he said, those institutions too could reopen on any day.
"We have no probation for those who are not enlisted. If the enlisted ones want to reopen, they can talk to us," he added.
The state minister also said that they were thinking about increasing the fund for school-level improvement plan (SLIP) under the Primary Education Development Program to ensure hygiene in educational institutions.
All educational institutions have remained closed since March 17 because of the coronavirus pandemic, hampering academic activities of about two crore students of more than one lakh primary schools and kindergartens.
GUIDELINES
On Sunday, DPE sent the directives to all district primary education officers for taking the necessary preparation to reopen schools.
As per the directives, school authorities, upon getting approval of the authorities concerned, would prepare the timing of school opening and closure and distribute mid-day meals in a way that would avoid the gathering of students and guardians.
The DPE guideline wrote that safe water and sanitation facilities should be prepared and enough arrangement of water tape for hand washing should be ensured before reopening schools.
For measuring body temperature, non-contact thermometers must be collected.
The guideline read, "Only two students will be allowed to sit on each bench at classrooms after the reopening of primary schools. Every student, teacher, and other staffers have to wear masks.
"The compound of schools must be cleaned and the dustbin should be disinfected every day. Floors of the offices and classrooms, benches, the handle of doors and grips of stairs should be disinfected before and after every shift of classes."
The guideline also directed the schools not to conduct assembly and take adequate measures to ensure physical distancing.
"The phone number of one or two teachers along with Headmaster will be displayed in an open space for the advantage of communication," it added.
The guideline also instructed school authorities to spent money from the SLIP programme to buy necessary items for maintaining hygiene. 
                                """
        neutral_news = News.objects.create(title=title, description=description, pubdate=pubdate, author=author,
                                           language=language, url=url,
                                           image_url=image_url, body=body)
        self.assertEqual(neutral_news.is_positive(), True)
