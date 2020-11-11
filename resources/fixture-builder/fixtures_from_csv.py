import csv
import sys
import json

def csv_to_dict(csv_file):
    """
    @csv_file: file
    @returns: array
    This method extracts info from a field on a csv
    It returns an array of dicts 
    containing the info
    """
    final_array = []
    reader = csv.DictReader(csv_file)
    emotions = "emotions"
    categories = "categories"
    pk = 1
    for row in reader:
        emotion = row[emotions]
        category = row[categories]

        fixture = {
            "pk": pk,
            "model": "reviews.emotion",
            "fields": {
                "name": str(emotion),
                "category": int(category)
            }
        }
        
        final_array.append(fixture)
        pk = pk +1
        
    return final_array

csv_file = open('resources/fixture-builder/emotions.csv', 'r', encoding='utf-8-sig')
list_of_dicts = csv_to_dict(csv_file)


with open('reviews/fixtures/emotions.json', 'w') as json_file:
    json.dump(list_of_dicts, json_file)