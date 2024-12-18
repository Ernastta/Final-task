# timeline.py
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date, datetime


class TimelineCreator:
   

    def __init__(self):
        pass

    def create_timeline(self, analyzed_messages: list[dict]) -> list[dict]:
        
        timeline = []
        messages_by_date = {}

        for msg in analyzed_messages:
            if msg["date"] is not None:
                date_obj = msg["date"].date()
                if date_obj not in messages_by_date:
                    messages_by_date[date_obj] = []
                messages_by_date[date_obj].append(msg)

        for date_obj, messages in messages_by_date.items():
            semantic_sum = 0
            labels = []
            for msg in messages:
                if msg['semantic_tag'] == "POSITIVE":
                    semantic_sum += 1
                elif msg['semantic_tag'] == "NEGATIVE":
                    semantic_sum -= 1

                labels.append(msg['label'])

            label_counts = Counter(labels)
            most_common_label = label_counts.most_common(1)[0][0] if label_counts else "unknown"

            timeline.append({
                "date": date_obj.strftime("%Y/%m/%d"),
                "semantic_tag": semantic_sum,
                "label": most_common_label
            })

        return timeline

    def visualize_timeline(self, timeline: list[dict], output_path: str):
          """
          Визуализирует таймлайн.
          """
          dates = [datetime.strptime(item['date'], "%Y/%m/%d").date() for item in timeline]
          semantic_tags = [item['semantic_tag'] for item in timeline]
          labels = [item["label"] for item in timeline]
          
          fig, ax = plt.subplots(figsize=(12, 6))
          ax.bar(dates, semantic_tags, label="Semantic Tag")
          
          ax.set_xlabel("Date")
          ax.set_ylabel("Semantic Tag Sum")
          ax.set_title("Timeline Visualization")
          ax.xaxis.set_major_locator(mdates.AutoDateLocator())
          ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
          ax.tick_params(axis="x", rotation=45)

          # Add labels to the plot
          for i, txt in enumerate(labels):
            ax.annotate(txt, (dates[i], semantic_tags[i]), textcoords="offset points", xytext=(0, 5), ha='center')

          plt.tight_layout()
          plt.savefig(output_path, dpi=300)
          plt.close(fig)