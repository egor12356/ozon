import requests
import pandas as pd

def go_to_csv(response):
    """Сохраняем в csv файл"""
    arr_address = []
    arr_number_flats = []

    for home in response:
        flats = home['flats']
        address = home['sourceAddressString']
        arr_address.append(address)
        arr_number_flats.append(flats)

    df = pd.DataFrame({'address': arr_address, 'number_floats': arr_number_flats})
    print(f'Всего квартир в заданой зоне: {df.number_floats.sum()}')

    df.to_csv('result.csv', index=False, sep=';', encoding='cp1251')


def main():
    url = 'https://geo.pochta.ru/api/address-search/in-polygon'
    # data = [{"lat":51.7705009339276,"lng":55.10016918182374},{"lat":51.76906685640219,"lng":55.113515853881836},{"lat":51.7668758166456,"lng":55.102229118347175}]
    # data = [{"lat":50.72595004523511,"lng":37.54817962646485},{"lat":55.71318733251447,"lng":37.558822631835945},{"lat":55.72440327187514,"lng":37.585773468017585},{"lat":55.7349394523402,"lng":37.56843566894532}]

    # Можно сделать ввод данных через клавиатуру
    data = [{'lat': 55.749440, 'lng': 37.582188},
            {'lat': 55.758640, 'lng': 37.658958},
            # {'lat': 55.758640, 'lng': 37.658958},
            {'lat': 55.734162, 'lng': 37.634290},
            ]

    # Запрос к API (вроде ограничений на размер области как на сайте нет)
    response = requests.post(url, json=data).json()

    # Сохраняем в файл
    go_to_csv(response)

if __name__ == '__main__':
    main()
