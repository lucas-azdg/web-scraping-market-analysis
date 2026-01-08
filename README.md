📊 Automated Market Pricing & Competitor Analysis
Web Scraping | Data Cleaning | Business Intelligence

📌 Project Overview
This project demonstrates an end-to-end data pipeline. It starts by extracting live data from a retail website using Python, continues with a robust data cleaning process to handle encoding issues and currency formats, and concludes with an interactive Power BI dashboard for market intelligence.

🛠️ Tech Stack
Python 3.14 (Data Extraction & Processing)

BeautifulSoup4 & Requests (Web Scraping)

Pandas & Regular Expressions (Re) (Data Engineering)

Power BI (Data Visualization & UI/UX)

⚡ Key Technical Challenges
Dynamic Data Cleaning: Developed a custom cleaning function using Regular Expressions (Regex) to strip non-numeric characters and fix encoding bugs (e.g., removing ghost characters like Â).

Automation: Created a script that transforms raw, unstructured HTML into a structured .csv format ready for analysis.

📈 Dashboard Insights
The Power BI report focuses on three critical retail areas:

Price Concentration: Using Bins, I identified that most products are clustered in the $20-$40 range.

Inventory Health: A real-time breakdown of "In Stock" vs. "Out of Stock" items.

Premium Benchmarking: Identification of the highest-priced items to understand the competitor's upper-tier strategy.

📂 Repository Structure
main.py: The complete Python engine for scraping and cleaning.

market_data_cleaned.csv: The final dataset used for the dashboard.

Market_Analysis_Report.pbix: The Power BI source file.

🚀 How to Run
Clone the repo.

Install dependencies: pip install requests beautifulsoup4 pandas.

Run python main.py to generate the latest data.

Open the .pbix file to explore the interactive visuals.
