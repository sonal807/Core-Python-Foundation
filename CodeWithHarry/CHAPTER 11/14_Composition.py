#Composition: Composition is an OOP concept in which one class contains an object of another class as a part of itself. 
#It represents a “has-a” relationship, where one object is composed of other objects.

#Inheritance = IS-A
#Composition = HAS-A

class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()  #object of class Engine, this line is basically saying “Car HAS-A Engine.”

    def start_car(self):
        self.engine.start()  #Engine object is in self.engine, so we can call Engine class method
        print("Car Started")

car = Car()

car.start_car()

#Composition vs Inheritance:
#Inheritance represents an “IS-A” relationship, while Composition represents a “HAS-A” relationship.
#Inheritance allows a class to reuse or extend another class, whereas Composition allows a class to contain and use objects of another class
#Inheritance shows the relationship between calsses (Parent-Child realtionship), whereas Compostions is the relationship between objects(Object-containing realtionship)

#Inheritance → IS-A
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle): #Car, Vehicle se inherit kar raha hai. Car IS-A Vehicle
    pass

car = Car()
car.start()

#Composition → HAS-A
class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()  #Car ke andar Engine ka object hai.Car HAS-A Engine

car = Car()

car.engine.start()

#AI systems mein Composition bahut common hoti hai—jaise ek AI pipeline 
#ke andar model + tokenizer + retriever + logger ke objects ho sakte hain.

#Composition is used to build a larger class by combining objects of other classes. 
#The containing class uses these objects to perform its tasks

#Example:
class Tokenizer:
    def tokenize(self, text):
        return text.split()

class AIModel:
    def predict(self, tokens):
        print(f"Model is predicting using: {tokens}")

class AISystem:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.model = AIModel()

    def predict(self, text):
        tokens = self.tokenizer.tokenize(text)
        self.model.predict(tokens)

system = AISystem()

system.predict("Python is easy")

#Example:
class CPU:
    def process(self):
        print("CPU is processing")

class Computer:
    def __init__(self):
        self.cpu = CPU()

    def start(self):
        self.cpu.process()
        print("Computer Started")

com = Computer()

com.start()

#Composition — Real-World / AI Engineer Use Case
#Composition is commonly used in software systems to combine multiple independent components into one larger system.
#Each component handles a specific responsibility, while the main class coordinates them.

#Example:
class Preprocessor:
    def clean(self, data):
        print(f"Cleaning data: {data}")
        return data

class Model:
    def predict(self, data):
        print(f"Predicting using: {data}")
        return "Positive"

class Logger:
    def log(self, result):
        print(f"Result: {result}")

class AISystem:
    def __init__(self):
        self.preprocessor = Preprocessor()
        self.model = Model()
        self.logger = Logger()

    def run(self, data):
        data = self.preprocessor.clean(data)
        result = self.model.predict(data)
        self.logger.log(result)

ai = AISystem()

ai.run("User input")

#Example:
class Tokenizer:
    def tokenize(self, text):
        print(f"Tokenizing: {text}")
        return text.split()

class Model:
    def predict(self, tokens):
        print("Model is predicting")

class AIApplication:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.model = Model()

    def run(self, text):
        tokens = self.tokenizer.tokenize(text)
        self.model.predict(tokens)

ai = AIApplication()
ai.run("Hello! World")