import xml
import json

def main():
    while True:
        use = input('Введите:\n j для работы с json,\n '
                    'x - для работы с xml,\n '
                    'q - для выхода из программы\n')
        if use == 'j':
            json_def()
        if use == 'x':
            xml_def()
        if use == 'q':
            break

def top_list(description):
    for i in range(len(description)):
        if len(description[i]) > 6:
            description[i] = description[i].lower()
        else:
            description[i] = ''
    description_dict = {}
    for words in description:
        description_dict[words] = description.count(words)
    del description_dict['']
    description_list = list(description_dict.items())
    description_list.sort(key=lambda i: i[1])
    description_list = description_list[-10:]
    print('Топ 10 слов:\n')
    for i in description_list[::-1]:
        print(f'{i[0]} - {i[1]}')
    print()

def xml_def():
    import xml.etree.ElementTree as ET
    tree = ET.parse("newsafr.xml")
    root = tree.getroot()
    items = root.findall("channel/item")
    description = []
    for i in range(len(items)):
        description += items[i][2].text.split()
    top_list(description)

def json_def():
    json_data = {}
    with open("newsafr.json", encoding="utf-8") as f:
        json_data = json.load(f)
    news_list = []
    for key, values in json_data.items():
        news_list = values['channel']['items']
    description = []
    for news in range(len(news_list)):
        description += news_list[news]['description'].split()
    top_list(description)

main()