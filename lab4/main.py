import csv
import yaml
from strategies import ConsoleStrategy, RedisStrategy, KafkaStrategy

def get_strategy_from_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    target = config.get("output_type", "console")
    
    strategies = {
        "console": ConsoleStrategy(),
        "redis": RedisStrategy(),
        "kafka": KafkaStrategy()
    }
    return strategies.get(target, ConsoleStrategy())

def process_data():
    strategy = get_strategy_from_config()
    dataset_file = "animals.csv"
    
    try:
        with open(dataset_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Normalizing keys to handle different CSV formats
                row_lower = {k.lower().replace(" ", "_"): v for k, v in row.items()}
                
                # Extracting data based on common Variant 7 headers
                animal_id = row_lower.get('animal_id') or row_lower.get('impound_number') or "N/A"
                animal_name = row_lower.get('animal_name') or row_lower.get('name') or "Unknown"
                animal_type = row_lower.get('animal_type') or "Other"
                intake_type = row_lower.get('intake_type') or "Unknown"

                record = (f"ID: {animal_id}, "
                         f"Name: {animal_name}, "
                         f"Type: {animal_type}, "
                         f"Status: {intake_type}")
                
                # Pattern Requirement: Output is separated from data reading [cite: 5, 6]
                strategy.save(record)
                
    except FileNotFoundError:
        print(f"Error: {dataset_file} not found.")

if __name__ == "__main__":
    process_data()