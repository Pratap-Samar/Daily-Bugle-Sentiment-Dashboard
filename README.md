# 📰 The Daily Bugle Report: A Spider-Man Sentiment Analysis Dashboard

### [Live Demo Link](https://daily-bugle-sentiment-dashboard-ahjgl6kbfpxtexzshgwgag.streamlit.app/)


Full Stack Data Science Project that scrapes, analyzes, and visualizes fan sentiment for iconic Spider-Man comic book storylines. It employs a full data pipeline to deliver a data-driven verdict on the web-slinger's most celebrated and controversial moments.



---
## 🧠 What I Learned
This project was a practical journey through the entire data science pipeline. The key takeaways were:

* **Data Source Vetting**: Learned the importance of evaluating potential data sources for completeness and structure, leading to a pivot from a Fandom Wiki to Wikipedia, which dramatically improved the quality of the foundational dataset.

* **Building Resilient Scrapers**: Developed robust web scrapers by implementing `User-Agent` headers to avoid being blocked and creating functions with fallback logic to handle inconsistent HTML structures.

* **Applied NLP for Human Language**: Utilized Natural Language Processing (NLP) techniques to normalize and clean search queries to match real-world language, which is essential for finding high-quality discussion data from APIs.

* **Data Storytelling through UI/UX**: Leveraged Streamlit and custom CSS not just to display data, but to create a themed, user-friendly experience that tells a clear story and makes insights accessible and engaging.

---
## 🚧 Challenges and Solutions
This project involved several data processing and visualization challenges. The final dashboard is the result of iteratively solving these problems.

#### Challenge: Incomplete Data Source
* **Problem**: The initial data source was missing pages and synopses for many iconic storylines.
* **Solution**: Pivoted to a more structured and comprehensive source (Wikipedia). This required rewriting the scraper but resulted in a much higher quality foundational dataset.

#### Challenge: Web Scraping Roadblocks
* **Problem**: The script was being blocked by servers, resulting in HTTP `403: Forbidden` errors.
* **Solution**: Implemented a `User-Agent` header in all `requests` calls to mimic a real browser and ensure consistent access to the web pages.

#### Challenge: Finding High-Quality Fan Comments
* **Problem**: Searching the Reddit API with official, formal titles yielded irrelevant results or posts with little discussion.
* **Solution**: Created a title-cleaning function to normalize search queries and upgraded the scraping logic to select the post with the highest comment count from the top 10 search results, ensuring the analysis was performed on the richest possible sample of fan opinion.

---
## 🤔 Limitations of the Analysis
While this project provides a strong quantitative measure of fan opinion, it's important to acknowledge its limitations to ensure accurate interpretation of the results.

* **Inherent Limitations of Sentiment Analysis**
    The VADER sentiment analysis model, while powerful, cannot understand complex human nuances.
    * **Sarcasm & Nuance:** The model can be easily fooled by sarcasm. A comment like, "Yeah, 'One More Day' was a *brilliant* story..." would be scored as highly positive when it is, in fact, critical.
    * **Emotional Context:** A story can have a low sentiment score not because it's "badly written," but because it's emotionally devastating (e.g., "The Night Gwen Stacy Died"). The numerical score doesn't distinguish between anger at a poor plot and sadness at a tragic, well-told one.

* **Challenges with Reddit Search Accuracy**
    The methodology of scraping the most-commented post based on a search query is effective but not perfect. The Reddit API's search function can sometimes return posts that are not directly about the specific comic book arc.
    * For example, a search for the comic **"Planet of the Symbiotes"** returned a popular thread where the comments were actually about Sony's *Venom* movies.
    * Similarly, a search for **"Brand New Day"** pulled comments about a recent Spider-Man movie that shared the same title, not the original 2008 comic storyline.

This means that for certain story arcs, the calculated sentiment score may not accurately reflect fan opinion on the comic itself.

---
## 🛠️ Technology Stack
* **Data Collection**: Python, `requests`, `BeautifulSoup4`, `praw` (Reddit API Wrapper)
* **Data Processing & Analysis**: `pandas`, `NLTK` (VADER for Sentiment Analysis)
* **Web Application & Frontend**: `Streamlit`, `HTML`, `CSS`
* **Environment**: Google Colab / Local Development

---
## 📂 Data & Reproducibility
The live demo of this application runs on a static data file (`spiderman_sentiment_data.csv`). This ensures the deployed app is always fast, stable, and does not depend on live API calls.

### Running with Fresh Data
If you would like to reproduce the analysis with the absolute latest data, you can run the data collection pipeline yourself.

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Set Up Environment**: Install the required Python libraries.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Notebook**: Open and run all the cells in the `The_Daily_Bugle(1).ipynb` Jupyter Notebook.

    > **Note**: To run the notebook successfully, you will need to provide your own Reddit API credentials in the relevant cells.

Running the notebook will execute the entire scraping and sentiment analysis process and will overwrite the existing `spiderman_sentiment_data.csv` with fresh data.

---
## 🏁 Setup and Local Execution
To run the Streamlit web application on your local machine:

1.  Ensure you have followed steps 1 and 2 from the section above (Clone Repo & Install Dependencies).
2.  Run the following command in your terminal:
    ```bash
    streamlit run app.py
    ```
