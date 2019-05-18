from flask_table import Table, Col
from flask import Flask, render_template

# Declare your table
class ItemTable(Table):
    title = Col('title')
    date = Col('date')
    link = Col('link')
    location = Col('location')

# Get some objects
class Item(object):
    def __init__(self, title, date, link, location):
        self.title = title
        self.date = date
        self.link = link
        self.location = location


items_list = []
#for x in range(5):
 #           items_list.append(dict(title='title' + str(x), date='date' + str(x), link='link' + str(x), location='location' + str(x)))