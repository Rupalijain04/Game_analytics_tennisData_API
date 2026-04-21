# 🎾 Game Analytics: Unlocking Tennis Data with SportRadar API

## 📌 Project Overview

This project focuses on collecting, transforming, and analyzing real-time tennis data using the **SportRadar Tennis API**. Since no static dataset was provided, data was extracted directly from API endpoints, converted into structured tables, and prepared for further SQL analysis and dashboard creation.

The project demonstrates an end-to-end workflow involving:

* API Integration
* Data Extraction
* JSON Transformation
* Data Cleaning
* CSV/Database Ready Tables
* Sports Analytics Insights

---

## 🎯 Objective

To build a structured tennis analytics dataset using live API data and prepare it for business insights, reporting, and dashboard development.

---

## 🛠️ Tools & Technologies Used

* **Python**
* **Pandas**
* **Requests Library**
* **CSV**
* **MySQL / PostgreSQL** (for further analysis)
* **Streamlit** (for dashboard development)

---

## 🔗 API Source

Data was collected using the **SportRadar Tennis API**.

Endpoints used:

1. Competitions
2. Complexes
3. Rankings

---

## 📂 Project Workflow

1. Generated API key from SportRadar.
2. Integrated API using Python requests library.
3. Fetched JSON data from multiple endpoints.
4. Explored nested JSON structure.
5. Converted raw JSON into structured tables using pandas.
6. Handled missing fields and inconsistent data.
7. Saved final datasets into CSV files.
8. Prepared data for SQL analysis and dashboarding.

---

## 📊 Tables Created

### 1. Competitions Table

* competition_id
* competition_name
* parent_id
* type
* gender
* category_id

### 2. Categories Table

* category_id
* category_name

### 3. Complexes Table

* complex_id
* complex_name

### 4. Venues Table

* venue_id
* venue_name
* city
* country
* timezone
* complex_id

### 5. Rankings Table

* rank
* movement
* points
* competitions_played
* competitor_id

### 6. Competitors Table

* competitor_id
* name
* country
* country_code
* abbreviation

---

## 🔍 Key Challenges Faced

### 1. No Dataset Provided

Resolved by collecting live data directly from APIs.

### 2. Nested JSON Structure

Flattened complex nested objects into relational tables.

### 3. Missing Fields

Used safe methods like `.get()` to avoid runtime errors.

### 4. API Errors / Invalid Routes

Handled using documentation review and debugging.

### 5. File Permission Errors

Resolved by checking file access and save locations.

---

## 📈 Business Use Cases

* Competition hierarchy analysis
* Venue and location analysis
* Country-wise player analysis
* Ranking trends
* Sports event exploration
* Dashboard reporting

---

## 🚀 Key Learnings

* Real-time API integration
* Working with nested JSON data
* Data cleaning and transformation
* Building relational datasets
* Error handling and debugging
* Preparing data for analytics dashboards

---

## 📁 Project Files

* `competitions.csv`
* `categories.csv`
* `complexes.csv`
* `venues.csv`
* `rankings.csv`
* `competitors.csv`
* `api_scripts.py`

---

## 💼 My Contribution

I worked on the **API Integration and Data Extraction** part of the project. My responsibilities included:

* Connecting to SportRadar API
* Fetching real-time data
* Transforming nested JSON into structured tables
* Handling missing values and inconsistencies
* Exporting final datasets for the team

---

## 🔮 Future Enhancements

* SQL Database Integration
* Streamlit Dashboard
* Automated Daily Data Refresh
* Advanced Sports Insights
* Interactive Visualizations

---

## 🙌 Conclusion

This project provided hands-on experience in real-world data engineering and analytics by transforming raw sports API data into structured business-ready datasets.

---

Thanks for visiting this project ⭐
