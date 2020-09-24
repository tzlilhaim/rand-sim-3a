from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)
    
    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)

def count_articles(key,value):
    count = len(filter_CSV(key,value))
    return count

def is_article(key,value):
    isExist = True if count_articles(key,value) else False
    return isExist

def longest_article(key,value):
    articles = filter_CSV(key,value)
    longest = max(articles, key=lambda x:x['pages'])
    return longest

# def get_mapped_by_field():
#     reader = CSV_Manager("./articles.csv")
#     articles = reader.get_csv_as_dicts()
#     mapped = reader.map_by_field()
#     return articles

print("Articles with a title of t4:")
print(filter_CSV("title", "t4"))
print('')
print("Articles of a1 author:")
print(filter_CSV("author", "a1"))
print(count_articles('title', 't4'))
print(count_articles("author", "a1"))
print(is_article('title', 't4'))
print(is_article('title', 't100'))
print(longest_article("author", "a1"))
#print(get_mapped_by_field())