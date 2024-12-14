# exporter.py
import csv

class CSVExporter:
    """
    Класс для экспорта результатов анализа в CSV файл.
    """

    def __init__(self):
        pass

    def export(self, data: list[dict], output_path: str):
        """
        Сохраняет список словарей в CSV файл.
        """
        if not data:
            print("Warning: No data to export to CSV.")
            return

        try:
             with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
                fieldnames = data[0].keys() # Заголовки из первого словаря
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader() # Записать заголовки
                writer.writerows(data) # Записать данные
             print(f"Data successfully exported to {output_path}")

        except Exception as e:
           print(f"Error exporting data to CSV: {e}")