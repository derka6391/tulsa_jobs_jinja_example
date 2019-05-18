# import things
from flask_table import Table, Col
from flask import Flask, render_template
from items import items_list
import json
f = open('items.json')
data = json.load(f)
f.close()

app = Flask(__name__)

@app.route('/')
def result():
        return render_template('result.html', data = data)

if __name__ == '__main__':
    app.run(debug=True)

# Or, equivalently, some dicts


# Or, more likely, load items from your database with something like
# items = ItemModel.query.all()

# Populate the table
#table = ItemTable(items)

# Print the html
#print(table.__html__())
# or just {{ table }} from within a Jinja template