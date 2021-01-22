import json
import os


directory = os.getcwd()

reddit_locations = open(directory + r'\locations\reddit_locations.json', 'r+', encoding='utf-8-sig')
saved_locations = json.load(reddit_locations)
reddit_locations.close()


def goSearchTags():
    for location in saved_locations:
        for tag in location['tags']:
            if tag.lower() == 'park':
                print(location["title"])


def goSearchCountry(*args):
    if args != None:
        for location in saved_locations:
            if location.lower() == args.lower():
                goSearchTags()


goSearch()