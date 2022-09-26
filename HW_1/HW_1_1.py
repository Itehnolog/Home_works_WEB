import pickle
import json
from abc import ABC, abstractmethod


class SerializationInterface(ABC):  # abstract base class

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass


class SerializeJson(SerializationInterface):  # serialization to(from) json

    def serialize(self, filename, data):
        with open(filename, "w") as f:
            json.dump(data, f)
        return f"data {data} dumped to {filename}"

    def deserialize(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return f"data {data} loaded from {filename}"


class SerializeBin(SerializationInterface):  # serialization to(from) bin

    def serialize(self, filename, data):
        with open(filename, "wb") as f:
            pickle.dump(data, f)
        return f"data {data} dumped to {filename}"

    def deserialize(self, filename):
        with open(filename, "rb") as f:
            data = pickle.load(f)
        return f"data {data} loaded from {filename}"


list_examle = ["45", "some_text", [1, 2], 34567,
               {"some_key": "some_value"}, (123, 456)]

json_method = SerializeJson()
print(json_method.serialize("test.json", list_examle))
print("_"*100)
print(json_method.deserialize("test.json"))
print("_"*100)
pickle_method = SerializeBin()
print(pickle_method.serialize("test.dump", list_examle))
print("_"*100)
print(pickle_method.deserialize("test.dump"))
