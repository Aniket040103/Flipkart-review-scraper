from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import mysql.connector
import logging
import re

logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

# MySQL Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # Replace with your MySQL username
    password="Aniket@123",   # Replace with your MySQL password
    database="flipkart_reviews" # Your database name
)
cursor = conn.cursor()

def sanitize_table_name(name):
    """
    Converts a product name to a safe table name.
    """
    safe_name = re.sub(r'\W+', '_', name.lower())
    return f"{safe_name}_reviews"

@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "cPHDOP col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            commentboxes = prod_html.find_all('div', {'class': "RcXBOT"})
            
            # Sanitize the product name and create a dedicated table
            table_name = sanitize_table_name(searchString)
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS `{table_name}` (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                rating VARCHAR(10),
                comment_head VARCHAR(255),
                comment TEXT
            )
            """
            cursor.execute(create_table_query)
            conn.commit()

            reviews = []
            for commentbox in commentboxes:
                try:
                    name = commentbox.div.div.find_all('p', {'class': '_2NsDsF AwS1CA'})[0].text
                except:
                    name = 'No Name'
                    logging.info("name not found")

                try:
                    rating = commentbox.div.div.div.div.text
                except:
                    rating = 'No Rating'
                    logging.info("rating not found")

                try:
                    commentHead = commentbox.div.div.div.p.text
                except:
                    commentHead = 'No Comment Heading'
                    logging.info("comment heading not found")
                
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                except Exception as e:
                    custComment = 'No Comment'
                    logging.info(e)

                mydict = {
                    "Product": searchString,
                    "Name": name,
                    "Rating": rating,
                    "CommentHead": commentHead,
                    "Comment": custComment
                }
                reviews.append(mydict)

                # Insert data into the product-specific table
                try:
                    insert_query = f"""
                    INSERT INTO `{table_name}` (name, rating, comment_head, comment)
                    VALUES (%s, %s, %s, %s)
                    """
                    values = (name, rating, commentHead, custComment)
                    cursor.execute(insert_query, values)
                    conn.commit()
                except Exception as e:
                    logging.info(f"Error inserting data into MySQL: {e}")

            logging.info("Final reviews: {}".format(reviews))
            return render_template('result.html', reviews=reviews)

        except Exception as e:
            logging.info(e)
            return str(e)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
