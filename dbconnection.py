#!/usr/bin/python3
import os
import pymongo

clientIP = os.system('echo $CLIENT_IP_ADDRESS')

client = pymongo.MongoClient(str(clientIP))
database = client['project']
user_collection = database['users']


def match_email(email):
    matching_mail = user_collection.find_one({"mail": email})
    print(matching_mail)
    return matching_mail


def register_user(email, name, surname):
    user_collection.insert_one(
        {"mail": email, "name": name, "surname": surname})


def read_users():
    users_list = []
    users_data = user_collection.find({})
    for el in users_data:
        users_list.append(el)
    return users_list
