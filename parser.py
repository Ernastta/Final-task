# parser.py
from bs4 import BeautifulSoup
import os
from datetime import datetime
import re


class TelegramParser:
    
    def __init__(self):
        pass

    def _parse_html_file(self, file_path: str) -> list[dict]:
       
        messages = []
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")

            message_blocks = soup.find_all("div", class_="message")

            for block in message_blocks:
                # Поиск блока с текстом сообщения
                text_block = block.find("div", class_="text")
                if not text_block:
                    continue  # Пропускаем, если нет текстового сообщения
                text = text_block.get_text(strip=True)

                date_block = block.find("div", class_="date")
                if not date_block:
                    continue  # Пропускаем, если нет блока с датой
                date_time_str = date_block.get('title')

                if date_time_str:
                    date_time_obj = None
                    match = re.match(r'(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', date_time_str)
                    if match:
                       date_time_str_without_tz = match.group(1)
                       date_time_obj = datetime.strptime(date_time_str_without_tz, '%d.%m.%Y %H:%M:%S')
                else:
                    date_time_obj = None


                messages.append(
                    {
                        "date": date_time_obj,
                        "text": text,
                    }
                )
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
        except Exception as e:
            print(f"Error parsing file {file_path}: {e}")

        return messages

    def parse(self, input_path: str) -> list[dict]:
      
        all_messages = []

        if os.path.isdir(input_path):
            for filename in os.listdir(input_path):
                if filename.endswith(".html"):
                    file_path = os.path.join(input_path, filename)
                    messages = self._parse_html_file(file_path)
                    all_messages.extend(messages)
        elif os.path.isfile(input_path) and input_path.endswith(".html"):
            messages = self._parse_html_file(input_path)
            all_messages.extend(messages)
        else:
            print(f"Error: Invalid input path: {input_path}")

        return all_messages