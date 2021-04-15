import requests
import json

language_dict = {
	'1': 'en', '2': 'ar', '3': 'zh', '4': 'fr', '5': 'de', '6': 'hi', '7': 'ga', '8': 'it',
	'9': 'ja', '10': 'ko', '11': 'pt', '12': 'ru', '13': 'es'
}

display = '''
1 - English    5 - German     9 - Japanese      13 - Spanish
2 - Arabic	   6 - Hindi      10 - Korean
3 - Chinese	   7 - Irish      11 - Portuguese
4 - French	   8 - Italian    12 - Russian
Для выхода из программы, наберите: !q
'''

print(display)
source_choice = str(input('Выберите цифру!\nC какого языка будем переводить: '))
target_choice = str(input('Выберите цифру!\nНА какой язык будем переводить: '))

url = 'https://libretranslate.com/translate'


def translation_text(text, source: str, target: str):
	r = requests.post(url, data=json.dumps({'q': text, 'source': language_dict[source], 'target': language_dict[target]}), headers={'Content-Type': 'application/json'})
	sc = r.status_code
	data = r.json()
	if sc != 200:
		print('Что-то пошло не так')
	else:
		print(data['translatedText'])


while True:
	t = str(input('Что будем переводить: '))
	if t == '!q':
		exit()
	else:
		translation_text(t, source_choice, target_choice)