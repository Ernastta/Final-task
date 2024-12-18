# analyzer.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split # <--  ADD
from sklearn.metrics import classification_report #  <-- ADD


class TextAnalyzer:
  

    def __init__(self, model_type='tfidf', weights_path=None):
       
        self.model_type = model_type
        self.weights_path = weights_path
        self.model = self._load_model()
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.is_fitted = False


    def _load_model(self):
       
         if self.model_type == 'tfidf':
             model = Pipeline([
                 ('tfidf', TfidfVectorizer(ngram_range=(1, 2), max_features=5000)),
                 ('clf', LogisticRegression(random_state=42, solver='liblinear'))
             ])
          
             if self.weights_path:
                 try:
                     weights_df = pd.read_csv(self.weights_path)
                     if 'feature' in weights_df.columns and 'weight' in weights_df.columns:
                         feature_names = weights_df['feature'].tolist()
                         feature_weights = weights_df['weight'].tolist()
                         feature_dict = {name: weight for name, weight in zip(feature_names, feature_weights)}
                         model.set_params(tfidf__vocabulary=feature_dict)

                     else:
                         print("Error: weights file must contain 'feature' and 'weight' columns")
                 except Exception as e:
                     print(f"Error loading weights: {e}")

             return model
         else:
            raise ValueError(f"Unsupported model type: {self.model_type}")


    def _get_sentiment(self, text: str) -> str:
       
        scores = self.sentiment_analyzer.polarity_scores(text)
        if scores['compound'] >= 0.05:
             return "POSITIVE"
        elif scores['compound'] <= -0.05:
              return "NEGATIVE"
        else:
           return "NEUTRAL"

    def _predict_category(self, text: str) -> str:
      
        if not self.is_fitted:
            return "unknown"
        try:
            return self.model.predict([text])[0]
        except Exception as e:
            print(f"Error predicting category: {e}")
            return "unknown"


    def analyze_messages(self, messages: list[dict]) -> list[dict]:
      
        analyzed_messages = []
        texts = [msg['text'] for msg in messages]
        if texts:
           # Учим модель
            try:
              labels = ["sport" , "disaster", "politics" , "other"]
              X_train, X_test, y_train, y_test = train_test_split(texts, [labels[i%len(labels)] for i in range(len(texts))], test_size=0.2, random_state=42)
              self.model.fit(X_train, y_train)
              self.is_fitted = True
            except Exception as e:
              print(f"Error training model: {e}")
              self.is_fitted = False
            
            for msg in messages:
                sentiment = self._get_sentiment(msg['text'])
                category = self._predict_category(msg['text'])
                analyzed_messages.append({
                   "date": msg['date'],
                   "text": msg["text"],
                   "semantic_tag": sentiment,
                   "label": category,
                })
        return analyzed_messages