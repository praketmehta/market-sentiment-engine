# Market Sentiment Engine

A natural language processing pipeline designed to analyze real-time financial news headlines and quantify market sentiment. This tool helps identify broader market trends and shifts in investor confidence by converting qualitative news into actionable quantitative metrics.

## Features
* **Real-Time Data Extraction:** Integrates with the Finnhub API to fetch the latest financial headlines for specific stock tickers.
* **NLP Sentiment Scoring:** Utilizes the VADER (Valence Aware Dictionary and sEntiment Reasoner) library to calculate compound polarity scores (Positive, Negative, Neutral).
* **Automated Reporting:** Aggregates sentiment data and exports it into a structured CSV format for further dashboarding or time-series analysis.

## Tech Stack
* **Python 3.x**
* **VADER Sentiment** (NLP)
* **Pandas** (Data Manipulation)
* **Requests** (API Integration)
