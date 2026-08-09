import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_financial_news(api_key=None, ticker="AAPL"):
    """Fetches news headlines. Uses mock data if no API key is provided."""
    if api_key:
        url = f"https://finnhub.io/api/v1/company-news?symbol={ticker}&from=2023-08-01&to=2023-08-10&token={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return [article['headline'] for article in response.json()]
        else:
            print("Failed to fetch data. Check API key.")
            return []
    else:
        return [
            "Tech stocks rally as inflation data cools down",
            "Federal reserve signals potential rate hikes next quarter",
            "Supply chain bottlenecks cause massive revenue drop for major retailers",
            "New AI breakthroughs promise record profits for semiconductor industry",
            "Market volatility spikes amid global geopolitical tensions"
        ]

def analyze_sentiment(headlines):
    """Calculates sentiment scores for a list of headlines."""
    results = []
    for headline in headlines:
        scores = analyzer.polarity_scores(headline)
        
        if scores['compound'] >= 0.05:
            label = "Positive"
        elif scores['compound'] <= -0.05:
            label = "Negative"
        else:
            label = "Neutral"
            
        results.append({
            "Headline": headline,
            "Compound_Score": scores['compound'],
            "Sentiment": label
        })
        
    return pd.DataFrame(results)

if __name__ == "__main__":
    print("--- Running Market Sentiment Engine ---")
    
    headlines = get_financial_news(api_key=None) 
    
    sentiment_df = analyze_sentiment(headlines)
    
    print("\nRecent Market Headlines Analysis:")
    print(sentiment_df.to_string(index=False))
    
    # Save to CSV to prove dashboarding/reporting capabilities
    sentiment_df.to_csv("market_sentiment_output.csv", index=False)
    print("\nData successfully exported to market_sentiment_output.csv")
