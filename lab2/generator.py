import csv
import random

class DataGenerator:
    @staticmethod
    def generate(filename="data.csv", count=1100):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['course_id', 'title', 'price'])
            for i in range(count):
                writer.writerow([
                    f"CRS-{i:04}", 
                    f"Online Course Vol {i}", 
                    round(random.uniform(9.99, 199.99), 2)
                ])
        print(f"Success: Generated {count} rows in {filename}")

if __name__ == "__main__":
    DataGenerator.generate()