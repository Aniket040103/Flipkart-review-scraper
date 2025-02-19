# Flipkart Review Scraper

![Flipkart Scraper](https://img.shields.io/badge/Web%20Scraping-Flipkart-blue) ![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen) ![Flask](https://img.shields.io/badge/Flask-Web%20Framework-red)

## 📌 Project Overview
This **Flipkart Review Scraper** is a web application built using **Flask** that scrapes product reviews from Flipkart and stores them in an **SQL database**. Users can enter a product name, and the scraper fetches reviews, including the **customer name, rating, review title, and comment**.

## ✨ Features
- 🔍 **Scrapes Flipkart product reviews** using `BeautifulSoup`.
- 💾 **Stores reviews in a MySQL database**, creating a separate table for each product.
- 🖥 **Web-based UI** using Flask and HTML templates.
- 📜 **Logs errors and activities** using Python's logging module.

## 🛠 Tech Stack
- **Backend:** Flask, Python
- **Web Scraping:** BeautifulSoup, requests
- **Database:** MySQL
- **Frontend:** HTML, Bootstrap
- **Version Control:** Git & GitHub

## 🚀 Installation & Setup
Follow these steps to set up and run the project:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Aniket040103/Flipkart-review-scraper.git
cd Flipkart-review-scraper
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL Database
- Create a MySQL database (e.g., `review_scraper`).
- Update `config.py` or modify `app.py` to include your MySQL credentials.

### 5️⃣ Run the Application
```bash
python app.py
```
Access the web app at **http://127.0.0.1:5000/**.

## 📂 Project Structure
```
Flipkart-review-scraper/
│-- templates/         # HTML templates
│-- static/            # CSS & JS files
│-- app.py             # Flask main application
│-- db_config.py       # Database connection setup
│-- scrapper.py        # Web scraping logic
│-- requirements.txt   # Python dependencies
│-- README.md          # Project documentation
```

## 🛠 Future Enhancements
- 📊 **Add data visualization** for review analysis.
- 📜 **Store reviews in a NoSQL database** like MongoDB.
- 🔄 **Automate daily scraping** and store historical trends.

## 🤝 Contributing
Pull requests and feature suggestions are welcome! 🎯

## 📬 Contact
- **Developer:** Aniket Pawar
- **GitHub:** [Aniket040103](https://github.com/Aniket040103)
- **Email:** aniketpawar040103@example.com

---
⭐ **If you like this project, don't forget to star the repo!** ⭐
