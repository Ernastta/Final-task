  # main.py
import argparse
from parser import TelegramParser
from analyzer import TextAnalyzer
from exporter import CSVExporter
from timeline import TimelineCreator  # <-- импорт


def main():
      parser = argparse.ArgumentParser(
          description="Telegram News Channels Analyzer"
      )
      parser.add_argument(
          "input", type=str, help="Path to HTML file or folder with HTML files"
      )
      parser.add_argument(
          "output", type=str, help="Path to output CSV file"
      )
      parser.add_argument(
          "--timeline", type=str, help="Path to save timeline CSV file"
      )
      parser.add_argument(
          "--model",
          type=str,
          default="tfidf",
          help="Type of model to use: tfidf, topic, zero-shot",
      )
      parser.add_argument(
          "--weights",
          type=str,
          help="Path to file with weights for model",
      )
      parser.add_argument(
         "--plot", type=str, help="Path to save plot image"
      )
      args = parser.parse_args()

      try:
          # 1. Парсинг
          tg_parser = TelegramParser()
          messages = tg_parser.parse(args.input)

          # 2. Анализ
          analyzer = TextAnalyzer(model_type=args.model, weights_path=args.weights)
          analyzed_messages = analyzer.analyze_messages(messages)

          # 3. Экспорт
          exporter = CSVExporter()
          exporter.export(analyzed_messages, args.output)

          # 4. Timeline
          if args.timeline:
             timeline_creator = TimelineCreator()
             timeline = timeline_creator.create_timeline(analyzed_messages)
             exporter.export(timeline, args.timeline)
             if args.plot:
                  timeline_creator.visualize_timeline(timeline, args.plot)

          print("Analysis complete!")
      except Exception as e:
          print(f"An error occurred: {e}")


if __name__ == "__main__":
      main()