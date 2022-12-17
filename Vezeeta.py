from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

doctor_name = []
doctor_surname = []
doctor_specilaity = []
doctor_address = []
doctor_price = []
doctor_waiting = []
close_scrape = range(100, 1264, 100)
out = True
for page in tqdm(range(1, 1264), desc='Loading'):
    url = f'https://www.vezeeta.com/ar/%D8%AF%D9%83%D8%AA%D9%88%D8%B1/%D9%83%D9%84-%D8%A7%D9%84%D8%AA%D8%AE%D8%B5%D8%B5%D8%A7%D8%AA/%D9%85%D8%B5%D8%B1?page={page}'
    #  webpage url
    webpage = requests.get(url)
    # webcontent of webpage
    webcontent = webpage.content
    # data from the content
    data = BeautifulSoup(webcontent, "html.parser")

    doctor_cards = data.find_all('div', {'width': 'calc(100% - 558px)'})
    for doctor in range(len(doctor_cards)):
        doctor_name.append(doctor_cards[doctor].find('span', {'itemprop': 'name'}).text)
        doctor_surname.append(doctor_cards[doctor].find('h3', {
            'class': 'DoctorCardSubComponentsstyle__Text-sc-1vq3h7c-14 DoctorCardSubComponentsstyle__DescText-sc-1vq3h7c-17 dZnRSf esZVig'}).text)
        doctor_specilaity.append(doctor_cards[doctor].find('span', {
            'class': 'DoctorCardSubComponentsstyle__LimitDetails-sc-1vq3h7c-19 DoctorCardSubComponentsstyle__SpecialtyRowLimitDetails-sc-1vq3h7c-22 fSNnRI kABNHc'}).text)
        doctor_cards[doctor].find('span', {'itemprop': 'address'})
        if doctor_cards[doctor].find('span', {'itemprop': 'address'}) is not None:
            doctor_address.append(doctor_cards[doctor].find('span', {'itemprop': 'address'}).text)
        else:
            doctor_waiting.append('لا يوجد عنوان')
        doctor_price.append(doctor_cards[doctor].find('span', {'itemprop': 'priceRange'}).text)
        doctor_cards[doctor].find('span', {'class': 'DoctorCardstyle__Text-sc-uptab2-4 lhhnfH'})
        doctor_cards[doctor].find('span', {'color': '#6ACF80'})
        doctor_cards[doctor].find('span', {'color': '#0070CD'})
        if doctor_cards[doctor].find('span', {'color': '#0070CD'}) is not None:
            doctor_waiting.append(doctor_cards[doctor].find('span', {'color': '#0070CD'}).text)
        elif doctor_cards[doctor].find('span', {'color': '#6ACF80'}) is not None:
            doctor_waiting.append(doctor_cards[doctor].find('span', {'color': '#6ACF80'}).text)
        elif doctor_cards[doctor].find('span', {'class': 'DoctorCardstyle__Text-sc-uptab2-4 lhhnfH'}) is not None:
            doctor_waiting.append(
                doctor_cards[doctor].find('span', {'class': 'DoctorCardstyle__Text-sc-uptab2-4 lhhnfH'}).text)
        else:
            doctor_waiting.append('لم تدرج مدة الانتظار')

    if page in close_scrape:
        choose = input('\nDo you want to continue?   y or n\n').capitalize()
        if choose == 'N':
            break
        else:
            print('The Scraping is continue')

print('The Scraping had been stopped and Download percentage is ::')

for doctor_num in range(len(doctor_name)):
    print(
        f' دكتور {doctor_num + 1} ::: {doctor_name[doctor_num]} | {doctor_surname[doctor_num]} | {doctor_specilaity[doctor_num]} | {doctor_waiting[doctor_num]}  | سعر الحجز {doctor_price[doctor_num]}جنية ')
    print('\n')
