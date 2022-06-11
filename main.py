import json
import requests

url = 'https://api.itsukaralink.jp/v1.2/events.json'
fn = 'events.json'
rawdata = requests.get(url).content
with open(fn ,mode='wb') as f: # wb でバイト型を書き込める
  f.write(rawdata)

f = open('events.json', 'r', encoding='utf-8')
json_dict = json.load(f)


output = open('output.txt', 'w')

date = input('YYYY-MM-DD の形式で日付を入力してください。（例: 2022-06-10）')

for index, title in enumerate(json_dict['data']['events']):
    if '2022-06-11' in json_dict['data']['events'][index]['start_date'] :
        livers_other = ''
        name = json_dict['data']['events'][index]['name']
        date = json_dict['data']['events'][index]['start_date']
        livers = json_dict['data']['events'][index]['livers'][0]['name']
        if len(json_dict['data']['events'][index]['livers']) != 1:
            livers_other = ';&size(25){他}'
        url = json_dict['data']['events'][index]['url']

        print('-' + date[11:13] + '時' + date[14:16] + '分～ &attachref(' + livers + '/face.png,nolink,25x25)'+ livers_other +'; [[' + livers + ':' + url + ']] at:YouTube', file=output)

print('Output Successfully!')





