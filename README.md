# Telegram News Channels Analyzer

Это приложение Python для анализа содержания новостных телеграм-каналов. Оно принимает на вход HTML-файл или папку с HTML-файлами, экспортированными из Telegram, и создает CSV-файл с результатами анализа, а также таймлайн и его визуализацию.

## Установка

1. Убедитесь, что у вас установлен Python 3.6+.
2. Установите зависимости:

```bash
pip install -r requirements.txt

## Использование

Для запуска приложения используйте следующую команду:

```bash
& C:/Users/.conda/envs/python311/python.exe c:/Desktop/main.py <input> <output> [--timeline <timeline>] [--plot <plot>] [--model <model>] [--weights <weights>]

## Где:

<input>: Путь к HTML-файлу или папке с HTML-файлами (обязательный параметр).

<output>: Путь к выходному CSV-файлу с результатами анализа (обязательный параметр).

--timeline <timeline>: Путь к выходному CSV-файлу с таймлайном (необязательный параметр).

--plot <plot>: Путь к файлу для сохранения графика таймлайна (необязательный параметр).

--model <model>: Тип модели для анализа текста (tfidf, bert, sentence, zero_shot, по умолчанию tfidf).

--weights <weights>: Путь к файлу с весами для модели (необязательный параметр).

## Пример:

& C:/Users/.conda/envs/python311/python.exe c:/Users/Desktop/main.py "C:/Users/Desktop/telegram_export.html" "C:/Users/Desktop/analysis_results.csv" --timeline "C:/Users/Desktop/timeline.csv" --plot "C:/Users/Desktop/timeline.png"

После запуска скрипта будут сгенерированы файлы analysis_results.csv, timeline.csv и timeline.png.

## Примеры использования

## Пример 1: Анализ одного HTML файла:

& C:/Users/.conda/envs/python311/python.exe c:/Users/Desktop/main.py "C:/Users/Desktop/telegram_export.html" "C:/Users/Desktop/analysis_results.csv"

Этот пример проанализирует telegram_export.html и сохранит результаты в analysis_results.csv.

## Пример 2: Анализ с таймлайном и графиком:

& C:/Users/.conda/envs/python311/python.exe c:/Users/Desktop/main.py "C:/Users/Desktop/telegram_export.html" "C:/Users//Desktop/analysis_results.csv" --timeline "C:/Users/Desktop/timeline.csv" --plot "C:/Users/Desktop/timeline.png"

Этот пример проанализирует telegram_export.html, сохранит результаты в analysis_results.csv, создаст таймлайн в timeline.csv и сгенерирует график в timeline.png.

## Скриншоты

!(Screenshots/screenshot__results.PNG)
!(Screenshots/screenshot_timeline_example.PNG)
!(Screenshots/screenshot_timeline.png)






