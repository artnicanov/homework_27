import json
import csv

ADS_MODEL = 'ads.ad'
USER_MODEL = 'users.user'
LOCATION_MODEL = 'users.location'
CATEGORIES_MODEL = 'ads.category'

ADS_JSON_FILE_NAME = 'ads.json'
USERS_JSON_FILE_NAME = 'users.json'
LOCATION_JSON_FILE_NAME = 'location.json'
CATEGORIES_JSON_FILE_NAME = 'categories.json'

def convert_to_json(csv_file, json_file, model):
	result = []
	with open(csv_file, encoding='utf-8') as csv_f:
		for row in csv.DictReader(csv_f):
			record = {'model': model}

			if model == ADS_MODEL:
				del row['Id']
			else:
				del row['id']

			if model == ADS_MODEL:
				row['price'] = int(row['price'])
				row['author_id'] = int(row['author_id'])
				row['category_id'] = int(row['category_id'])

				if row['is_published'] == "TRUE":
					row['is_published'] = True
				else:
					row['is_published'] = False

			if model == LOCATION_MODEL:
				row['lat'] = float(row['lat'])
				row['lng'] = float(row['lng'])

			if model == USER_MODEL:
				row['age'] = int(row['age'])
				row['location_id'] = int(row['location_id'])

			record['fields'] = row
			result.append(record)

	with open(json_file, 'w', encoding='utf-8') as json_f:
		json_f.write(json.dumps(result, ensure_ascii=False))

convert_to_json('location.csv', LOCATION_JSON_FILE_NAME, LOCATION_MODEL)
convert_to_json('user.csv', USERS_JSON_FILE_NAME, USER_MODEL)
convert_to_json('category.csv', CATEGORIES_JSON_FILE_NAME, CATEGORIES_MODEL)
convert_to_json('ad.csv', ADS_JSON_FILE_NAME, ADS_MODEL)
