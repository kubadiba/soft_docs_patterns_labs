from abc import ABC, abstractmethod

# Common interface for all output strategies
class OutputStrategy(ABC):
    @abstractmethod
    def save(self, data: str):
        pass

# Strategy 1: Console Output
class ConsoleStrategy(OutputStrategy):
    def save(self, data: str):
        print(f"[CONSOLE]: {data}")

# Strategy 2: Redis Output (Mock implementation)
class RedisStrategy(OutputStrategy):
    def save(self, data: str):
        # Logic to send data to Redis cache
        print(f"[REDIS]: Saving to cache -> {data[:60]}...")

# Strategy 3: Kafka Output (Mock implementation)
class KafkaStrategy(OutputStrategy):
    def save(self, data: str):
        # Logic to produce message to Kafka topic
        print(f"[KAFKA]: Producing to 'animal_data_topic' -> {data[:60]}...")