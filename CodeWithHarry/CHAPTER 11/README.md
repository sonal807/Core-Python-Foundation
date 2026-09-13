# 📘 Chapter 11 - OOP Advanced

## 🎯 Objective

The objective of this chapter is to learn the **advanced concepts of Object-Oriented Programming (OOP) in Python**.

In the previous chapter, we learned the fundamentals of OOP, including:

- Classes
- Objects
- Attributes
- Instance Attributes
- Class Attributes
- Methods
- `self`
- `__init__()`
- Static Methods

In this chapter, we move from basic OOP concepts to more advanced techniques used to design **flexible, reusable, maintainable, and scalable Python programs**.

The major concepts covered in this chapter include:

- Inheritance
- `super()`
- Method Resolution Order (MRO)
- `@classmethod`
- Property Decorators
- Operator Overloading
- Encapsulation
- Polymorphism
- Abstraction
- Composition

These concepts form an important foundation for advanced Python programming and are widely used in large software systems and Python libraries.

---

# 📌 Topics Covered

1. Inheritance
   - Basic Concept
   - Single Inheritance
   - Multiple Inheritance
   - Multilevel Inheritance
   - Hierarchical Inheritance
   - Hybrid Inheritance

2. `super()`
   - Basic Concept
   - Calling Parent Methods
   - Calling Parent Constructor
   - `super()` with Multiple Inheritance

3. Method Resolution Order (MRO)
   - Basic Concept
   - MRO in Single Inheritance
   - MRO in Multiple Inheritance
   - C3 Linearization
   - `super()` with MRO

4. `@classmethod`
   - Basic Concept
   - `cls`
   - Working with Class Attributes
   - Alternative Constructors

5. Property Decorators
   - `@property`
   - Getter
   - Setter
   - Deleter
   - Getter + Setter + Deleter Patterns

6. Operator Overloading
   - Basic Concept
   - Arithmetic Operators
   - Comparison Operators
   - `__str__()`
   - `__len__()`
   - Practical Examples

7. Encapsulation
   - Basic Concept
   - Access Modifiers
   - Public Members
   - Protected Members
   - Private Members
   - Private Variables
   - Name Mangling
   - Getters
   - Setters
   - Setter Validation
   - Property Decorators and Encapsulation

8. Polymorphism
   - Basic Concept
   - Method Overriding
   - Method Overriding with `super()`
   - Duck Typing
   - Method Overloading
   - Default Arguments
   - `*args`
   - `**kwargs`
   - Built-in Function Polymorphism

9. Abstraction
   - Basic Concept
   - Abstract Class
   - `ABC`
   - `@abstractmethod`
   - Complete Working
   - Rules and Important Behavior
   - `raise NotImplementedError`
   - Practical Example
   - Abstraction vs Encapsulation

10. Composition
    - Basic Concept
    - Basic Working
    - Composition vs Inheritance
    - Practical Example
    - AI Engineer Use Case

---

# 🧬 1. Inheritance

## 🧠 What is Inheritance?

**Inheritance** is an OOP concept that allows one class to acquire properties and behavior from another class.

The class whose properties and methods are inherited is commonly called the:

```text
Parent Class
```

The class that inherits from it is commonly called the:

```text
Child Class
```

Other commonly used terms are:

```text
Parent → Base Class / Superclass

Child → Derived Class / Subclass
```

Inheritance promotes **code reuse** because the child class can use functionality already defined in the parent class.

---

# ❓ Why Do We Need Inheritance?

Suppose we have:

```python
class Animal:

    def eat(self):
        print("Animal is eating.")
```

Now suppose we want classes such as:

```text
Dog
Cat
Horse
```

All of them may need the `eat()` method.

Instead of writing the same method repeatedly:

```python
class Dog:

    def eat(self):
        print("Animal is eating.")


class Cat:

    def eat(self):
        print("Animal is eating.")
```

we can create a common parent class:

```python
class Animal:

    def eat(self):
        print("Animal is eating.")
```

and allow other classes to inherit from it:

```python
class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

Now both `Dog` and `Cat` can use `eat()`.

---

# ⭐ Advantages of Inheritance

Inheritance provides several benefits:

### 1. Code Reusability

Existing functionality can be reused instead of rewriting it.

### 2. Reduced Duplication

Common functionality can be placed in one parent class.

### 3. Better Organization

Related classes can be organized into a hierarchy.

### 4. Extensibility

A child class can add new attributes and methods.

### 5. Customization

A child class can override inherited behavior when required.

---

# 🧱 Basic Syntax of Inheritance

The basic syntax is:

```python
class ChildClass(ParentClass):
    # child class body
    pass
```

Example:

```python
class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    pass
```

Here:

```text
Animal → Parent Class
Dog    → Child Class
```

---

# 🐕 Creating an Object of the Child Class

```python
dog = Dog()

dog.eat()
```

Output:

```text
Animal is eating.
```

Although `eat()` is defined inside `Animal`, the `Dog` object can use it because `Dog` inherits from `Animal`.

---

# 🔗 Parent-Child Relationship

Inheritance can be visualized as:

```text
        Animal
           │
           │ inherits
           ↓
          Dog
```

The child receives accessible functionality from the parent.

---

# 1️⃣ Single Inheritance

**Single inheritance** occurs when one child class inherits from one parent class.

Structure:

```text
Parent
   ↓
Child
```

Example:

```python
class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")
```

Create an object:

```python
dog = Dog()

dog.eat()
dog.bark()
```

Output:

```text
Animal is eating.
Dog is barking.
```

The `Dog` class gets:

```text
eat()
```

from the parent and defines:

```text
bark()
```

itself.

---

# 🧠 Understanding Single Inheritance

In the example:

```python
class Animal:
```

is the parent class.

```python
class Dog(Animal):
```

means:

```text
Dog inherits from Animal
```

Therefore, a `Dog` object can access the methods available through the inheritance relationship.

---

# 📊 Single Inheritance Structure

```text
       Animal
      /      \
   eat()    ...
        ↓
       Dog
      /   \
   eat()  bark()
```

The child can use inherited functionality and can also provide its own functionality.

---

# 2️⃣ Multiple Inheritance

**Multiple inheritance** occurs when one child class inherits from more than one parent class.

Structure:

```text
Parent 1     Parent 2
    \          /
     \        /
      \      /
       Child
```

Example:

```python
class Father:

    def father_method(self):
        print("Father method")


class Mother:

    def mother_method(self):
        print("Mother method")


class Child(Father, Mother):
    pass
```

Now:

```python
child = Child()

child.father_method()
child.mother_method()
```

Output:

```text
Father method
Mother method
```

The `Child` class inherits from both:

```text
Father
Mother
```

---

# 🧩 Multiple Inheritance Syntax

```python
class Child(Parent1, Parent2):
    pass
```

Example:

```python
class Child(Father, Mother):
    pass
```

The order in the parentheses is important because it participates in Python's **Method Resolution Order (MRO)**.

MRO will be discussed in detail later in this chapter.

---

# 3️⃣ Multilevel Inheritance

**Multilevel inheritance** occurs when inheritance happens through multiple levels.

Structure:

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

Example:

```python
class Grandparent:

    def grandparent_method(self):
        print("Grandparent method")


class Parent(Grandparent):

    def parent_method(self):
        print("Parent method")


class Child(Parent):

    def child_method(self):
        print("Child method")
```

Now:

```python
child = Child()

child.grandparent_method()
child.parent_method()
child.child_method()
```

Output:

```text
Grandparent method
Parent method
Child method
```

The `Child` class can access inherited functionality from both levels above it.

---

# 🧠 Understanding Multilevel Inheritance

The relationship is:

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

The `Child` inherits from `Parent`.

`Parent` inherits from `Grandparent`.

Therefore, the child can access inherited functionality through the hierarchy.

---

# 📊 Multilevel Inheritance Example

```text
        Vehicle
           ↓
          Car
           ↓
        ElectricCar
```

For example:

```python
class Vehicle:

    def move(self):
        print("Vehicle is moving.")


class Car(Vehicle):

    def drive(self):
        print("Car is driving.")


class ElectricCar(Car):

    def charge(self):
        print("Electric car is charging.")
```

Now:

```python
car = ElectricCar()

car.move()
car.drive()
car.charge()
```

Output:

```text
Vehicle is moving.
Car is driving.
Electric car is charging.
```

---

# 4️⃣ Hierarchical Inheritance

**Hierarchical inheritance** occurs when multiple child classes inherit from the same parent class.

Structure:

```text
             Parent
            /      \
           ↓        ↓
        Child 1   Child 2
```

Example:

```python
class Animal:

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):

    def bark(self):
        print("Dog is barking.")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing.")
```

Now:

```python
dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()
```

Both `Dog` and `Cat` inherit from:

```text
Animal
```

---

# 🧠 Understanding Hierarchical Inheritance

The structure is:

```text
             Animal
             /    \
            /      \
          Dog      Cat
```

The common functionality belongs in the parent class.

Child-specific functionality belongs in the corresponding child class.

For example:

```text
Animal
  └── eat()

Dog
  └── bark()

Cat
  └── meow()
```

---

# 5️⃣ Hybrid Inheritance

**Hybrid inheritance** is a combination of two or more types of inheritance.

For example, a design may combine:

- Multiple inheritance
- Multilevel inheritance
- Hierarchical inheritance

A hybrid hierarchy can look like:

```text
          A
         / \
        B   C
         \ /
          D
```

Here:

```text
A → Parent of B and C

D → Inherits from B and C
```

This combines hierarchical and multiple inheritance.

Example:

```python
class A:

    def method_a(self):
        print("A")


class B(A):

    def method_b(self):
        print("B")


class C(A):

    def method_c(self):
        print("C")


class D(B, C):

    def method_d(self):
        print("D")
```

Now:

```python
obj = D()

obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()
```

Output:

```text
A
B
C
D
```

This example contains a combination of inheritance patterns.

---

# ⚠️ Diamond Inheritance

A common structure associated with multiple/hybrid inheritance is the **diamond-shaped inheritance hierarchy**.

Example:

```text
          A
         / \
        B   C
         \ /
          D
```

Here:

```text
D
```

inherits from both:

```text
B
C
```

and both `B` and `C` inherit from:

```text
A
```

The problem is that Python needs a consistent way to determine **which method should be used when the same method exists in multiple classes**.

This is where **Method Resolution Order (MRO)** becomes important.

Python uses **C3 linearization** to determine the MRO for such class hierarchies.

MRO will be covered in detail in a later section.

---

# 📊 Types of Inheritance

| Type | Structure | Description |
|---|---|---|
| Single | `A → B` | One parent and one child |
| Multiple | `A + B → C` | One child has multiple parents |
| Multilevel | `A → B → C` | Inheritance across multiple levels |
| Hierarchical | `A → B, C` | Multiple children share one parent |
| Hybrid | Combination | Combination of multiple inheritance patterns |

---

# 🧠 Quick Visual Revision

## Single Inheritance

```text
A
↓
B
```

---

## Multiple Inheritance

```text
A     B
 \   /
   C
```

---

## Multilevel Inheritance

```text
A
↓
B
↓
C
```

---

## Hierarchical Inheritance

```text
    A
   / \
  B   C
```

---

## Hybrid Inheritance

```text
    A
   / \
  B   C
   \ /
    D
```

---

# 🧩 Inheritance with Attributes

Inheritance is not limited to methods.

A child class can also access inherited attributes.

Example:

```python
class Animal:

    species = "Animal"

    def eat(self):
        print("Eating...")


class Dog(Animal):
    pass
```

Now:

```python
dog = Dog()

print(dog.species)
dog.eat()
```

Output:

```text
Animal
Eating...
```

The child object can access the inherited class attribute and method.

---

# 🧩 Inheritance with `__init__()`

Consider:

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass
```

Now:

```python
dog = Dog("Bruno")

print(dog.name)
```

Output:

```text
Bruno
```

The child class does not define its own `__init__()`, so the inherited initialization behavior can be used.

---

# ⚠️ What Happens When the Child Defines Its Own `__init__()`?

Suppose:

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

Now:

```python
dog = Dog("Bruno", "Labrador")
```

The child has its own `__init__()`.

Therefore, the parent's initialization method is not automatically executed simply because the classes are related.

If the child needs the parent's initialization logic, it can explicitly call it using:

```python
super()
```

Example:

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

Now:

```python
dog = Dog("Bruno", "Labrador")

print(dog.name)
print(dog.breed)
```

Output:

```text
Bruno
Labrador
```

The `super()` concept will be covered in detail in the next part.

---

# 🧠 Important Inheritance Concepts

When working with inheritance, remember these relationships:

```text
Parent Class
     ↓
Provides common functionality
     ↓
Child Class
     ↓
Inherits + Extends + Can Override
```

A child class can generally:

### 1. Use inherited methods

```python
child.parent_method()
```

### 2. Add new methods

```python
def child_method(self):
    ...
```

### 3. Add new attributes

```python
self.new_attribute = value
```

### 4. Override inherited methods

```python
def parent_method(self):
    ...
```

### 5. Call parent functionality

```python
super().parent_method()
```

---

# ⚖️ Inheritance vs Code Duplication

Without inheritance:

```python
class Dog:

    def eat(self):
        print("Eating")


class Cat:

    def eat(self):
        print("Eating")
```

The same logic is duplicated.

With inheritance:

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

The common functionality exists only once.

---

# 🌍 Real-Life Examples of Inheritance

Inheritance can be used when different entities have a genuine **"is-a" relationship**.

### 🚗 Vehicle Example

```text
Vehicle
 ├── Car
 ├── Bike
 └── Truck
```

A car is a vehicle.

---

### 🐾 Animal Example

```text
Animal
 ├── Dog
 ├── Cat
 └── Horse
```

A dog is an animal.

---

### 👨‍💼 Employee Example

```text
Employee
 ├── Developer
 ├── Manager
 └── Designer
```

A developer is an employee.

---

### 🏦 Banking Example

```text
Account
 ├── SavingsAccount
 └── CurrentAccount
```

Different account types can share common account functionality.

---

# ⚠️ Common Beginner Mistakes with Inheritance

## 1. Confusing Inheritance with Object Creation

This:

```python
class Dog(Animal):
```

defines an inheritance relationship.

This:

```python
dog = Dog()
```

creates an object.

They are different operations.

---

## 2. Forgetting Parentheses in Class Definition

Correct:

```python
class Dog(Animal):
    pass
```

---

## 3. Incorrectly Calling the Parent Constructor

If a child class defines its own `__init__()` and needs the parent's initialization logic, it should explicitly invoke the appropriate parent behavior, commonly using:

```python
super().__init__()
```

---

## 4. Overusing Inheritance

Not every relationship should be represented using inheritance.

Inheritance is generally appropriate when there is a meaningful:

```text
"is-a"
```

relationship.

For example:

```text
Dog is an Animal
```

makes sense.

But:

```text
Engine is a Car
```

does not.

An engine is a **part of** a car, which is a composition relationship.

Composition will be discussed later in this chapter.

---

# 💡 Best Practices for Inheritance

### 1. Keep Parent Classes General

The parent should contain functionality genuinely shared by its children.

### 2. Keep Child Classes Specific

Child classes should add or customize behavior specific to them.

### 3. Avoid Deep and Unnecessary Hierarchies

Very complicated inheritance structures can become difficult to understand.

### 4. Prefer Clear Relationships

Use inheritance when the relationship naturally represents:

```text
Child "is a" Parent
```

### 5. Use `super()` When Appropriate

When extending parent behavior, `super()` can avoid unnecessarily duplicating parent implementation details.

### 6. Understand MRO

MRO becomes especially important when using multiple or complex inheritance.

---

# ⭐ Key Points

- Inheritance allows a class to acquire functionality from another class.
- The class being inherited from is called the parent/base/superclass.
- The inheriting class is called the child/derived/subclass.
- Inheritance promotes code reuse.
- A child class can inherit methods and attributes.
- A child class can add its own methods and attributes.
- A child class can override inherited methods.
- Single inheritance has one parent and one child.
- Multiple inheritance allows one class to inherit from multiple parents.
- Multilevel inheritance creates a chain of inheritance.
- Hierarchical inheritance allows multiple children to share one parent.
- Hybrid inheritance combines multiple inheritance patterns.
- Multiple and hybrid inheritance can produce complex hierarchies.
- Python uses MRO to determine the order in which classes are searched.
- `super()` can be used to access parent behavior.
- Inheritance is generally suitable for an "is-a" relationship.
- Composition is often more suitable for a "has-a" relationship.

---

# 📊 Inheritance Quick Revision Table

| Concept | Meaning |
|---|---|
| Parent Class | Class being inherited from |
| Child Class | Class that inherits |
| Base Class | Another name for parent class |
| Derived Class | Another name for child class |
| Single Inheritance | One parent → one child |
| Multiple Inheritance | Multiple parents → one child |
| Multilevel Inheritance | Parent → Child → Grandchild |
| Hierarchical Inheritance | One parent → multiple children |
| Hybrid Inheritance | Combination of inheritance types |
| Method Reuse | Child can use inherited methods |
| Method Override | Child provides its own implementation |
| `super()` | Accesses the next class in the inheritance hierarchy |
| MRO | Order used to search classes for methods/attributes |

---

# 🚀 Inheritance Summary

Inheritance is one of the most important OOP concepts because it allows related classes to share common functionality while still maintaining their own specialized behavior.

The basic idea is:

```text
Parent Class
     ↓
Common Functionality
     ↓
Child Class
     ↓
Reuse + Extend + Customize
```

Python supports several inheritance patterns:

```text
Single
Multiple
Multilevel
Hierarchical
Hybrid
```

Understanding these inheritance structures is essential before learning advanced concepts such as:

```text
super()
MRO
C3 Linearization
Method Overriding
Polymorphism
```

These concepts work together to make Python's OOP system powerful and flexible.

# 🔄 Part 2 — `super()` and Method Resolution Order (MRO)

## 🔄 2. `super()`

## 🧠 Basic Concept

`super()` is a built-in function in Python that is used to access methods and attributes from a class higher in the **Method Resolution Order (MRO)**.

It is most commonly used when a child class wants to use functionality from its parent class without directly referring to the parent class by name.

In simple inheritance, `super()` is often used to call the parent class's method or constructor.

### Basic Syntax

```python
super().method_name()
```

For calling the parent constructor:

```python
super().__init__()
```

### Basic Example

```python
class Parent:
    def show(self):
        print("This is the Parent class")


class Child(Parent):
    def show(self):
        super().show()
        print("This is the Child class")


obj = Child()
obj.show()
```

**Output:**

```text
This is the Parent class
This is the Child class
```

Here:

- `Child` inherits from `Parent`.
- `Child` overrides the `show()` method.
- `super().show()` calls the next `show()` method according to the MRO.
- In this simple case, the next class is `Parent`.

---

## 🎯 Why Use `super()`?

`super()` is useful because it:

1. Allows a child class to reuse parent functionality.
2. Avoids writing the parent class name explicitly.
3. Makes inheritance code cleaner.
4. Helps maintain code when class relationships change.
5. Is especially important in **multiple inheritance**.
6. Allows classes to cooperate through the MRO.
7. Helps prevent duplicate execution in cooperative multiple inheritance.

---

# 📞 2.1 Calling Parent Methods

A child class can override a method and still call the original parent implementation using `super()`.

### Example

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()
dog.sound()
```

**Output:**

```text
Animal makes a sound
Dog barks
```

The child class adds its own behavior while preserving the behavior of the parent class.

### Without `super()`

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()
```

**Output:**

```text
Dog barks
```

The parent implementation is not executed.

---

# 🏗️ 2.2 Calling Parent Constructor

One of the most common uses of `super()` is calling the parent class's `__init__()` method.

### Example

```python
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


student = Student("Sonal", "Python")

print(student.name)
print(student.course)
```

**Output:**

```text
Sonal
Python
```

Here:

```python
super().__init__(name)
```

calls:

```python
Person.__init__(self, name)
```

Conceptually, it initializes the `name` attribute defined by the parent class.

---

## ⚠️ Important Point

If a child class defines its own `__init__()`, Python does **not automatically call the parent's `__init__()`**.

Therefore, if the parent constructor needs to run, the child usually needs to call it explicitly using `super()`.

### Example

```python
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course):
        self.course = course


student = Student("Sonal", "Python")

print(student.course)
```

This works for `course`, but the parent's initialization of `name` was never performed.

Trying:

```python
print(student.name)
```

will raise:

```text
AttributeError
```

Therefore:

```python
super().__init__(name)
```

is important when the parent class has initialization logic that the child needs.

---

# 🔢 2.3 Passing Arguments with `super()`

`super()` can also pass arguments to the parent constructor or method.

### Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


student = Student("Sonal", 21, "AI/ML")

print(student.name)
print(student.age)
print(student.course)
```

**Output:**

```text
Sonal
21
AI/ML
```

---

# 🔗 2.4 `super()` with Multiple Inheritance

`super()` becomes particularly important when dealing with **multiple inheritance**.

Consider:

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


obj = D()
obj.show()
```

**Output:**

```text
D
B
C
A
```

At first, this may seem surprising.

One might expect:

```text
D
B
A
```

But that is not what happens.

Python follows the **Method Resolution Order (MRO)**:

```text
D → B → C → A → object
```

Therefore:

```python
super()
```

does not simply mean:

> "Call my direct parent."

Instead, it means approximately:

> "Continue looking for the requested method from the next class in the MRO."

This distinction is extremely important in multiple inheritance.

---

# 🚫 2.5 Direct Parent Call vs `super()`

Consider:

```python
class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        Parent.show(self)
        print("Child")


obj = Child()
obj.show()
```

This works, but it directly refers to `Parent`.

Using `super()`:

```python
class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        super().show()
        print("Child")


obj = Child()
obj.show()
```

The second approach is generally preferred.

### Comparison

| Direct Parent Call | `super()` |
|---|---|
| Explicitly names the parent | Uses the MRO |
| `Parent.method(self)` | `super().method()` |
| Can bypass MRO cooperation | Works cooperatively with MRO |
| Less flexible in multiple inheritance | Better for multiple inheritance |
| Tightly couples code to a specific parent | More maintainable |

---

# ⚠️ 2.6 Important Behavior of `super()`

`super()` does not mean:

```text
Go directly to the parent class.
```

More accurately, it means:

```text
Start attribute lookup after the current class in the MRO.
```

For example:

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(B):
    def show(self):
        print("C")
        super().show()


obj = C()
obj.show()
```

MRO:

```text
C → B → A → object
```

Therefore:

```text
C
B
A
```

is printed.

---

# 🧭 3. Method Resolution Order (MRO)

## 🧠 Basic Concept

**Method Resolution Order (MRO)** is the order in which Python searches classes when looking for a method, attribute, or other inherited member.

MRO becomes especially important when a class has multiple parent classes.

### Example

```python
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(B):
    pass


obj = C()
obj.show()
```

Python searches approximately like this:

```text
C → B → A → object
```

Since `show()` is found in `A`, Python executes:

```text
A
```

---

# 🔍 3.1 Viewing the MRO

Python provides several ways to inspect the MRO.

## Using `mro()`

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
```

**Output:**

```text
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```

---

## Using `__mro__`

```python
print(C.__mro__)
```

This also displays the MRO.

### Example

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.__mro__)
```

The important order is:

```text
C → B → A → object
```

---

## Using `inspect.getmro()`

Python's `inspect` module can also be used:

```python
import inspect


class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(inspect.getmro(C))
```

---

# 🧬 3.2 MRO in Single Inheritance

In single inheritance, the MRO is straightforward.

```python
class Animal:
    def sound(self):
        print("Animal")


class Dog(Animal):
    pass


dog = Dog()
dog.sound()

print(Dog.mro())
```

The MRO is:

```text
Dog → Animal → object
```

Python searches:

1. `Dog`
2. `Animal`
3. `object`

Since `sound()` exists in `Animal`, Python executes that method.

---

# 🔀 3.3 MRO in Multiple Inheritance

Multiple inheritance occurs when a class inherits from more than one class.

```python
class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.mro())
```

The MRO is:

```text
C → A → B → object
```

Python follows the order specified in the class definition while maintaining the rules of MRO.

---

# 💎 3.4 Diamond Inheritance

A common example of multiple inheritance is the **Diamond Problem**.

Consider:

```text
        A
       / \
      B   C
       \ /
        D
```

Here:

- `A` is the common parent.
- `B` inherits from `A`.
- `C` inherits from `A`.
- `D` inherits from both `B` and `C`.

### Python Example

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


obj = D()
obj.show()
```

The MRO is:

```text
D → B → C → A → object
```

**Output:**

```text
D
B
C
A
```

Python does not simply follow:

```text
D → B → A
```

because that would ignore `C`.

The MRO provides a consistent order for resolving methods.

---

# 🧮 3.5 C3 Linearization

Python uses an algorithm called **C3 Linearization** to calculate the MRO for classes using multiple inheritance.

C3 Linearization creates an MRO that satisfies important properties such as:

- **Consistency**
- **Monotonicity**
- **Preservation of local precedence order**

You do not usually need to manually calculate C3 Linearization when writing normal Python programs, but understanding its purpose is important.

---

## 📌 Local Precedence Order

Consider:

```python
class D(B, C):
    pass
```

Python must respect the order:

```text
B before C
```

Therefore, the MRO cannot place `C` before `B`.

---

## 📌 Monotonicity

If one class establishes an ordering between classes, a subclass should not arbitrarily reverse that ordering.

For example, if:

```text
B comes before C
```

is established by the inheritance structure, a valid subclass MRO should preserve that relationship where applicable.

---

## 📌 Avoiding Duplicate Classes

In the diamond structure:

```text
        A
       / \
      B   C
       \ /
        D
```

Python should not execute `A` twice simply because both `B` and `C` inherit from it.

C3 Linearization helps create a consistent order such as:

```text
D → B → C → A → object
```

Therefore, `A` appears only once.

---

# 🔢 3.6 Understanding C3 with the Diamond Example

Consider:

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
```

The important result is:

```text
D → B → C → A → object
```

Python has to satisfy several constraints:

1. `D` must come first.
2. `B` must appear before its parent `A`.
3. `C` must appear before its parent `A`.
4. `B` must remain before `C` because `D(B, C)` specifies that order.
5. `A` must appear only after both `B` and `C`.
6. `object` comes at the end.

Therefore:

```text
D → B → C → A → object
```

is a valid MRO.

---

# 🔄 3.7 `super()` with MRO

`super()` and MRO are closely connected.

When Python evaluates:

```python
super().method()
```

it looks for `method()` according to the MRO, starting after the current class.

### Example

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


obj = D()
obj.show()
```

MRO:

```text
D → B → C → A → object
```

Execution:

```text
D.show()
    ↓
super().show()
    ↓
B.show()
    ↓
super().show()
    ↓
C.show()
    ↓
super().show()
    ↓
A.show()
```

Therefore the output is:

```text
D
B
C
A
```

---

# 🤝 3.8 Cooperative Multiple Inheritance

When multiple classes use `super()` correctly, they can cooperate with one another.

This is called **cooperative multiple inheritance**.

### Example

```python
class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()


obj = D()
```

MRO:

```text
D → B → C → A → object
```

**Output:**

```text
D
B
C
A
```

Each class gets an opportunity to execute its constructor.

---

# 🧠 3.9 Why `super()` Is Important in Multiple Inheritance

Consider this approach:

```python
class B(A):
    def show(self):
        A.show(self)
```

and:

```python
class C(A):
    def show(self):
        A.show(self)
```

If another class inherits from both `B` and `C`, direct calls can cause `A.show()` to be executed more than once.

Using:

```python
super().show()
```

allows the classes to cooperate through the MRO.

This is one of the biggest reasons why `super()` is preferred in well-designed multiple inheritance hierarchies.

---

# 🚫 3.10 Common Mistake — Assuming `super()` Means Parent

A common beginner explanation is:

> "`super()` calls the parent class."

This is often true in simple inheritance, but it is not the complete explanation.

A more accurate explanation is:

> `super()` delegates attribute lookup to the next class in the MRO.

### Example

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()
```

For `D`:

```text
D → B → C → A → object
```

When `D` calls:

```python
super().show()
```

it goes to `B`.

When `B` calls:

```python
super().show()
```

it goes to `C`, not directly to `A`.

That is the key idea.

---

# 🚫 3.11 Common Mistake — Mixing Direct Parent Calls and `super()`

Avoid unnecessarily mixing:

```python
Parent.method(self)
```

with:

```python
super().method()
```

in a cooperative multiple inheritance design.

### Less Cooperative Approach

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        A.show(self)
        print("B")
```

### Cooperative Approach

```python
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        super().show()
        print("B")
```

The second approach is generally better suited to inheritance hierarchies that may involve multiple inheritance.

---

# 🧩 3.12 `super()` with Constructors in Multiple Inheritance

Constructors can also cooperate through the MRO.

### Example

```python
class A:
    def __init__(self):
        print("A constructor")


class B(A):
    def __init__(self):
        print("B constructor")
        super().__init__()


class C(A):
    def __init__(self):
        print("C constructor")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D constructor")
        super().__init__()


obj = D()
```

MRO:

```text
D → B → C → A → object
```

**Output:**

```text
D constructor
B constructor
C constructor
A constructor
```

Every class cooperates with the next class in the MRO.

---

# 📦 3.13 Passing Arguments Through Cooperative `__init__()`

In real applications, constructors often receive arguments.

One common pattern is to use keyword arguments and forward them with `super()`.

### Example

```python
class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)


class Student(Person):
    def __init__(self, course, **kwargs):
        self.course = course
        super().__init__(**kwargs)


student = Student(name="Sonal", course="AI/ML")

print(student.name)
print(student.course)
```

**Output:**

```text
Sonal
AI/ML
```

The use of `**kwargs` can make cooperative inheritance easier when several classes need different initialization arguments.

---

# 🔎 3.14 `super()` vs `ParentClass`

| Feature | `super()` | Direct Parent Call |
|---|---|---|
| Syntax | `super().method()` | `Parent.method(self)` |
| Uses MRO | Yes | No |
| Works well with multiple inheritance | Yes | Can cause problems |
| Explicit parent name required | No | Yes |
| Supports cooperative inheritance | Yes | Usually not |
| Maintainability | Better | More tightly coupled |

---

# 📊 3.15 MRO Examples

| Inheritance | Typical MRO |
|---|---|
| `B(A)` | `B → A → object` |
| `C(B)` | `C → B → A → object` |
| `C(A, B)` | `C → A → B → object` |
| `D(B, C)` where both inherit `A` | `D → B → C → A → object` |

The exact MRO depends on the complete inheritance graph and Python's C3 Linearization rules.

---

# 🏆 3.16 Best Practices for `super()`

1. Prefer `super()` over unnecessary direct parent calls.
2. Understand the MRO before using complex multiple inheritance.
3. Use `super()` consistently in cooperative inheritance hierarchies.
4. Do not assume `super()` always means the direct parent.
5. Use `Class.mro()` or `Class.__mro__` when debugging inheritance behavior.
6. Keep multiple inheritance designs simple and purposeful.
7. When using cooperative constructors, ensure classes forward the required arguments correctly.
8. Avoid mixing incompatible constructor signatures in a cooperative hierarchy.
9. Document complicated inheritance structures.
10. Use composition instead of complicated inheritance when inheritance does not represent a genuine "is-a" relationship.

---

# ❌ 3.17 Common Beginner Mistakes

### Mistake 1 — Forgetting `super()`

```python
class Parent:
    def __init__(self):
        self.name = "Sonal"


class Child(Parent):
    def __init__(self):
        self.course = "Python"
```

The parent's constructor is not called.

Better:

```python
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.course = "Python"
```

---

### Mistake 2 — Thinking `super()` Always Calls the Parent

Incorrect understanding:

```text
super() = direct parent
```

Better understanding:

```text
super() = next class in the MRO
```

---

### Mistake 3 — Ignoring MRO in Multiple Inheritance

When using:

```python
class D(B, C):
    pass
```

always remember that Python calculates an MRO for `D`.

Use:

```python
print(D.mro())
```

to inspect it.

---

### Mistake 4 — Calling the Same Parent Directly from Multiple Classes

Direct parent calls can interfere with cooperative multiple inheritance.

Prefer:

```python
super().method()
```

when the hierarchy is designed cooperatively.

---

# ⭐ Key Points — `super()` and MRO

- `super()` is a built-in Python function.
- It returns a proxy object used for delegated attribute lookup.
- `super().method()` calls the next implementation according to the MRO.
- `super().__init__()` is commonly used to call the next constructor.
- MRO stands for **Method Resolution Order**.
- MRO determines the order in which Python searches classes.
- MRO is especially important in multiple inheritance.
- Python uses **C3 Linearization** to calculate MRO.
- `Class.mro()` can display the MRO.
- `Class.__mro__` can also display the MRO.
- `object` is normally at the end of the MRO.
- `super()` does not simply mean "parent class".
- Cooperative multiple inheritance relies heavily on `super()`.
- Consistent use of `super()` helps prevent duplicate method execution in diamond inheritance structures.

---

# 📊 Quick Revision Table

| Concept | Meaning |
|---|---|
| `super()` | Provides access to the next class in the MRO |
| `super().__init__()` | Calls the next constructor in the MRO |
| MRO | Order in which Python searches classes |
| `mro()` | Method used to view MRO |
| `__mro__` | Attribute containing the MRO |
| Multiple Inheritance | Class inherits from multiple classes |
| Diamond Inheritance | Two parent classes share a common base |
| C3 Linearization | Algorithm used by Python to calculate MRO |
| Cooperative Inheritance | Classes cooperate using `super()` |
| `object` | Ultimate base class for ordinary Python classes |

---

# 🧪 Complete Example — `super()` + MRO

```python
class Animal:
    def __init__(self):
        print("Animal")


class Mammal(Animal):
    def __init__(self):
        print("Mammal")
        super().__init__()


class Bird(Animal):
    def __init__(self):
        print("Bird")
        super().__init__()


class Bat(Mammal, Bird):
    def __init__(self):
        print("Bat")
        super().__init__()


bat = Bat()

print("\nMRO:")
for cls in Bat.mro():
    print(cls.__name__)
```

**Output:**

```text
Bat
Mammal
Bird
Animal

MRO:
Bat
Mammal
Bird
Animal
object
```

This example combines the most important concepts from this section:

- Multiple inheritance
- Diamond inheritance
- `super()`
- Constructor chaining
- MRO
- Cooperative inheritance

---

# 💡 Real-Life Applications

`super()` and MRO are useful when building:

- Large object-oriented applications
- Frameworks
- Machine learning systems
- Data processing pipelines
- Plugin systems
- GUI applications
- Web frameworks
- Reusable class hierarchies
- Mixins
- Extensible software architectures

In advanced Python development, understanding MRO becomes particularly important when working with frameworks and libraries that use multiple inheritance or mixins.

---

# 🚀 Summary

`super()` provides a clean way to continue method or constructor lookup through the inheritance hierarchy.

In simple inheritance, it commonly allows a child class to call functionality from its parent.

In multiple inheritance, however, `super()` becomes much more powerful because it follows the **Method Resolution Order (MRO)** rather than simply jumping to a specific parent.

Python calculates the MRO using **C3 Linearization**, which provides a consistent and predictable ordering for complex inheritance structures.

The most important relationship to remember is:

```text
Inheritance
    ↓
MRO determines the search order
    ↓
super() follows that order
    ↓
C3 Linearization calculates the MRO
```

A strong understanding of these concepts is essential before moving on to more advanced Python OOP topics such as:

- `@classmethod`
- Property decorators
- Operator overloading
- Encapsulation
- Polymorphism
- Abstraction
- Composition

# 🏛️ Part 3 — `@classmethod`

# 🏛️ 4. `@classmethod`

## 🧠 Basic Concept

A **class method** is a method that is bound to the **class** rather than to a particular object.

In Python, a class method is created using the `@classmethod` decorator.

A normal instance method receives the object as its first parameter:

```python
def method(self):
    ...
```

A class method receives the class itself as its first parameter:

```python
@classmethod
def method(cls):
    ...
```

Here:

- `self` refers to the current **object/instance**.
- `cls` refers to the current **class**.
- `@classmethod` converts a normal function into a class method.

### Basic Syntax

```python
class ClassName:

    @classmethod
    def method_name(cls):
        # class-level logic
        pass
```

---

# 🔍 4.1 Instance Method vs Class Method

Python OOP commonly uses three types of methods:

| Method Type | First Parameter | Works Mainly With |
|---|---|---|
| Instance Method | `self` | Object/instance |
| Class Method | `cls` | Class |
| Static Method | None | Independent utility logic |

### Instance Method

```python
class Student:

    def show(self):
        print("Instance method")
```

The method receives an object through `self`.

### Class Method

```python
class Student:

    @classmethod
    def show(cls):
        print("Class method")
```

The method receives the class through `cls`.

---

# 🎯 4.2 Understanding `cls`

`cls` is simply a conventional name for the class reference.

Just like:

```python
self
```

is the conventional name for the current object,

```python
cls
```

is the conventional name for the current class.

### Example

```python
class Student:

    @classmethod
    def show_class(cls):
        print(cls)


Student.show_class()
```

**Output:**

```text
<class '__main__.Student'>
```

Here:

```python
cls
```

refers to:

```python
Student
```

---

# 🏗️ 4.3 Calling a Class Method

A class method can be called directly using the class.

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


Student.show_school()
```

**Output:**

```text
ABC School
```

No object is required to call the method.

---

# 🔄 4.4 Calling a Class Method Through an Object

A class method can also be accessed through an object.

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


student = Student()

student.show_school()
```

**Output:**

```text
ABC School
```

However, the method still receives the **class** as `cls`, not the object as `self`.

---

# 📦 4.5 Working with Class Attributes

One of the most useful purposes of class methods is working with **class attributes**.

### Example

```python
class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


print(Student.school)

Student.change_school("XYZ School")

print(Student.school)
```

**Output:**

```text
ABC School
XYZ School
```

The class method changes the class-level attribute.

---

# 🔧 4.6 Modifying Class Attributes Using `cls`

Consider:

```python
class Employee:

    company = "Tech Company"

    @classmethod
    def change_company(cls, name):
        cls.company = name


print(Employee.company)

Employee.change_company("AI Company")

print(Employee.company)
```

**Output:**

```text
Tech Company
AI Company
```

The important statement is:

```python
cls.company = name
```

Because `cls` represents the class, the class attribute is modified.

---

# 🧩 4.7 Class Method with Multiple Class Attributes

A class method can access and modify multiple class attributes.

```python
class Student:

    school = "ABC School"
    city = "Lucknow"

    @classmethod
    def update_details(cls, school, city):
        cls.school = school
        cls.city = city


print(Student.school)
print(Student.city)

Student.update_details("XYZ School", "Delhi")

print(Student.school)
print(Student.city)
```

**Output:**

```text
ABC School
Lucknow
XYZ School
Delhi
```

---

# 🔢 4.8 Class Method Can Access Class Data

A class method can access:

- Class attributes
- Other class methods
- Class-level configuration
- Class-level counters
- Alternative constructors

### Example

```python
class Employee:

    company = "Tech Company"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def show_count(cls):
        print("Total employees:", cls.employee_count)


e1 = Employee("Sonal")
e2 = Employee("Rahul")

Employee.show_count()
```

**Output:**

```text
Total employees: 2
```

---

# 🔄 4.9 Class Method Calling Another Class Method

A class method can call another class method using `cls`.

### Example

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

    @classmethod
    def display(cls):
        cls.show_school()


Student.display()
```

**Output:**

```text
ABC School
```

Here:

```python
cls.show_school()
```

calls another class method.

---

# 🏭 4.10 Alternative Constructors

One of the most important real-world uses of `@classmethod` is creating **alternative constructors**.

Normally, an object is created using:

```python
ClassName(...)
```

But sometimes we want to create an object using data in a different format.

For example, suppose a class expects:

```text
name
age
```

But our data is provided as:

```text
"Sonal-21"
```

A class method can convert that data into the required format.

---

# 🛠️ 4.11 Basic Alternative Constructor

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


student = Student.from_string("Sonal-21")

print(student.name)
print(student.age)
```

**Output:**

```text
Sonal
21
```

Here:

```python
from_string()
```

is an alternative constructor.

Instead of:

```python
Student("Sonal", 21)
```

we can use:

```python
Student.from_string("Sonal-21")
```

---

# 🧠 4.12 Why Use `cls` in Alternative Constructors?

Notice this line:

```python
return cls(name, int(age))
```

`cls` represents the class that called the class method.

This is better than writing:

```python
return Student(name, int(age))
```

because `cls` allows the method to work properly with subclasses as well.

### Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


student = Student.from_string("Sonal-21")

print(student.name)
print(student.age)
```

The class method creates and returns an object of the class represented by `cls`.

---

# 🧬 4.13 Alternative Constructor with Subclasses

Using `cls` makes alternative constructors inheritance-friendly.

```python
class Person:

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, data):
        return cls(data)


class Student(Person):
    pass


student = Student.from_string("Sonal")

print(type(student))
print(student.name)
```

**Output:**

```text
<class '__main__.Student'>
Sonal
```

Because:

```python
Student.from_string()
```

was called, `cls` refers to:

```python
Student
```

Therefore:

```python
return cls(data)
```

creates a `Student` object.

This is an important advantage of using `cls` instead of directly writing the parent class name.

---

# 📊 4.14 `self` vs `cls`

| `self` | `cls` |
|---|---|
| Refers to the object | Refers to the class |
| Used in instance methods | Used in class methods |
| Accesses instance attributes | Accesses class attributes |
| Represents one object | Represents the class |
| Each object has its own instance data | Class data is shared at class level |

### Example

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def show_student(self):
        print(self.name)

    @classmethod
    def show_school(cls):
        print(cls.school)


student = Student("Sonal")

student.show_student()
Student.show_school()
```

**Output:**

```text
Sonal
ABC School
```

---

# 🔄 4.15 Class Method vs Instance Method

### Instance Method

```python
class Student:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


student = Student("Sonal")
student.show()
```

The method operates on a specific object.

### Class Method

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


Student.show_school()
```

The method operates on class-level information.

---

# 🏫 4.16 Practical Example — School

```python
class Student:

    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", self.school)


student1 = Student("Sonal", 21)
student2 = Student("Rahul", 22)

student1.display()

Student.change_school("XYZ School")

student2.display()
```

**Output:**

```text
Name: Sonal
Age: 21
School: ABC School
Name: Rahul
Age: 22
School: XYZ School
```

The class method changed the shared class-level value.

---

# 💰 4.17 Practical Example — Employee Company

```python
class Employee:

    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)


employee1 = Employee("Sonal", 50000)
employee2 = Employee("Rahul", 60000)

Employee.change_company("XYZ Technologies")

employee1.display()
employee2.display()
```

**Output:**

```text
Name: Sonal
Salary: 50000
Company: XYZ Technologies
Name: Rahul
Salary: 60000
Company: XYZ Technologies
```

Both objects see the updated class attribute.

---

# 📄 4.18 Practical Example — Creating Object from a Dictionary

Class methods can also be used to create objects from structured data.

```python
class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["course"]
        )


data = {
    "name": "Sonal",
    "age": 21,
    "course": "AI/ML"
}

student = Student.from_dict(data)

print(student.name)
print(student.age)
print(student.course)
```

**Output:**

```text
Sonal
21
AI/ML
```

This pattern is useful when converting external data into Python objects.

---

# 🤖 4.19 AI/ML Use Case

Class methods can be useful in AI/ML projects when objects need to be created from different data sources.

For example:

```python
class ModelConfig:

    def __init__(self, model_name, learning_rate, epochs):
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.epochs = epochs

    @classmethod
    def from_dict(cls, config):
        return cls(
            config["model_name"],
            config["learning_rate"],
            config["epochs"]
        )


config_data = {
    "model_name": "NeuralNetwork",
    "learning_rate": 0.001,
    "epochs": 50
}

config = ModelConfig.from_dict(config_data)

print(config.model_name)
print(config.learning_rate)
print(config.epochs)
```

**Output:**

```text
NeuralNetwork
0.001
50
```

This pattern can be useful for:

- Model configuration
- Dataset configuration
- Hyperparameter objects
- API responses
- JSON-to-object conversion
- Data preprocessing pipelines

---

# ⚠️ 4.20 Important Rules of `@classmethod`

1. A class method is defined using `@classmethod`.
2. Its first parameter is conventionally called `cls`.
3. `cls` refers to the class.
4. A class method can access class attributes through `cls`.
5. A class method can modify class attributes.
6. A class method can call other class methods through `cls`.
7. Class methods can be called using the class.
8. They can also be accessed through an object.
9. Class methods are commonly used as alternative constructors.
10. Using `cls(...)` in alternative constructors makes them inheritance-friendly.

---

# ❌ 4.21 Common Beginner Mistakes

## Mistake 1 — Forgetting `@classmethod`

Incorrect:

```python
class Student:

    def show_school(cls):
        print(cls.school)
```

This is not automatically a class method.

Correct:

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)
```

---

## Mistake 2 — Using `self` Instead of `cls`

Incorrect style:

```python
@classmethod
def show(cls):
    print(self.school)
```

`self` is not defined here.

Correct:

```python
@classmethod
def show(cls):
    print(cls.school)
```

---

## Mistake 3 — Confusing Class and Instance Attributes

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

Here:

```python
self.name
```

is an instance attribute.

While:

```python
Student.school
```

is a class attribute.

---

## Mistake 4 — Hardcoding the Class Name

Instead of:

```python
return Student(name, age)
```

inside an alternative constructor, prefer:

```python
return cls(name, age)
```

This allows subclasses to reuse the same class method correctly.

---

# 🧠 4.22 When Should You Use `@classmethod`?

Use a class method when the method:

- Needs access to the class itself.
- Works with class attributes.
- Changes class-level configuration.
- Creates objects in an alternative way.
- Needs to remain compatible with subclasses.
- Represents behavior associated with the class rather than a specific object.

### Good Examples

```text
change company name
change school name
track total objects
create object from string
create object from dictionary
create object from JSON-like data
create object from configuration
```

---

# 🚫 4.23 When Should You NOT Use `@classmethod`?

Do not use a class method simply because it is available.

If the method needs information specific to an object, use an instance method.

### Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)
```

This should be an instance method because the method operates on a particular student's data.

A class method would not be appropriate here.

---

# 📊 4.24 `@classmethod` vs `@staticmethod` vs Instance Method

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None | `@classmethod` | `@staticmethod` |
| First parameter | `self` | `cls` | None |
| Access instance data | Yes | No, not directly | No |
| Access class data | Yes | Yes | Only explicitly |
| Works with object | Yes | Yes | Yes |
| Works with class | Through instance normally | Yes | Yes |
| Common use | Object behavior | Class behavior | Utility logic |
| Alternative constructor | No | Yes | Usually no |

---

# 🏆 4.25 Best Practices

1. Use `@classmethod` when behavior belongs to the class.
2. Use `cls` as the conventional first parameter.
3. Use `cls.attribute` for class-level data.
4. Use `cls(...)` for alternative constructors.
5. Avoid using class methods for object-specific behavior.
6. Keep class methods focused and readable.
7. Prefer class methods when subclasses should inherit and reuse object-creation logic.
8. Clearly name alternative constructors, such as:
   - `from_string()`
   - `from_dict()`
   - `from_json()`
   - `from_file()`
   - `from_config()`

---

# ⭐ Key Points — `@classmethod`

- `@classmethod` creates a class method.
- A class method receives `cls` as its first parameter.
- `cls` refers to the class.
- Class methods can access class attributes.
- Class methods can modify class attributes.
- They can call other class methods using `cls`.
- They can be called directly using the class.
- One of their most important uses is creating **alternative constructors**.
- Alternative constructors commonly use `return cls(...)`.
- Using `cls(...)` makes the constructor work naturally with subclasses.
- Instance methods use `self`.
- Class methods use `cls`.
- Static methods do not automatically receive `self` or `cls`.

---

# 📊 Quick Revision Table

| Concept | Description |
|---|---|
| `@classmethod` | Decorator used to create a class method |
| `cls` | Reference to the current class |
| Class Attribute | Attribute shared at class level |
| `cls.attribute` | Access class attribute |
| `cls.method()` | Call another class method |
| `cls(...)` | Create an object of the current class |
| Alternative Constructor | Another way to create an object |
| `from_string()` | Common alternative constructor pattern |
| `from_dict()` | Creates an object from dictionary data |
| Instance Method | Works primarily with object data |
| Class Method | Works primarily with class data |
| Static Method | Utility method without automatic `self` or `cls` |

---

# 🧪 Complete Example — Class Method + Class Attribute + Alternative Constructor

```python
class Student:

    school = "ABC School"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def from_string(cls, data):
        name, age, course = data.split("-")
        return cls(name, int(age), course)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("School:", self.school)


student1 = Student.from_string("Sonal-21-AI/ML")

student1.display()

print("\nChanging school...")

Student.change_school("XYZ School")

student1.display()
```

**Output:**

```text
Name: Sonal
Age: 21
Course: AI/ML
School: ABC School

Changing school...
Name: Sonal
Age: 21
Course: AI/ML
School: XYZ School
```

This complete example demonstrates:

- `@classmethod`
- `cls`
- Class attributes
- Modifying class attributes
- Alternative constructors
- `cls(...)`
- Instance methods
- Instance attributes

---

# 🚀 Summary

A **class method** is a method that works with the class rather than being tied primarily to one particular object.

It is created using:

```python
@classmethod
```

and receives the class through:

```python
cls
```

The `cls` parameter allows us to access and modify class-level data:

```python
cls.school
```

One of the most powerful uses of class methods is creating **alternative constructors**:

```python
@classmethod
def from_string(cls, data):
    ...
    return cls(...)
```

This allows objects to be created from different forms of input while keeping the class design clean and reusable.

The key relationship to remember is:

```text
Instance Method
      ↓
     self
      ↓
Current Object

Class Method
      ↓
      cls
      ↓
Current Class
```

Understanding `@classmethod`, `self`, and `cls` provides an important foundation for the next advanced OOP concepts such as **property decorators, operator overloading, encapsulation, polymorphism, abstraction, and composition**.

# 🏠 Part 4 — Property Decorators

# 🏠 5. Property Decorators

## 🧠 Basic Concept

**Property decorators** allow us to control how attributes are accessed, modified, and deleted.

In Python, the `@property` decorator allows a method to be accessed like an attribute.

This is useful when we want to:

- Control access to data.
- Validate values before storing them.
- Calculate values dynamically.
- Hide internal implementation details.
- Implement getters and setters.
- Provide controlled access to attributes.

The main decorators used with properties are:

```text
@property
@attribute.setter
@attribute.deleter
```

---

# 🔑 5.1 Why Do We Need Property Decorators?

Consider a simple class:

```python
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Sonal")

print(student.name)
```

**Output:**

```text
Sonal
```

This works, but there is no control over the value.

For example:

```python
student.name = 12345
```

Python will allow it.

If we want to control how `name` is accessed or modified, we can use a property.

---

# 🏷️ 5.2 `@property`

The `@property` decorator converts a method into a property.

This means we can call the method **without using parentheses**.

### Normal Method

```python
class Student:

    def get_name(self):
        return "Sonal"


student = Student()

print(student.get_name())
```

Here we need:

```python
student.get_name()
```

because `get_name()` is a method.

### Using `@property`

```python
class Student:

    @property
    def name(self):
        return "Sonal"


student = Student()

print(student.name)
```

**Output:**

```text
Sonal
```

Notice that we use:

```python
student.name
```

instead of:

```python
student.name()
```

The method behaves like an attribute.

---

# 🧠 5.3 Basic `@property` Syntax

```python
class ClassName:

    @property
    def attribute_name(self):
        return some_value
```

Example:

```python
class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


person = Person("Sonal")

print(person.name)
```

**Output:**

```text
Sonal
```

Here:

```python
@property
```

creates a getter for `name`.

---

# 📥 5.4 Getter

A **getter** is used to retrieve or read a value.

With the `@property` decorator, the method acts as the getter.

### Example

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


student = Student("Sonal")

print(student.name)
```

**Output:**

```text
Sonal
```

The getter is:

```python
@property
def name(self):
    return self._name
```

It allows us to read:

```python
student.name
```

---

# 🔒 5.5 Why Use `_name` Instead of `name`?

Notice that we used:

```python
self._name
```

instead of:

```python
self.name
```

Inside the property getter, writing:

```python
return self.name
```

would call the property again and can result in infinite recursion.

Therefore, a common pattern is:

```python
self._name
```

for the internal storage variable and:

```python
@property
def name(self):
    return self._name
```

for controlled access.

---

# ✏️ 5.6 Setter

A **setter** allows us to control how a property is modified.

The syntax is:

```python
@property
def name(self):
    ...

@name.setter
def name(self, value):
    ...
```

### Example

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


student = Student("Sonal")

print(student.name)

student.name = "Rahul"

print(student.name)
```

**Output:**

```text
Sonal
Rahul
```

The statement:

```python
student.name = "Rahul"
```

automatically calls:

```python
@name.setter
```

---

# 🔄 5.7 How Getter and Setter Work Together

Consider:

```python
student.name
```

Python calls the getter:

```python
@property
def name(self):
    return self._name
```

When we write:

```python
student.name = "Rahul"
```

Python calls:

```python
@name.setter
def name(self, value):
    self._name = value
```

Therefore:

```text
student.name
      ↓
    Getter
      ↓
   self._name
```

and:

```text
student.name = value
      ↓
    Setter
      ↓
   self._name = value
```

---

# 🛡️ 5.8 Setter Validation

One of the biggest advantages of a setter is **validation**.

Suppose a student's age must be between `1` and `100`.

```python
class Student:

    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 1 <= value <= 100:
            self._age = value
        else:
            raise ValueError("Age must be between 1 and 100")


student = Student(21)

print(student.age)

student.age = 25

print(student.age)
```

**Output:**

```text
21
25
```

If we try:

```python
student.age = 150
```

Python raises:

```text
ValueError: Age must be between 1 and 100
```

This prevents invalid data from entering the object.

---

# 🚫 5.9 Validation Without Property

Without a setter, someone could directly modify the attribute:

```python
student.age = -10
```

There would be no validation unless we manually handled it.

With a property setter:

```python
@age.setter
def age(self, value):
    if value > 0:
        self._age = value
```

we can control every assignment made through:

```python
student.age = value
```

---

# 🧮 5.10 Property for Calculated Values

A property does not always need to store a separate value.

It can calculate a value dynamically.

### Example

```python
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

print(rectangle.area)
```

**Output:**

```text
50
```

Notice:

```python
rectangle.area
```

looks like a normal attribute.

But internally Python executes:

```python
return self.length * self.width
```

---

# 📊 5.11 Property for Percentage Calculation

```python
class Student:

    def __init__(self, marks, total):
        self.marks = marks
        self.total = total

    @property
    def percentage(self):
        return (self.marks / self.total) * 100


student = Student(450, 500)

print(student.percentage)
```

**Output:**

```text
90.0
```

The percentage does not need to be separately stored because it can be calculated whenever required.

---

# 🗑️ 5.12 Deleter

A **deleter** controls what happens when a property is deleted.

The syntax is:

```python
@property
def name(self):
    ...

@name.deleter
def name(self):
    ...
```

### Example

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name


student = Student("Sonal")

print(student.name)

del student.name
```

**Output:**

```text
Sonal
Deleting name...
```

The statement:

```python
del student.name
```

calls the property deleter.

---

# 🔄 5.13 Getter + Setter + Deleter

A property can have all three:

- Getter
- Setter
- Deleter

### Complete Example

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")

        self._name = value

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name


student = Student("Sonal")

print(student.name)

student.name = "Rahul"

print(student.name)

del student.name
```

**Output:**

```text
Sonal
Rahul
Deleting name...
```

This is the complete property pattern.

---

# 🧩 5.14 Complete Property Pattern

The general pattern is:

```python
class ClassName:

    def __init__(self, value):
        self._attribute = value

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    @attribute.deleter
    def attribute(self):
        del self._attribute
```

The three operations are:

```text
Read
 ↓
@property
 ↓
Getter

Write
 ↓
@property.setter
 ↓
Setter

Delete
 ↓
@property.deleter
 ↓
Deleter
```

---

# 🔐 5.15 Read-Only Property

A property can be made **read-only** by defining only the getter.

### Example

```python
class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(5)

print(circle.area)
```

This works:

```python
print(circle.area)
```

But there is no setter for:

```python
circle.area = 100
```

Therefore, the property cannot normally be assigned through that property interface.

This is useful for values that should be calculated rather than directly changed.

---

# 🔒 5.16 Write-Controlled Property

A setter can also restrict how values are modified.

### Example

```python
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value


account = BankAccount(5000)

print(account.balance)

account.balance = 7000

print(account.balance)
```

**Output:**

```text
5000
7000
```

Trying:

```python
account.balance = -1000
```

raises a `ValueError`.

---

# 💰 5.17 Practical Example — Bank Account

Properties are especially useful when an object's data must follow rules.

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount


account = BankAccount(5000)

print(account.balance)

account.deposit(2000)
print(account.balance)

account.withdraw(1000)
print(account.balance)
```

**Output:**

```text
5000
7000
6000
```

The property controls the validity of the balance.

---

# 🎓 5.18 Practical Example — Student Marks

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")


student = Student(85)

print(student.marks)

student.marks = 95

print(student.marks)
```

**Output:**

```text
85
95
```

Invalid:

```python
student.marks = 150
```

results in:

```text
ValueError: Marks must be between 0 and 100
```

---

# 🤖 5.19 AI/ML Use Case

Property decorators are useful in AI/ML systems where configuration values must be validated.

For example, a learning rate should generally be positive.

```python
class ModelConfig:

    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if value <= 0:
            raise ValueError("Learning rate must be positive")

        self._learning_rate = value


config = ModelConfig(0.001)

print(config.learning_rate)

config.learning_rate = 0.01

print(config.learning_rate)
```

**Output:**

```text
0.001
0.01
```

Trying:

```python
config.learning_rate = -0.1
```

raises an error.

Properties can therefore help protect configuration values such as:

- Learning rate
- Batch size
- Number of epochs
- Model thresholds
- Confidence values
- Dataset parameters

---

# 🔍 5.20 Property vs Normal Attribute

| Normal Attribute | Property |
|---|---|
| Direct access | Controlled access |
| No automatic validation | Can validate values |
| Stores data directly | Can calculate data dynamically |
| Less control | More control |
| Simple use cases | Controlled/complex use cases |

---

# 🔄 5.21 Property vs Getter/Setter Methods

Traditional OOP code might use:

```python
student.get_name()
student.set_name("Rahul")
```

With properties:

```python
student.name
student.name = "Rahul"
```

### Traditional Approach

```python
class Student:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


student = Student("Sonal")

print(student.get_name())

student.set_name("Rahul")

print(student.get_name())
```

### Property Approach

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


student = Student("Sonal")

print(student.name)

student.name = "Rahul"

print(student.name)
```

The property approach provides a cleaner interface.

---

# 🧠 5.22 Why Properties Are Considered Pythonic

In some programming languages, getters and setters are commonly written as separate methods.

Python provides properties so that we can maintain a simple attribute-like interface while still controlling what happens internally.

For example:

```python
student.name
```

can internally execute:

```python
return self._name
```

and:

```python
student.name = "Rahul"
```

can internally execute validation logic.

This gives us both:

- Simple syntax for users of the class.
- Controlled behavior inside the class.

---

# ⚠️ 5.23 Common Beginner Mistakes

## Mistake 1 — Using Parentheses with a Property

Incorrect:

```python
print(student.name())
```

Correct:

```python
print(student.name)
```

A property is accessed like an attribute.

---

## Mistake 2 — Creating Infinite Recursion

Incorrect:

```python
class Student:

    @property
    def name(self):
        return self.name
```

The property calls itself repeatedly.

Correct:

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

---

## Mistake 3 — Forgetting the Matching Setter Name

Correct:

```python
@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    self._age = value
```

The setter must use the same property name:

```python
@age.setter
```

---

## Mistake 4 — Not Validating Data

A setter is especially useful when data has restrictions.

Instead of:

```python
@age.setter
def age(self, value):
    self._age = value
```

we can validate:

```python
@age.setter
def age(self, value):
    if value < 0:
        raise ValueError("Age cannot be negative")

    self._age = value
```

---

# 🧩 5.24 Property with Multiple Conditions

A setter can perform more complex validation.

```python
class Employee:

    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")

        if value < 0:
            raise ValueError("Salary cannot be negative")

        self._salary = value


employee = Employee(50000)

print(employee.salary)

employee.salary = 60000

print(employee.salary)
```

**Output:**

```text
50000
60000
```

This demonstrates how properties can combine:

- Type validation
- Range validation
- Business rules

---

# 🧹 5.25 Property Deleter with Cleanup

A deleter can perform additional work before deleting data.

```python
class User:

    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.deleter
    def username(self):
        print(f"Removing user: {self._username}")
        del self._username


user = User("Sonal")

print(user.username)

del user.username
```

**Output:**

```text
Sonal
Removing user: Sonal
```

A deleter is useful when deletion requires additional logic.

---

# 🏆 5.26 Best Practices

1. Use `@property` when an attribute requires controlled access.
2. Use a private-style internal attribute such as `_name` to store the actual value.
3. Use setters for validation.
4. Use read-only properties for calculated or protected values.
5. Avoid unnecessary properties for simple attributes.
6. Keep property logic short and understandable.
7. Raise appropriate exceptions for invalid values.
8. Avoid recursive references such as `return self.name` inside the `name` property.
9. Use descriptive property names.
10. Use properties to maintain a clean public interface while hiding implementation details.

---

# ⭐ Key Points — Property Decorators

- `@property` converts a method into an attribute-like property.
- A property getter is created using `@property`.
- A setter is created using `@property_name.setter`.
- A deleter is created using `@property_name.deleter`.
- Properties allow controlled access to data.
- Getters are used to read values.
- Setters are used to modify values.
- Deleters are used to delete values.
- Setters are useful for validation.
- Properties can calculate values dynamically.
- A property can be read-only if no setter is defined.
- Internal values are commonly stored using names such as `_name`.
- Properties provide a clean interface without exposing internal implementation details.

---

# 📊 Quick Revision Table

| Concept | Syntax | Purpose |
|---|---|---|
| Property | `@property` | Create a property/getter |
| Getter | `@property` | Read a value |
| Setter | `@name.setter` | Modify a value |
| Deleter | `@name.deleter` | Delete a value |
| Internal Attribute | `self._name` | Store underlying data |
| Validation | Inside setter | Prevent invalid data |
| Read-only Property | Getter without setter | Prevent normal assignment |
| Calculated Property | Getter with calculation | Compute values dynamically |

---

# 🧪 Complete Example — Getter + Setter + Deleter + Validation

```python
class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")

        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not 1 <= value <= 100:
            raise ValueError("Age must be between 1 and 100")

        self._age = value

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self._marks = value

    @property
    def percentage(self):
        return self._marks

    @name.deleter
    def name(self):
        print("Deleting student name...")
        del self._name


student = Student("Sonal", 21, 95)

print("Name:", student.name)
print("Age:", student.age)
print("Marks:", student.marks)
print("Percentage:", student.percentage)

student.marks = 98

print("Updated Marks:", student.marks)

del student.name
```

**Output:**

```text
Name: Sonal
Age: 21
Marks: 95
Percentage: 95
Updated Marks: 98
Deleting student name...
```

This example combines:

- `@property`
- Getter
- Setter
- Deleter
- Validation
- Internal attributes
- Calculated property
- Controlled data access

---

# 🚀 Summary

Property decorators allow Python classes to provide a clean attribute-like interface while maintaining complete control over how data is accessed, modified, and deleted.

The basic property pattern is:

```text
@property
    ↓
Getter
    ↓
Read the value

@property.setter
    ↓
Setter
    ↓
Modify the value

@property.deleter
    ↓
Deleter
    ↓
Delete the value
```

The most important pattern to remember is:

```python
class Student:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name
```

Properties are especially useful when we need:

- Validation
- Encapsulation
- Read-only attributes
- Calculated attributes
- Controlled modification
- Controlled deletion

Understanding property decorators provides an important foundation for the next advanced OOP concepts, especially **encapsulation and controlled access to object data**.

# ➕ Part 5 — Operator Overloading

# ⚙️ 6. Operator Overloading

## 🧠 Basic Concept

**Operator overloading** allows us to define how operators such as `+`, `-`, `*`, `==`, `<`, and `>` behave when they are used with objects of our own classes.

Python already knows how operators work with built-in data types.

For example:

```python
print(10 + 20)
```

**Output:**

```text
30
```

For strings:

```python
print("Hello " + "World")
```

**Output:**

```text
Hello World
```

The same `+` operator behaves differently depending on the types of its operands.

This is an example of **polymorphic behavior**.

With custom classes, we can define similar behavior by implementing special methods, also called **magic methods** or **dunder methods**.

---

# 🔤 6.1 What Are Magic Methods?

Magic methods are special methods whose names begin and end with double underscores.

For example:

```python
__init__
__str__
__len__
__add__
__eq__
```

They allow Python objects to interact with built-in language features and operators.

### Example

When we write:

```python
a + b
```

Python can internally call:

```python
a.__add__(b)
```

Similarly:

```python
a == b
```

can internally use:

```python
a.__eq__(b)
```

And:

```python
str(a)
```

uses:

```python
a.__str__()
```

---

# ➕ 6.2 Operator Overloading with `__add__()`

The `__add__()` method defines the behavior of the `+` operator.

### Basic Example

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

result = num1 + num2

print(result)
```

**Output:**

```text
30
```

When Python sees:

```python
num1 + num2
```

it effectively performs:

```python
num1.__add__(num2)
```

---

# 🔢 6.3 Arithmetic Operators

Python provides several special methods for arithmetic operators.

| Operator | Special Method | Meaning |
|---|---|---|
| `+` | `__add__()` | Addition |
| `-` | `__sub__()` | Subtraction |
| `*` | `__mul__()` | Multiplication |
| `/` | `__truediv__()` | True division |
| `//` | `__floordiv__()` | Floor division |
| `%` | `__mod__()` | Modulus |
| `**` | `__pow__()` | Power |

---

# ➖ 6.4 Overloading `-`

The `__sub__()` method defines the behavior of the `-` operator.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


num1 = Number(30)
num2 = Number(10)

print(num1 - num2)
```

**Output:**

```text
20
```

---

# ✖️ 6.5 Overloading `*`

The `__mul__()` method defines the behavior of `*`.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value


num1 = Number(5)
num2 = Number(4)

print(num1 * num2)
```

**Output:**

```text
20
```

---

# ➗ 6.6 Overloading `/`

The `__truediv__()` method defines true division.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return self.value / other.value


num1 = Number(20)
num2 = Number(5)

print(num1 / num2)
```

**Output:**

```text
4.0
```

---

# 🔢 6.7 Overloading `%`

The `__mod__()` method defines the modulus operator.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __mod__(self, other):
        return self.value % other.value


num1 = Number(17)
num2 = Number(5)

print(num1 % num2)
```

**Output:**

```text
2
```

---

# ⚡ 6.8 Overloading `**`

The `__pow__()` method defines the power operator.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __pow__(self, other):
        return self.value ** other.value


num1 = Number(2)
num2 = Number(3)

print(num1 ** num2)
```

**Output:**

```text
8
```

---

# 🆚 6.9 Comparison Operators

Comparison operators can also be overloaded.

Common comparison operators include:

```text
==    !=    <    >    <=    >=
```

Python provides special methods for these operators.

| Operator | Special Method |
|---|---|
| `==` | `__eq__()` |
| `!=` | `__ne__()` |
| `<` | `__lt__()` |
| `>` | `__gt__()` |
| `<=` | `__le__()` |
| `>=` | `__ge__()` |

---

# 🟰 6.10 Overloading `==` with `__eq__()`

The `__eq__()` method defines equality comparison.

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks


student1 = Student(90)
student2 = Student(90)

print(student1 == student2)
```

**Output:**

```text
True
```

Without defining suitable equality behavior, two separate objects generally compare based on object identity rather than their stored values.

---

# ❌ 6.11 Overloading `!=` with `__ne__()`

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __ne__(self, other):
        return self.marks != other.marks


student1 = Student(90)
student2 = Student(80)

print(student1 != student2)
```

**Output:**

```text
True
```

---

# 🔽 6.12 Overloading `<` with `__lt__()`

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = Student(70)
student2 = Student(90)

print(student1 < student2)
```

**Output:**

```text
True
```

---

# 🔼 6.13 Overloading `>` with `__gt__()`

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


student1 = Student(90)
student2 = Student(70)

print(student1 > student2)
```

**Output:**

```text
True
```

---

# 🔽 6.14 Overloading `<=` and `>=`

The special methods are:

```python
__le__()
__ge__()
```

### Example

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value


num1 = Number(10)
num2 = Number(20)

print(num1 <= num2)
print(num1 >= num2)
```

**Output:**

```text
True
False
```

---

# 📝 6.15 `__str__()`

The `__str__()` method defines the **human-readable string representation** of an object.

When we use:

```python
print(object)
```

Python uses the object's string representation.

### Without `__str__()`

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Sonal", 21)

print(student)
```

The output will usually look similar to:

```text
<__main__.Student object at 0x...>
```

This is not very useful for users.

---

# ✨ 6.16 Using `__str__()`

We can define a meaningful representation.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"


student = Student("Sonal", 21)

print(student)
```

**Output:**

```text
Student(name=Sonal, age=21)
```

Now the object has a meaningful human-readable representation.

---

# 🧠 6.17 How `__str__()` Works

When we write:

```python
print(student)
```

Python effectively asks the object for its string representation.

Conceptually:

```python
str(student)
```

uses:

```python
student.__str__()
```

Therefore:

```python
print(student)
```

and:

```python
print(str(student))
```

both use the `__str__()` representation.

---

# 📏 6.18 `__len__()`

The `__len__()` method defines what happens when `len()` is used on an object.

### Example

```python
class Team:

    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


team = Team(["A", "B", "C", "D"])

print(len(team))
```

**Output:**

```text
4
```

Python effectively calls:

```python
team.__len__()
```

when we use:

```python
len(team)
```

---

# 📚 6.19 `__len__()` with Custom Data

```python
class Course:

    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)


course = Course([
    "Python",
    "OOP",
    "DSA",
    "Machine Learning"
])

print(len(course))
```

**Output:**

```text
4
```

---

# 🧮 6.20 Complete Arithmetic Operator Example

We can implement several operators in the same class.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __str__(self):
        return str(self.value)


num1 = Number(20)
num2 = Number(10)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
```

**Output:**

```text
30
10
200
```

Notice that the arithmetic methods return another `Number` object:

```python
return Number(...)
```

The `__str__()` method then controls how that result is displayed.

---

# 🔗 6.21 Chaining Operator Overloading

Because our arithmetic methods return `Number` objects, we can perform operations repeatedly.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __str__(self):
        return str(self.value)


num1 = Number(10)
num2 = Number(20)
num3 = Number(5)

result = (num1 + num2) * num3

print(result)
```

**Output:**

```text
150
```

The execution is conceptually:

```text
num1 + num2
      ↓
Number(30)
      ↓
Number(30) * num3
      ↓
Number(150)
```

---

# 🎯 6.22 Practical Example — Vector Addition

Operator overloading is useful for mathematical objects.

Consider a two-dimensional vector:

```text
(x, y)
```

We can define vector addition using `+`.

```python
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

result = v1 + v2

print(result)
```

**Output:**

```text
(6, 8)
```

This is much more readable than manually writing:

```python
Vector(
    v1.x + v2.x,
    v1.y + v2.y
)
```

every time.

---

# 📐 6.23 Practical Example — Vector Comparison

We can also compare vectors based on their magnitude.

```python
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()


v1 = Vector(3, 4)
v2 = Vector(6, 8)

print(v1 < v2)
```

**Output:**

```text
True
```

Here:

```text
Magnitude of v1 = 5
Magnitude of v2 = 10
```

Therefore:

```python
v1 < v2
```

returns:

```text
True
```

---

# 💰 6.24 Practical Example — Money

Operator overloading can make custom financial objects easier to use.

```python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __str__(self):
        return f"₹{self.amount}"


money1 = Money(500)
money2 = Money(300)

print(money1 + money2)
print(money1 - money2)
print(money1 == money2)
```

**Output:**

```text
₹800
₹200
False
```

The class now behaves naturally with arithmetic and comparison operators.

---

# 🤖 6.25 AI/ML Use Case — Vector Objects

Operator overloading has an important connection to mathematical and scientific programming.

Machine learning frequently works with:

- Vectors
- Matrices
- Tensors
- Numerical objects
- Model parameters
- Coordinates

For example, a custom vector class could support:

```python
vector1 + vector2
```

instead of:

```python
Vector(
    vector1.x + vector2.x,
    vector1.y + vector2.y
)
```

This makes mathematical code more readable.

Libraries such as NumPy and scientific computing frameworks use similar ideas to provide natural mathematical syntax for numerical objects.

---

# 🧠 6.26 Operator Overloading Is Not Creating New Operators

Operator overloading does **not** allow us to invent new operators.

We cannot create an operator such as:

```text
@@
```

just by defining a special method.

Instead, operator overloading means:

> Defining how an existing Python operator behaves for objects of a custom class.

For example:

```python
+
-
*
/
==
<
>
```

can have custom behavior through their corresponding special methods.

---

# ⚠️ 6.27 Return Types Matter

Operator methods should generally return a meaningful value.

For example:

```python
def __add__(self, other):
    return self.value + other.value
```

returns an integer.

But:

```python
def __add__(self, other):
    return Number(self.value + other.value)
```

returns a `Number` object.

Both can be valid depending on the design.

### Example

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
```

This allows further operations on the returned object.

---

# 🔄 6.28 Reflected Arithmetic Operators

Python also provides reflected arithmetic methods.

Examples include:

| Operator | Normal Method | Reflected Method |
|---|---|---|
| `+` | `__add__()` | `__radd__()` |
| `-` | `__sub__()` | `__rsub__()` |
| `*` | `__mul__()` | `__rmul__()` |
| `/` | `__truediv__()` | `__rtruediv__()` |

These become useful when the custom object appears on the **right-hand side** of an operation.

For example:

```python
10 + obj
```

may involve:

```python
obj.__radd__(10)
```

if the normal operation cannot handle the operands.

---

# 🔢 6.29 Example of `__radd__()`

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __radd__(self, other):
        return self.value + other


num = Number(10)

print(5 + num)
```

**Output:**

```text
15
```

Here the custom object appears on the right side of `+`.

---

# 🔢 6.30 Unary Operators

Python also supports special methods for unary operators.

| Operator | Special Method |
|---|---|
| `-obj` | `__neg__()` |
| `+obj` | `__pos__()` |
| `abs(obj)` | `__abs__()` |

### Example

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return Number(-self.value)

    def __abs__(self):
        return abs(self.value)

    def __str__(self):
        return str(self.value)


num = Number(-10)

print(-num)
print(abs(num))
```

**Output:**

```text
10
10
```

---

# 📊 6.31 Common Operator Overloading Methods

| Operation | Method |
|---|---|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `//` | `__floordiv__()` |
| `%` | `__mod__()` |
| `**` | `__pow__()` |
| `==` | `__eq__()` |
| `!=` | `__ne__()` |
| `<` | `__lt__()` |
| `>` | `__gt__()` |
| `<=` | `__le__()` |
| `>=` | `__ge__()` |
| `str(obj)` | `__str__()` |
| `len(obj)` | `__len__()` |
| `-obj` | `__neg__()` |
| `+obj` | `__pos__()` |
| `abs(obj)` | `__abs__()` |

---

# 🧩 6.32 Operator Overloading and Readability

Good operator overloading should make code easier to understand.

Good example:

```python
total = price1 + price2
```

when `price1` and `price2` are meaningful money objects.

Another good example:

```python
result = vector1 + vector2
```

when both objects represent mathematical vectors.

Poor operator overloading would define `+` to perform an unrelated operation that users would not naturally expect.

Therefore, operator overloading should be **intuitive and consistent**.

---

# ⚠️ 6.33 Common Beginner Mistakes

## Mistake 1 — Forgetting `self`

Incorrect:

```python
def __add__(other):
    return self.value + other.value
```

Correct:

```python
def __add__(self, other):
    return self.value + other.value
```

---

## Mistake 2 — Forgetting `return`

Incorrect:

```python
def __add__(self, other):
    self.value + other.value
```

The expression is calculated but not returned.

Correct:

```python
def __add__(self, other):
    return self.value + other.value
```

---

## Mistake 3 — Returning an Unexpected Type

If a class is designed to work with other objects of the same class, returning an unrelated type can make further operations confusing.

Always decide clearly whether an operator should return:

- A primitive value
- A new object
- A boolean
- Another meaningful result

---

## Mistake 4 — Making Operators Behave Unexpectedly

Avoid defining:

```python
obj1 + obj2
```

to perform something completely unrelated to addition.

Operator overloading should follow intuitive behavior.

---

## Mistake 5 — Forgetting `__str__()`

Without `__str__()`, printing custom objects can produce an unhelpful representation.

Adding:

```python
def __str__(self):
    return "..."
```

can make debugging and output much clearer.

---

# 🏆 6.34 Best Practices

1. Use operator overloading only when it makes the class easier to use.
2. Keep operator behavior intuitive.
3. Use the appropriate special method for each operator.
4. Return meaningful values from operator methods.
5. Validate operand types when necessary.
6. Use `__str__()` for readable object output.
7. Use `__len__()` when the object has a meaningful size or length.
8. Consider reflected methods such as `__radd__()` when operand order matters.
9. Avoid overloading operators for unrelated behavior.
10. Document unusual operator behavior.
11. Keep custom mathematical classes consistent with normal mathematical expectations.
12. Prefer readable and predictable object behavior.

---

# ⭐ Key Points — Operator Overloading

- Operator overloading defines how existing Python operators work with custom objects.
- It is implemented using special methods.
- Special methods are also called magic methods or dunder methods.
- `__add__()` controls `+`.
- `__sub__()` controls `-`.
- `__mul__()` controls `*`.
- `__truediv__()` controls `/`.
- `__eq__()` controls `==`.
- `__lt__()` controls `<`.
- `__gt__()` controls `>`.
- `__str__()` controls the human-readable representation of an object.
- `__len__()` controls the result of `len(object)`.
- Reflected methods such as `__radd__()` handle reversed operand situations.
- Operator overloading should make custom objects natural and readable.
- It is widely useful for mathematical and scientific objects.

---

# 📊 Quick Revision Table

| Concept | Example | Special Method |
|---|---|---|
| Addition | `a + b` | `__add__()` |
| Subtraction | `a - b` | `__sub__()` |
| Multiplication | `a * b` | `__mul__()` |
| Division | `a / b` | `__truediv__()` |
| Equality | `a == b` | `__eq__()` |
| Less Than | `a < b` | `__lt__()` |
| Greater Than | `a > b` | `__gt__()` |
| String Conversion | `str(a)` | `__str__()` |
| Length | `len(a)` | `__len__()` |
| Unary Negative | `-a` | `__neg__()` |
| Unary Positive | `+a` | `__pos__()` |
| Absolute Value | `abs(a)` | `__abs__()` |

---

# 🧪 Complete Practical Example — `Vector` Class

```python
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(2, 1)

print("v1:", v1)
print("v2:", v2)

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Equal:", v1 == v2)
print("Magnitude:", len(v1))
```

**Output:**

```text
v1: Vector(3, 4)
v2: Vector(2, 1)
Addition: Vector(5, 5)
Subtraction: Vector(1, 3)
Equal: False
Magnitude: 5
```

This example demonstrates:

- `__init__()`
- `__add__()`
- `__sub__()`
- `__eq__()`
- `__len__()`
- `__str__()`

It shows how a custom object can behave naturally with Python operators and built-in functions.

---

# 🚀 Summary

**Operator overloading** allows custom Python objects to work naturally with existing operators and built-in functions.

Instead of writing complicated method calls such as:

```python
vector1.add(vector2)
```

we can define:

```python
vector1 + vector2
```

using:

```python
__add__()
```

Similarly:

```text
a - b       → __sub__()
a * b       → __mul__()
a / b       → __truediv__()
a == b      → __eq__()
a < b       → __lt__()
a > b       → __gt__()
str(a)      → __str__()
len(a)      → __len__()
```

The most important idea is:

```text
Python Operator
      ↓
Special / Dunder Method
      ↓
Custom Class Behavior
```

Operator overloading is particularly useful for classes representing:

- Vectors
- Matrices
- Money
- Measurements
- Dates
- Complex numbers
- Scientific data
- Machine learning objects

When used correctly, operator overloading makes custom classes **more natural, readable, expressive, and Pythonic**.

# 🔐 Part 6 — Encapsulation

# 🔐 7. Encapsulation

## 🧠 Basic Concept

**Encapsulation** is the concept of bundling data and the methods that operate on that data inside a class while controlling how that data can be accessed or modified.

In simple words:

> **Encapsulation means keeping related data and behavior together and controlling access to the internal data of an object.**

For example, consider a bank account.

A bank account has:

- Account holder
- Account number
- Balance
- Deposit operation
- Withdrawal operation

We should not allow anyone to freely change the balance to an invalid value.

Instead of:

```python
account.balance = -50000
```

we can control how the balance is changed.

This is where encapsulation becomes useful.

---

# 🎯 7.1 Why Do We Need Encapsulation?

Encapsulation helps us:

1. Protect important data.
2. Control how data is accessed.
3. Prevent accidental modification.
4. Validate data before storing it.
5. Hide implementation details.
6. Make code easier to maintain.
7. Improve security and reliability.
8. Keep related data and behavior together.

### Real-Life Example

Think about an ATM.

You can:

- Check your balance.
- Deposit money.
- Withdraw money.

But you cannot directly access the bank's internal database and modify your balance.

The system provides controlled operations.

Similarly, encapsulation allows a class to expose controlled ways of interacting with its internal data.

---

# 🔒 7.2 Access Modifiers

Python does not have strict access modifiers in exactly the same way as languages such as Java or C++.

Instead, Python uses naming conventions and **name mangling** to communicate and partially enforce different levels of access.

Python commonly uses:

```text
Public
Protected
Private
```

The syntax is:

```text
name       → Public
_name      → Protected by convention
__name     → Private-style name mangling
```

---

# 🌐 7.3 Public Members

A **public member** can be accessed from anywhere.

It is written without a leading underscore.

### Example

```python
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Sonal")

print(student.name)
```

**Output:**

```text
Sonal
```

Here:

```python
self.name
```

is a public attribute.

It can be accessed directly:

```python
student.name
```

---

# 🧠 7.4 Public Methods

Methods without a leading underscore are also considered public.

```python
class Student:

    def show(self):
        print("Student details")


student = Student()

student.show()
```

**Output:**

```text
Student details
```

The method:

```python
show()
```

is public.

---

# 🛡️ 7.5 Protected Members

A protected member is written with a **single leading underscore**.

```python
_name
```

This indicates:

> This member is intended for internal use within the class and its subclasses.

### Example

```python
class Student:

    def __init__(self, name):
        self._name = name


student = Student("Sonal")

print(student._name)
```

**Output:**

```text
Sonal
```

Notice that Python still allows:

```python
student._name
```

So a single underscore does **not** make the attribute truly inaccessible.

It is primarily a convention.

---

# 🧬 7.6 Protected Members with Inheritance

Protected members are commonly used when a subclass needs access to data defined by its parent.

```python
class Person:

    def __init__(self, name):
        self._name = name


class Student(Person):

    def show_name(self):
        print(self._name)


student = Student("Sonal")

student.show_name()
```

**Output:**

```text
Sonal
```

The subclass can access:

```python
self._name
```

because the single underscore is mainly a convention indicating internal/protected-style use.

---

# 🔐 7.7 Private Members

A private-style member is written using **two leading underscores**.

```python
__name
```

Python applies **name mangling** to such names.

### Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


account = BankAccount(5000)
```

Trying:

```python
print(account.__balance)
```

will result in an `AttributeError`.

This happens because Python internally changes the name.

---

# 🧩 7.8 Private Variables

A private variable is commonly used when we want to discourage direct access from outside the class.

### Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)


account = BankAccount(5000)

account.show_balance()
```

**Output:**

```text
5000
```

The balance is stored as:

```python
self.__balance
```

and accessed through a method.

---

# 🧬 7.9 Name Mangling

Python uses **name mangling** for identifiers beginning with two underscores and not ending with two underscores.

For example:

```python
self.__balance
```

is internally transformed approximately into:

```python
self._BankAccount__balance
```

### Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


account = BankAccount(5000)

print(account._BankAccount__balance)
```

**Output:**

```text
5000
```

This demonstrates that Python's private members are not truly inaccessible.

The purpose of name mangling is mainly to:

- Avoid accidental name conflicts.
- Protect attributes from accidental overriding in subclasses.
- Discourage direct external access.

---

# ⚠️ 7.10 Important Point About Private Members

Python does **not** provide absolute private access like some languages.

This:

```python
__balance
```

does not mean:

> Nobody can ever access this variable.

Instead, Python changes its name through name mangling.

Therefore, it is better to think of `__name` as:

> **Private-style access with name mangling.**

rather than as a completely inaccessible variable.

---

# 📊 7.11 Public vs Protected vs Private

| Type | Syntax | Accessibility | Meaning |
|---|---|---|---|
| Public | `name` | Everywhere | Normal public member |
| Protected | `_name` | Technically accessible | Internal-use convention |
| Private | `__name` | Name-mangled | Stronger protection against accidental access |

---

# 🔎 7.12 Access Modifier Example

```python
class Student:

    def __init__(self):
        self.name = "Sonal"
        self._course = "Python"
        self.__marks = 95


student = Student()

print(student.name)
print(student._course)

# print(student.__marks)
```

**Output:**

```text
Sonal
Python
```

The following line:

```python
student.__marks
```

will raise an `AttributeError`.

---

# 🧠 7.13 Why Use Private Variables?

Private variables are useful when direct external modification should be discouraged.

For example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

Instead of allowing:

```python
account.balance = -100000
```

we can provide controlled methods:

```python
deposit()
withdraw()
```

This lets the class control how its internal state changes.

---

# 💰 7.14 Practical Example — Bank Account

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)

account.show_balance()

account.deposit(2000)
account.show_balance()

account.withdraw(1000)
account.show_balance()
```

**Output:**

```text
Balance: 5000
Balance: 7000
Balance: 6000
```

The balance is stored internally as:

```python
self.__balance
```

and can only be modified through controlled methods.

---

# 📥 7.15 Getters

A **getter** is a method used to retrieve the value of an internal attribute.

### Example

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student = Student(95)

print(student.get_marks())
```

**Output:**

```text
95
```

Here:

```python
get_marks()
```

is the getter.

---

# ✏️ 7.16 Setters

A **setter** is a method used to modify an internal attribute.

### Example

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student = Student(80)

print(student.get_marks())

student.set_marks(95)

print(student.get_marks())
```

**Output:**

```text
80
95
```

---

# 🛡️ 7.17 Setter Validation

Setters become especially useful when we need validation.

Suppose marks must be between `0` and `100`.

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100")


student = Student(80)

print(student.get_marks())

student.set_marks(95)

print(student.get_marks())
```

**Output:**

```text
80
95
```

If we try:

```python
student.set_marks(150)
```

Python raises:

```text
ValueError: Marks must be between 0 and 100
```

---

# 🔐 7.18 Encapsulation with Getters and Setters

A common encapsulation pattern is:

```text
Private Data
     ↓
   Getter
     ↓
Read Data

Private Data
     ↑
   Setter
     ↑
Modify Data
```

### Example

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Invalid marks")
```

The internal data is not directly exposed through a normal public attribute.

---

# 🏠 7.19 Property Decorators and Encapsulation

Python provides a cleaner way to implement getters and setters using **property decorators**.

Instead of:

```python
student.get_marks()
student.set_marks(95)
```

we can write:

```python
student.marks
student.marks = 95
```

while still controlling the internal data.

### Example

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")


student = Student(85)

print(student.marks)

student.marks = 95

print(student.marks)
```

**Output:**

```text
85
95
```

The property provides controlled access while maintaining simple attribute syntax.

---

# 🔄 7.20 Traditional Getter/Setter vs Property

### Traditional Approach

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Invalid marks")


student = Student(90)

print(student.get_marks())

student.set_marks(95)

print(student.get_marks())
```

### Property Approach

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Invalid marks")


student = Student(90)

print(student.marks)

student.marks = 95

print(student.marks)
```

The property approach is generally more natural in Python.

---

# 🧠 7.21 Encapsulation Does Not Mean Hiding Everything

Encapsulation does not mean that every variable must be private.

For example, a simple class can legitimately have public attributes:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

There is no need to make every attribute private automatically.

Use access control when it provides a meaningful benefit such as:

- Validation
- Preventing accidental modification
- Protecting internal implementation
- Maintaining class invariants
- Providing a controlled interface

---

# ⚙️ 7.22 Class Invariants

A **class invariant** is a condition that should remain true for an object's state.

For example, a bank account might require:

```text
balance >= 0
```

A student might require:

```text
0 <= marks <= 100
```

Encapsulation helps maintain these rules.

### Example

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self._marks = value
```

Now every assignment through the property is validated.

---

# 🏦 7.23 Practical Example — Bank Account with Property

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount


account = BankAccount(5000)

print("Initial Balance:", account.balance)

account.deposit(2000)

print("After Deposit:", account.balance)

account.withdraw(1000)

print("After Withdrawal:", account.balance)
```

**Output:**

```text
Initial Balance: 5000
After Deposit: 7000
After Withdrawal: 6000
```

This combines:

- Encapsulation
- Property decorators
- Getter
- Setter
- Validation
- Controlled modification

---

# 🔑 7.24 Private Methods

Encapsulation can also be applied to methods.

A method beginning with two underscores is subject to name mangling.

### Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def __calculate_interest(self):
        return self.__balance * 0.05

    def show_interest(self):
        print("Interest:", self.__calculate_interest())


account = BankAccount(10000)

account.show_interest()
```

**Output:**

```text
Interest: 500.0
```

Here:

```python
__calculate_interest()
```

is a private-style method.

It is intended to be used internally by the class.

---

# 🧩 7.25 Public Interface and Internal Implementation

A well-encapsulated class usually exposes a clear **public interface** while keeping implementation details internal.

For example:

```python
account.deposit(1000)
```

is part of the public interface.

The user of the class does not need to know exactly how the balance is stored internally.

The implementation might use:

```python
self._balance
```

or:

```python
self.__balance
```

The internal representation can change without requiring the user to change how they interact with the class.

This is an important benefit of encapsulation.

---

# 🔄 7.26 Encapsulation and Abstraction

Encapsulation and abstraction are related but different concepts.

### Encapsulation

Focuses on:

```text
How data and behavior are bundled
and how access to internal state is controlled.
```

### Abstraction

Focuses on:

```text
What functionality is exposed
while hiding unnecessary implementation details.
```

For example, a bank account class can encapsulate its balance and provide simple operations such as:

```python
deposit()
withdraw()
```

The user does not need to know the internal implementation.

---

# 📊 7.27 Encapsulation vs Abstraction

| Encapsulation | Abstraction |
|---|---|
| Bundles data and methods | Hides unnecessary complexity |
| Controls access to data | Focuses on essential behavior |
| Uses properties, naming conventions, methods | Uses abstract classes, interfaces, etc. |
| Protects internal state | Simplifies usage |
| Concerned with access | Concerned with design |

Both concepts are important parts of object-oriented programming.

---

# 🧬 7.28 Encapsulation with Inheritance

Private members behave differently with inheritance because of name mangling.

### Example

```python
class Parent:

    def __init__(self):
        self.__value = 100


class Child(Parent):

    def show(self):
        # print(self.__value)
        pass
```

The child class cannot directly access:

```python
self.__value
```

as if it were an ordinary inherited attribute.

The name has been mangled using the parent class name.

This is one reason why protected-style attributes:

```python
self._value
```

are often used when subclasses are expected to access the value.

---

# 🛡️ 7.29 Protected vs Private with Inheritance

### Protected

```python
class Parent:

    def __init__(self):
        self._value = 100


class Child(Parent):

    def show(self):
        print(self._value)


child = Child()

child.show()
```

**Output:**

```text
100
```

### Private

```python
class Parent:

    def __init__(self):
        self.__value = 100


class Child(Parent):

    def show(self):
        # print(self.__value)
        pass
```

The private-style name is mangled, so it is not directly available to the child under the same name.

---

# ⚠️ 7.30 Common Beginner Mistakes

## Mistake 1 — Thinking `_name` Is Truly Private

This:

```python
self._name
```

is only a convention.

Python still allows:

```python
object._name
```

It means:

> "This is intended for internal use."

---

## Mistake 2 — Thinking `__name` Is Completely Inaccessible

Python uses name mangling:

```python
self.__name
```

becomes approximately:

```python
self._ClassName__name
```

So it is not absolute security.

---

## Mistake 3 — Making Every Attribute Private

Not every attribute needs to be hidden.

For simple data:

```python
self.name = name
```

may be perfectly appropriate.

Use encapsulation when it provides a meaningful benefit.

---

## Mistake 4 — Forgetting Validation

If a setter is used, it is often useful to validate incoming values.

For example:

```python
@marks.setter
def marks(self, value):
    if not 0 <= value <= 100:
        raise ValueError("Invalid marks")

    self._marks = value
```

---

## Mistake 5 — Creating Recursive Properties

Incorrect:

```python
@property
def name(self):
    return self.name
```

Correct:

```python
@property
def name(self):
    return self._name
```

---

# 🏆 7.31 Best Practices

1. Use public attributes when no access control is needed.
2. Use `_name` to communicate internal or protected-style usage.
3. Use `__name` when name mangling provides a useful benefit.
4. Do not treat Python's private naming as a security mechanism.
5. Use getters and setters when controlled access is required.
6. Prefer properties when you want attribute-like syntax.
7. Validate values inside setters.
8. Keep class invariants protected.
9. Expose a clear public interface.
10. Hide unnecessary implementation details.
11. Do not make every attribute private without a reason.
12. Use encapsulation to improve maintainability and reliability.
13. Use protected-style attributes when subclasses are intentionally expected to access internal state.
14. Use private-style attributes to reduce accidental name conflicts and accidental access.

---

# 🤖 7.32 AI/ML Use Case

Encapsulation is useful when designing machine learning classes.

For example, a model configuration may contain parameters that should follow specific rules.

```python
class ModelConfig:

    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if value <= 0:
            raise ValueError("Learning rate must be positive")

        self._learning_rate = value


config = ModelConfig(0.001)

print(config.learning_rate)

config.learning_rate = 0.01

print(config.learning_rate)
```

**Output:**

```text
0.001
0.01
```

Encapsulation can help protect values such as:

- Learning rate
- Batch size
- Number of epochs
- Model threshold
- Confidence threshold
- Regularization parameters
- Dataset configuration

---

# 🔬 7.33 Practical Example — Machine Learning Model Configuration

```python
class ModelConfig:

    def __init__(self, learning_rate, epochs, batch_size):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if value <= 0:
            raise ValueError("Learning rate must be positive")

        self._learning_rate = value

    @property
    def epochs(self):
        return self._epochs

    @epochs.setter
    def epochs(self, value):
        if value <= 0:
            raise ValueError("Epochs must be positive")

        self._epochs = value

    @property
    def batch_size(self):
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value):
        if value <= 0:
            raise ValueError("Batch size must be positive")

        self._batch_size = value


config = ModelConfig(
    learning_rate=0.001,
    epochs=50,
    batch_size=32
)

print("Learning Rate:", config.learning_rate)
print("Epochs:", config.epochs)
print("Batch Size:", config.batch_size)
```

**Output:**

```text
Learning Rate: 0.001
Epochs: 50
Batch Size: 32
```

This demonstrates how encapsulation can protect important configuration values from invalid assignments.

---

# ⭐ Key Points — Encapsulation

- Encapsulation bundles data and methods inside a class.
- It controls how internal data is accessed and modified.
- Python commonly uses public, protected-style, and private-style naming conventions.
- Public members use normal names.
- Protected-style members use a single leading underscore.
- Private-style members use two leading underscores.
- Python uses name mangling for private-style names.
- `_name` is a convention, not strict access control.
- `__name` uses name mangling.
- Getters are used to retrieve internal values.
- Setters are used to modify internal values.
- Setters can validate data.
- Property decorators provide a clean way to implement controlled access.
- Encapsulation helps maintain class invariants.
- Encapsulation improves maintainability and reduces accidental misuse.
- Python's private naming mechanism is not a security boundary.
- Encapsulation and abstraction are related but represent different concepts.

---

# 📊 Quick Revision Table

| Concept | Syntax | Purpose |
|---|---|---|
| Public | `name` | Normal accessible member |
| Protected | `_name` | Internal-use convention |
| Private | `__name` | Name-mangled member |
| Getter | `get_name()` | Read internal data |
| Setter | `set_name()` | Modify internal data |
| Property Getter | `@property` | Attribute-style reading |
| Property Setter | `@name.setter` | Attribute-style modification |
| Name Mangling | `_ClassName__name` | Internal transformed name |
| Encapsulation | Class + controlled access | Protect and manage internal state |
| Class Invariant | Validation rule | Keep object state valid |

---

# 🧪 Complete Example — Encapsulation with Property and Validation

```python
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be a number")

        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

    def display(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


account = BankAccount("Sonal", 5000)

account.display()

account.deposit(2000)

print("\nAfter Deposit:")
account.display()

account.withdraw(1000)

print("\nAfter Withdrawal:")
account.display()
```

**Output:**

```text
Owner: Sonal
Balance: 5000

After Deposit:
Owner: Sonal
Balance: 7000

After Withdrawal:
Owner: Sonal
Balance: 6000
```

This example combines the major concepts of encapsulation:

- Public attribute
- Protected-style internal attribute
- Property
- Getter
- Setter
- Validation
- Controlled modification
- Class methods that operate on internal state
- A clear public interface

---

# 🚀 Summary

**Encapsulation** is an important OOP concept that helps us bundle data and behavior together while controlling access to the internal state of an object.

Python provides three commonly discussed access levels:

```text
Public
   ↓
name

Protected
   ↓
_name

Private-style
   ↓
__name
```

The important difference is that Python does not enforce these levels in the same strict way as some other programming languages.

A single underscore:

```python
_name
```

is mainly a convention.

A double underscore:

```python
__name
```

causes **name mangling**.

For controlled access, Python commonly uses:

```python
@property
```

and:

```python
@name.setter
```

This allows us to maintain a simple interface such as:

```python
account.balance
```

while still validating and controlling the internal data.

The key relationship to remember is:

```text
Encapsulation
      ↓
Bundle Data + Methods
      ↓
Control Access
      ↓
Validate Data
      ↓
Protect Object State
      ↓
Maintain Reliable Objects
```

Encapsulation is especially useful in larger applications where objects contain important state that should not be modified arbitrarily.

It also provides an important foundation for understanding **polymorphism, abstraction, and composition** in advanced Python OOP.

# 🔄 Part 7 — Polymorphism

# 🔄 8. Polymorphism

## 🧠 Basic Concept

**Polymorphism** is an important concept of Object-Oriented Programming in which the same interface, method, operator, or function can behave differently depending on the object or data it is working with.

The word **polymorphism** comes from:

```text
Poly  → Many
Morph → Forms
```

Therefore:

> **Polymorphism means one interface having multiple forms of behavior.**

### Simple Real-Life Example

A person can behave differently depending on the situation.

For example:

```text
At home       → Family member
At college    → Student
At workplace  → Employee
```

The same person has different roles in different contexts.

Similarly, in Python, the same method name can produce different behavior for different objects.

---

# 🎯 8.1 Why Do We Need Polymorphism?

Polymorphism helps us:

1. Write flexible code.
2. Reduce unnecessary conditional statements.
3. Work with different object types through a common interface.
4. Improve code reusability.
5. Make programs easier to extend.
6. Support loose coupling.
7. Make object-oriented designs cleaner.
8. Allow different classes to implement the same operation differently.

For example, instead of writing separate code for every animal:

```python
if animal_type == "dog":
    ...
elif animal_type == "cat":
    ...
elif animal_type == "cow":
    ...
```

we can give different classes a common method:

```python
animal.sound()
```

and let each class define its own behavior.

---

# 🧩 8.2 Basic Polymorphism Example

```python
class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

**Output:**

```text
Dog barks
Cat meows
```

Both classes have the same method:

```python
sound()
```

but the behavior is different.

This is polymorphism.

---

# 🔄 8.3 Polymorphism with a Common Function

We can write one function that works with different objects.

```python
class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
```

**Output:**

```text
Dog barks
Cat meows
```

The function:

```python
make_sound()
```

does not need to know whether it received a `Dog` or `Cat`.

It simply expects the object to provide:

```python
sound()
```

This makes the code flexible.

---

# 🧬 8.4 Polymorphism Through Inheritance

Polymorphism commonly occurs when a parent class defines a method and child classes provide their own implementations.

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

**Output:**

```text
Dog barks
Cat meows
```

Both `Dog` and `Cat` inherit from `Animal`, but they provide different implementations of:

```python
sound()
```

---

# 🔁 8.5 Method Overriding

**Method overriding** occurs when a child class provides its own implementation of a method that already exists in the parent class.

### Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
```

**Output:**

```text
Animal makes a sound
Dog barks
```

The `Dog` class overrides:

```python
Animal.sound()
```

with its own implementation.

---

# 🧠 8.6 Why Is Method Overriding Polymorphism?

The same method call:

```python
obj.sound()
```

can produce different results depending on the object's class.

For example:

```python
animal.sound()
```

produces:

```text
Animal makes a sound
```

while:

```python
dog.sound()
```

produces:

```text
Dog barks
```

The interface remains:

```python
sound()
```

but the behavior changes.

That is polymorphic behavior.

---

# 🧩 8.7 Multiple Child Classes

Polymorphism becomes more useful when multiple subclasses implement the same method.

```python
class Animal:

    def sound(self):
        print("Some animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


class Cow(Animal):

    def sound(self):
        print("Moo")


animals = [
    Dog(),
    Cat(),
    Cow()
]

for animal in animals:
    animal.sound()
```

**Output:**

```text
Bark
Meow
Moo
```

The loop does not need separate logic for each animal.

It simply calls:

```python
animal.sound()
```

---

# 🔄 8.8 Method Overriding with `super()`

Sometimes a child class wants to extend the parent's implementation rather than completely replace it.

We can use `super()`.

### Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()

dog.sound()
```

**Output:**

```text
Animal makes a sound
Dog barks
```

Here the child class:

1. Calls the parent implementation.
2. Adds its own behavior.

---

# 🧠 8.9 Why Use `super()` with Method Overriding?

Without `super()`:

```python
class Dog(Animal):

    def sound(self):
        print("Dog barks")
```

the parent method is completely replaced for `Dog`.

With:

```python
class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")
```

the child extends the parent behavior.

This is useful when the parent class contains important common functionality.

---

# 🏦 8.10 Practical Example — Payment System

Polymorphism is very useful in real-world software systems.

Consider different payment methods:

```python
class Payment:

    def pay(self, amount):
        print(f"Processing payment of ₹{amount}")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Cash(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


payments = [
    CreditCard(),
    UPI(),
    Cash()
]

for payment in payments:
    payment.pay(1000)
```

**Output:**

```text
Paid ₹1000 using Credit Card
Paid ₹1000 using UPI
Paid ₹1000 using Cash
```

The loop uses the same interface:

```python
payment.pay()
```

but each object behaves differently.

---

# 🦆 8.11 Duck Typing

Python strongly supports a concept known as **Duck Typing**.

The idea comes from the expression:

> "If it walks like a duck and quacks like a duck, then it is a duck."

In programming, this means:

> We care about what an object **can do**, rather than what its exact class is.

### Example

```python
class Dog:

    def speak(self):
        print("Dog barks")


class Person:

    def speak(self):
        print("Person speaks")


def make_speak(obj):
    obj.speak()


dog = Dog()
person = Person()

make_speak(dog)
make_speak(person)
```

**Output:**

```text
Dog barks
Person speaks
```

`Dog` and `Person` do not need to share a parent class.

They simply provide the required method:

```python
speak()
```

---

# 🧠 8.12 Duck Typing vs Inheritance-Based Polymorphism

### Inheritance-Based Polymorphism

```python
class Animal:

    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")
```

The classes share a common parent.

### Duck Typing

```python
class Dog:

    def sound(self):
        print("Bark")


class Car:

    def sound(self):
        print("Horn")
```

There is no inheritance relationship.

If an object has:

```python
sound()
```

a function can use it.

---

# 🔧 8.13 Duck Typing Example

```python
class Duck:

    def swim(self):
        print("Duck is swimming")


class Person:

    def swim(self):
        print("Person is swimming")


def start_swimming(obj):
    obj.swim()


start_swimming(Duck())
start_swimming(Person())
```

**Output:**

```text
Duck is swimming
Person is swimming
```

The function does not check:

```python
isinstance(obj, Duck)
```

It simply calls:

```python
obj.swim()
```

---

# ⚠️ 8.14 Duck Typing and Errors

Duck typing assumes that the object provides the required behavior.

For example:

```python
class Dog:

    def bark(self):
        print("Bark")


def make_sound(obj):
    obj.sound()


make_sound(Dog())
```

This raises:

```text
AttributeError
```

because `Dog` does not have:

```python
sound()
```

Therefore, duck typing provides flexibility, but the expected interface must still be respected.

---

# 🔄 8.15 Method Overloading

**Method overloading** traditionally means having multiple methods with the same name but different parameter lists.

For example, some languages allow:

```text
add(int, int)
add(int, int, int)
add(float, float)
```

Python does **not** support traditional method overloading in the same way.

If we define the same method multiple times inside a class, the latest definition replaces the previous one.

### Example

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
```

The second `add()` replaces the first one.

Therefore:

```python
calculator = Calculator()

print(calculator.add(1, 2))
```

will raise a `TypeError` because the active method expects three arguments in addition to `self`.

---

# 🧠 8.16 How Python Handles Method Overloading

Instead of traditional method overloading, Python commonly uses:

- Default arguments
- `*args`
- `**kwargs`
- Type checking when appropriate
- Flexible function designs

These techniques allow one method to handle different kinds or numbers of arguments.

---

# 🔢 8.17 Method Overloading with Default Arguments

Default arguments can provide different calling patterns.

```python
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


calculator = Calculator()

print(calculator.add(10))
print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))
```

**Output:**

```text
10
30
60
```

One method supports different numbers of arguments.

---

# 🧮 8.18 Another Default Argument Example

```python
class Student:

    def introduce(self, name, course="Python"):
        print(f"My name is {name} and I am learning {course}")


student = Student()

student.introduce("Sonal")
student.introduce("Sonal", "AI/ML")
```

**Output:**

```text
My name is Sonal and I am learning Python
My name is Sonal and I am learning AI/ML
```

The default argument provides flexible behavior.

---

# 🔢 8.19 Method Overloading with `*args`

`*args` allows a function or method to accept a variable number of positional arguments.

### Example

```python
class Calculator:

    def add(self, *args):
        return sum(args)


calculator = Calculator()

print(calculator.add(10))
print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))
print(calculator.add(10, 20, 30, 40))
```

**Output:**

```text
10
30
60
100
```

The same method handles different numbers of arguments.

---

# 🧠 8.20 Understanding `*args`

Suppose we call:

```python
calculator.add(10, 20, 30)
```

Inside the method:

```python
args
```

contains:

```python
(10, 20, 30)
```

It is a tuple.

Therefore:

```python
sum(args)
```

returns:

```text
60
```

---

# 🔑 8.21 Method Flexibility with `**kwargs`

`**kwargs` allows a method to accept a variable number of keyword arguments.

### Example

```python
class Student:

    def show_details(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")


student = Student()

student.show_details(
    name="Sonal",
    age=21,
    course="AI/ML"
)
```

**Output:**

```text
name: Sonal
age: 21
course: AI/ML
```

Here:

```python
kwargs
```

is a dictionary.

---

# 🧩 8.22 `*args` and `**kwargs` Together

A method can accept both.

```python
class Demo:

    def show(self, *args, **kwargs):
        print("Positional:", args)
        print("Keyword:", kwargs)


demo = Demo()

demo.show(10, 20, 30, name="Sonal", course="Python")
```

**Output:**

```text
Positional: (10, 20, 30)
Keyword: {'name': 'Sonal', 'course': 'Python'}
```

This provides a highly flexible method interface.

---

# 🧠 8.23 Default Arguments vs `*args` vs `**kwargs`

| Feature | Default Arguments | `*args` | `**kwargs` |
|---|---|---|---|
| Number of arguments | Predefined flexible options | Variable | Variable |
| Argument type | Positional/keyword | Positional | Keyword |
| Stores data as | Individual variables | Tuple | Dictionary |
| Example | `x=10` | `*args` | `**kwargs` |
| Main use | Optional values | Many positional values | Many named values |

---

# 🛠️ 8.24 Practical Example — Flexible Calculator

```python
class Calculator:

    def calculate(self, operation, *args):
        if operation == "add":
            return sum(args)

        elif operation == "multiply":
            result = 1

            for value in args:
                result *= value

            return result

        else:
            raise ValueError("Unknown operation")


calculator = Calculator()

print(calculator.calculate("add", 10, 20, 30))
print(calculator.calculate("multiply", 2, 3, 4))
```

**Output:**

```text
60
24
```

The method supports a variable number of values.

---

# 🧬 8.25 Built-in Function Polymorphism

Python's built-in functions often work with different types of objects.

For example:

```python
print(len("Python"))
print(len([10, 20, 30]))
print(len((1, 2, 3, 4)))
```

**Output:**

```text
6
3
4
```

The same function:

```python
len()
```

works with:

- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Many custom objects that implement `__len__()`

This is polymorphism.

---

# 🔢 8.26 `+` Operator Polymorphism

The `+` operator behaves differently for different data types.

```python
print(10 + 20)
print("Hello " + "World")
print([1, 2] + [3, 4])
```

**Output:**

```text
30
Hello World
[1, 2, 3, 4]
```

The same operator:

```python
+
```

performs different operations depending on the operand types.

This is another example of polymorphism.

---

# 📏 8.27 `len()` with Custom Objects

We can make our own objects work with `len()` using `__len__()`.

```python
class Team:

    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


team = Team([
    "A",
    "B",
    "C",
    "D"
])

print(len(team))
```

**Output:**

```text
4
```

The built-in function:

```python
len()
```

works with our custom object because we implemented:

```python
__len__()
```

---

# 🧩 8.28 Polymorphism with Different Classes

Different unrelated classes can provide the same interface.

```python
class PDF:

    def open(self):
        print("Opening PDF file")


class Image:

    def open(self):
        print("Opening image")


class Video:

    def open(self):
        print("Opening video")


def open_file(file):
    file.open()


open_file(PDF())
open_file(Image())
open_file(Video())
```

**Output:**

```text
Opening PDF file
Opening image
Opening video
```

The function does not care about the exact class.

It only requires:

```python
open()
```

---

# 💻 8.29 Practical Example — File Processing

Polymorphism can make file-processing systems easier to extend.

```python
class CSVFile:

    def process(self):
        print("Processing CSV file")


class JSONFile:

    def process(self):
        print("Processing JSON file")


class XMLFile:

    def process(self):
        print("Processing XML file")


def process_file(file):
    file.process()


files = [
    CSVFile(),
    JSONFile(),
    XMLFile()
]

for file in files:
    process_file(file)
```

**Output:**

```text
Processing CSV file
Processing JSON file
Processing XML file
```

A new file type can be added without changing the main processing function, as long as it provides:

```python
process()
```

---

# 🤖 8.30 AI/ML Use Case — Different Models

Polymorphism is useful when working with different machine learning models.

```python
class LinearModel:

    def predict(self, data):
        print("Linear model prediction")


class DecisionTree:

    def predict(self, data):
        print("Decision tree prediction")


class NeuralNetwork:

    def predict(self, data):
        print("Neural network prediction")


def make_prediction(model, data):
    model.predict(data)


data = [1, 2, 3]

models = [
    LinearModel(),
    DecisionTree(),
    NeuralNetwork()
]

for model in models:
    make_prediction(model, data)
```

**Output:**

```text
Linear model prediction
Decision tree prediction
Neural network prediction
```

The prediction function works with any model that provides:

```python
predict()
```

This is a practical example of polymorphic design.

---

# 🧠 8.31 Polymorphism in Machine Learning Systems

A machine learning application may support:

```text
Linear Regression
        ↓
predict()

Decision Tree
        ↓
predict()

Random Forest
        ↓
predict()

Neural Network
        ↓
predict()
```

The surrounding application can simply call:

```python
model.predict(data)
```

without needing to know the internal implementation of every model.

This makes the system easier to extend.

---

# 🔄 8.32 Method Overriding vs Method Overloading

These concepts are different.

### Method Overriding

A child class provides a different implementation of an inherited method.

```python
class Parent:

    def show(self):
        print("Parent")


class Child(Parent):

    def show(self):
        print("Child")
```

### Method Overloading

Traditionally means multiple methods with the same name but different parameter lists.

Python does not support this traditional form directly.

Instead, Python commonly uses:

```python
default arguments
*args
**kwargs
```

---

# 📊 8.33 Method Overriding vs Method Overloading

| Feature | Method Overriding | Method Overloading |
|---|---|---|
| Usually involves inheritance | Yes | Not necessarily |
| Same method name | Yes | Yes |
| Different implementation | Yes | Usually different parameter lists |
| Python directly supports traditional form | Yes | No |
| Common Python alternative | `super()` | Default arguments, `*args`, `**kwargs` |

---

# 🧠 8.34 Compile-Time vs Runtime Polymorphism

In languages that strongly distinguish compile-time and runtime polymorphism:

- Method overloading is often associated with compile-time polymorphism.
- Method overriding is commonly associated with runtime polymorphism.

Python is dynamically typed and resolves method behavior at runtime.

For example:

```python
animal.sound()
```

The method that gets executed depends on the actual object.

This is commonly described as runtime polymorphic behavior.

---

# 🧩 8.35 Polymorphism with a Common Interface

A good polymorphic design often follows this structure:

```text
Common Interface
       ↓
 ┌─────┼─────┐
 ↓     ↓     ↓
Class A  Class B  Class C
 ↓       ↓       ↓
Behavior Behavior Behavior
```

For example:

```python
class Shape:

    def area(self):
        raise NotImplementedError
```

Different shapes can implement:

```python
area()
```

in their own way.

This idea becomes particularly important when learning **abstraction**.

---

# ⚠️ 8.36 Common Beginner Mistakes

## Mistake 1 — Confusing Overriding with Overloading

Remember:

```text
Overriding → Child changes inherited method
Overloading → Multiple signatures for same method
```

Python supports overriding directly but does not provide traditional method overloading in the same way as Java or C++.

---

## Mistake 2 — Defining the Same Method Twice

Incorrect:

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
```

The second method replaces the first.

Use default arguments or `*args` instead.

---

## Mistake 3 — Using `type()` Unnecessarily

A common beginner pattern is:

```python
if type(obj) == Dog:
    ...
elif type(obj) == Cat:
    ...
```

This often defeats the purpose of polymorphism.

Prefer:

```python
obj.sound()
```

when the objects provide a common interface.

---

## Mistake 4 — Forgetting the Required Method

Duck typing requires the expected behavior.

If a function does:

```python
obj.speak()
```

the object must provide:

```python
speak()
```

Otherwise, an error will occur.

---

## Mistake 5 — Making Every Class Completely Different

Polymorphism works best when classes share a meaningful interface.

For example:

```python
predict()
```

makes sense for different model classes.

But forcing unrelated classes to use the same method name without a meaningful relationship can make the design confusing.

---

# 🏆 8.37 Best Practices

1. Use common interfaces for related behaviors.
2. Prefer polymorphism over long chains of type-specific conditionals when appropriate.
3. Keep overridden methods semantically consistent with the parent interface.
4. Use `super()` when extending parent behavior.
5. Use default arguments for simple flexible parameter requirements.
6. Use `*args` when a method genuinely needs variable positional arguments.
7. Use `**kwargs` when variable keyword arguments are useful.
8. Take advantage of duck typing when appropriate.
9. Avoid unnecessary type checks.
10. Design methods around behavior rather than implementation details.
11. Keep polymorphic interfaces simple and predictable.
12. Use abstraction when a formal common interface is beneficial.

---

# ⭐ Key Points — Polymorphism

- Polymorphism means one interface can have multiple forms of behavior.
- Different objects can respond differently to the same method call.
- Method overriding is a major form of polymorphism.
- Child classes can override parent methods.
- `super()` can be used to extend parent behavior.
- Python supports duck typing.
- Duck typing focuses on what an object can do rather than its exact type.
- Python does not support traditional method overloading by defining multiple methods with the same name.
- Default arguments can provide flexible method calls.
- `*args` accepts variable positional arguments.
- `**kwargs` accepts variable keyword arguments.
- Built-in functions such as `len()` demonstrate polymorphism.
- Operators such as `+` also behave polymorphically.
- Polymorphism improves flexibility and extensibility.
- It is highly useful when different classes share a common interface.

---

# 📊 Quick Revision Table

| Concept | Meaning |
|---|---|
| Polymorphism | Same interface, different behavior |
| Method Overriding | Child class changes inherited method behavior |
| `super()` | Calls the next implementation in the MRO |
| Duck Typing | Focus on behavior rather than exact type |
| Method Overloading | Multiple signatures for the same method; traditional form is not directly supported in Python |
| Default Arguments | Provide optional parameter values |
| `*args` | Accept variable positional arguments |
| `**kwargs` | Accept variable keyword arguments |
| Built-in Polymorphism | Same built-in function works with different types |
| Operator Polymorphism | Same operator behaves differently for different types |

---

# 🧪 Complete Example — Polymorphism

```python
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


class Cow(Animal):

    def sound(self):
        print("Cow moos")


def make_sound(animal):
    animal.sound()


animals = [
    Dog(),
    Cat(),
    Cow()
]

for animal in animals:
    make_sound(animal)
```

**Output:**

```text
Dog barks
Cat meows
Cow moos
```

The function:

```python
make_sound()
```

does not need to know which specific animal it receives.

It simply calls:

```python
animal.sound()
```

Each object provides its own implementation.

---

# 🧪 Complete Example — Duck Typing

```python
class Dog:

    def speak(self):
        print("Dog barks")


class Robot:

    def speak(self):
        print("Robot speaks")


class Person:

    def speak(self):
        print("Person speaks")


def make_speak(obj):
    obj.speak()


objects = [
    Dog(),
    Robot(),
    Person()
]

for obj in objects:
    make_speak(obj)
```

**Output:**

```text
Dog barks
Robot speaks
Person speaks
```

The classes are unrelated, but they all provide:

```python
speak()
```

Therefore, the same function can work with all of them.

---

# 🧪 Complete Example — Flexible Method Using `*args`

```python
class Calculator:

    def add(self, *args):
        return sum(args)

    def multiply(self, *args):
        result = 1

        for value in args:
            result *= value

        return result


calculator = Calculator()

print(calculator.add(10))
print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))

print(calculator.multiply(2, 3))
print(calculator.multiply(2, 3, 4))
```

**Output:**

```text
10
30
60
6
24
```

This demonstrates how Python can provide flexible method behavior without traditional method overloading.

---

# 🚀 Summary

**Polymorphism** allows different objects to respond differently to the same interface or operation.

The central idea is:

```text
Same Interface
      ↓
Different Objects
      ↓
Different Behavior
```

A common example is:

```python
animal.sound()
```

where:

```text
Dog  → Bark
Cat  → Meow
Cow  → Moo
```

Method overriding provides polymorphism through inheritance, while duck typing allows polymorphic behavior even between unrelated classes.

Python does not support traditional method overloading by defining multiple methods with the same name and different signatures. Instead, flexible methods can be created using:

```python
default arguments
*args
**kwargs
```

Python's built-in functions and operators also demonstrate polymorphism:

```python
len()
+
==
```

The most important concepts to remember are:

```text
Polymorphism
    ↓
Same Interface
    ↓
Different Implementations
    ↓
Flexible Code
    ↓
Reusable and Extensible Design
```

Polymorphism is especially important in larger applications because it allows new classes and behaviors to be added without rewriting the code that uses the common interface.

It is widely useful in:

- Software architecture
- Payment systems
- File processing
- Web applications
- APIs
- Machine learning systems
- Data processing pipelines
- Plugin architectures

Understanding polymorphism provides the foundation for the next major OOP concept: **Abstraction**.

# 🎭 Part 8 — Abstraction

# 🎭 9. Abstraction

## 🧠 Basic Concept

**Abstraction** is the process of hiding unnecessary implementation details and exposing only the essential functionality to the user.

In simple words:

> **Abstraction means focusing on what an object does rather than how it does it.**

### Real-Life Example

When we use an ATM, we can:

```text
Withdraw money
Deposit money
Check balance
```

We do not need to know the internal implementation of:

```text
Bank servers
Database operations
Authentication systems
Transaction processing
```

The ATM provides a simple interface while hiding the complex implementation.

This is abstraction.

---

# 🎯 9.1 Why Do We Need Abstraction?

Abstraction helps us:

1. Hide unnecessary implementation details.
2. Expose only essential functionality.
3. Reduce complexity.
4. Make code easier to understand.
5. Create clear interfaces.
6. Improve maintainability.
7. Make large applications easier to design.
8. Enforce a common structure among related classes.

For example, different payment systems may all provide:

```python
pay()
```

but the internal implementation can be completely different.

---

# 🧩 9.2 Basic Example of Abstraction

Suppose we have different types of vehicles.

Every vehicle should be able to start, but the actual starting mechanism can be different.

```python
class Car:

    def start(self):
        print("Car starts with a key")


class ElectricCar:

    def start(self):
        print("Electric car starts with a button")


car = Car()
electric_car = ElectricCar()

car.start()
electric_car.start()
```

**Output:**

```text
Car starts with a key
Electric car starts with a button
```

The user only needs to know that the vehicle can:

```python
start()
```

The internal mechanism is different.

---

# 🏗️ 9.3 Abstract Classes

Python provides the `abc` module to create formal abstract classes.

The important components are:

```python
ABC
```

and:

```python
@abstractmethod
```

### Import

```python
from abc import ABC, abstractmethod
```

A class can inherit from:

```python
ABC
```

to become an abstract base class.

---

# 🧱 9.4 `ABC`

`ABC` stands for:

> **Abstract Base Class**

It is provided by Python's `abc` module.

### Basic Syntax

```python
from abc import ABC, abstractmethod


class ClassName(ABC):

    @abstractmethod
    def method_name(self):
        pass
```

An abstract class is used to define a common interface for its subclasses.

---

# 🔨 9.5 `@abstractmethod`

The `@abstractmethod` decorator marks a method as abstract.

An abstract method specifies that subclasses are expected to provide an implementation.

### Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Here:

```python
sound()
```

is an abstract method.

It defines what subclasses must provide.

---

# 🚫 9.6 Cannot Directly Instantiate an Abstract Class

Consider:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Trying:

```python
animal = Animal()
```

raises a `TypeError`.

Conceptually, Python reports that an abstract class with unimplemented abstract methods cannot be instantiated.

The reason is that `Animal` defines an incomplete interface.

A concrete subclass must implement the abstract method first.

---

# 🐶 9.7 Complete Abstract Class Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()
```

**Output:**

```text
Dog barks
```

Here:

```text
Animal
   ↓
Abstract Base Class
   ↓
sound()
   ↓
Dog
   ↓
Implements sound()
```

---

# 🧠 9.8 How Abstraction Works

The basic structure is:

```text
Abstract Class
      ↓
Defines Interface
      ↓
Abstract Methods
      ↓
Concrete Subclasses
      ↓
Provide Implementations
```

For example:

```python
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Different shapes can implement:

```python
area()
```

in different ways.

---

# 📐 9.9 Practical Example — Shapes

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rectangle = Rectangle(10, 5)
circle = Circle(5)

print("Rectangle Area:", rectangle.area())
print("Circle Area:", circle.area())
```

**Output:**

```text
Rectangle Area: 50
Circle Area: 78.5
```

Both classes must provide:

```python
area()
```

but their implementations are different.

---

# 🧩 9.10 Abstraction with Multiple Subclasses

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


shapes = [
    Rectangle(10, 5),
    Circle(5),
    Square(4)
]

for shape in shapes:
    print(shape.area())
```

**Output:**

```text
50
78.5
16
```

The loop does not need to know which specific shape it is processing.

It only relies on the abstract interface:

```python
area()
```

This combines **abstraction and polymorphism**.

---

# 🧠 9.11 Complete Working of an Abstract Class

Consider:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")
```

The process is:

```text
1. Animal inherits from ABC
          ↓
2. sound() is marked abstract
          ↓
3. Animal becomes abstract
          ↓
4. Dog inherits Animal
          ↓
5. Dog implements sound()
          ↓
6. Dog becomes concrete
          ↓
7. Dog object can be created
```

Therefore:

```python
dog = Dog()
```

is valid.

But:

```python
animal = Animal()
```

is not valid.

---

# ⚠️ 9.12 Rules of Abstract Classes

Important rules include:

1. An abstract class can be created using `ABC`.
2. Abstract methods are created using `@abstractmethod`.
3. A class with unimplemented abstract methods cannot normally be instantiated.
4. A concrete subclass must implement all inherited abstract methods before it can be instantiated.
5. An abstract class can contain normal methods as well as abstract methods.
6. An abstract class can contain attributes.
7. An abstract method does not necessarily have to contain `pass`; it can have an implementation too.
8. Abstract classes are useful for defining common interfaces.
9. Subclasses can provide different implementations of the same abstract method.
10. Abstraction works particularly well with polymorphism.

---

# 🧩 9.13 Abstract Class Can Have Normal Methods

An abstract class does not need to contain only abstract methods.

It can contain:

- Abstract methods
- Normal methods
- Class attributes
- Instance methods
- Constructors

### Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def display_name(self):
        print("Animal:", self.name)


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog("Bruno")

dog.display_name()
dog.sound()
```

**Output:**

```text
Animal: Bruno
Dog barks
```

The subclass inherits the normal method:

```python
display_name()
```

and implements the abstract method:

```python
sound()
```

---

# 🏗️ 9.14 Abstract Class with Constructor

An abstract class can have its own `__init__()` method.

```python
from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):

    def calculate_salary(self):
        return 50000


developer = Developer("Sonal")

print(developer.name)
print(developer.calculate_salary())
```

**Output:**

```text
Sonal
50000
```

The parent constructor initializes:

```python
self.name
```

while the child implements:

```python
calculate_salary()
```

---

# 🔄 9.15 Abstract Methods Can Have an Implementation

An abstract method can contain actual code.

For example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        print("Generic animal sound")
```

The method is still abstract because it has:

```python
@abstractmethod
```

A subclass must still implement it before the subclass can normally be instantiated.

The implementation can sometimes be reused explicitly using `super()`.

### Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()

dog.sound()
```

**Output:**

```text
Animal sound
Dog barks
```

This demonstrates that an abstract method may also contain reusable behavior.

---

# 🚫 9.16 Incomplete Subclass

If a subclass does not implement all abstract methods, it remains abstract.

### Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    pass
```

`Dog` has not implemented:

```python
sound()
```

Therefore:

```python
dog = Dog()
```

raises a `TypeError`.

---

# 🧬 9.17 Multilevel Abstract Inheritance

Abstract methods can remain abstract across multiple levels of inheritance.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Mammal(Animal):
    pass


class Dog(Mammal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()
```

**Output:**

```text
Dog barks
```

`Mammal` remains abstract because it does not implement `sound()`.

`Dog` becomes concrete because it implements the method.

---

# 🔢 9.18 Multiple Abstract Methods

An abstract class can define multiple abstract methods.

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


car = Car()

car.start()
car.stop()
```

**Output:**

```text
Car started
Car stopped
```

The subclass must implement both:

```python
start()
stop()
```

before it can normally be instantiated.

---

# 🚗 9.19 Practical Example — Vehicle System

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")


class Bike(Vehicle):

    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike engine stopped")


vehicles = [
    Car(),
    Bike()
]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()
```

**Output:**

```text
Car engine started
Car engine stopped
Bike engine started
Bike engine stopped
```

This example combines:

- Abstract class
- Abstract methods
- Inheritance
- Method overriding
- Polymorphism

---

# 🚫 9.20 `raise NotImplementedError`

Before using the `abc` module, developers often used:

```python
raise NotImplementedError
```

to indicate that a method was expected to be implemented by subclasses.

### Example

```python
class Animal:

    def sound(self):
        raise NotImplementedError("Subclasses must implement sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()
```

**Output:**

```text
Dog barks
```

If a subclass does not override `sound()`:

```python
class Cat(Animal):
    pass
```

then:

```python
cat = Cat()
cat.sound()
```

raises:

```text
NotImplementedError
```

---

# 🧠 9.21 `ABC` vs `NotImplementedError`

Both approaches can communicate that subclasses are expected to provide an implementation, but they work differently.

### Using `NotImplementedError`

```python
class Animal:

    def sound(self):
        raise NotImplementedError
```

The class can still normally be instantiated.

The error occurs when the unimplemented method is actually called.

### Using `ABC` and `@abstractmethod`

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

The abstract class itself cannot normally be instantiated while the abstract method remains unimplemented.

Therefore, `abc` provides a more formal mechanism for defining abstract interfaces.

---

# 📊 9.22 `ABC` vs `NotImplementedError`

| `ABC` + `@abstractmethod` | `NotImplementedError` |
|---|---|
| Formal abstract class mechanism | Manual implementation requirement |
| Prevents instantiation of incomplete subclasses | Error occurs when method is called |
| Provided by `abc` module | Built-in exception |
| Explicit interface contract | Informal contract |
| Useful for large class hierarchies | Useful for simple designs |
| Enforces implementation earlier | Enforcement happens during method execution |

---

# 🧩 9.23 Practical Example — Payment System

Abstraction is useful when multiple classes must follow the same interface.

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


payments = [
    CreditCardPayment(),
    UPIPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay(1000)
```

**Output:**

```text
Paid ₹1000 using Credit Card
Paid ₹1000 using UPI
Paid ₹1000 using Cash
```

The abstract class defines:

```python
pay()
```

while each subclass provides its own implementation.

---

# 🤖 9.24 AI/ML Use Case — Model Interface

Abstraction is highly useful when designing systems that support different machine learning models.

For example:

```python
from abc import ABC, abstractmethod


class MLModel(ABC):

    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass


class LinearRegressionModel(MLModel):

    def train(self, data):
        print("Training Linear Regression model")

    def predict(self, data):
        print("Making Linear Regression prediction")


class NeuralNetworkModel(MLModel):

    def train(self, data):
        print("Training Neural Network")

    def predict(self, data):
        print("Making Neural Network prediction")


models = [
    LinearRegressionModel(),
    NeuralNetworkModel()
]

for model in models:
    model.train([1, 2, 3])
    model.predict([4, 5])
```

**Output:**

```text
Training Linear Regression model
Making Linear Regression prediction
Training Neural Network
Making Neural Network prediction
```

The abstract class defines a common interface:

```python
train()
predict()
```

Each machine learning model implements these operations differently.

---

# 🧠 9.25 Why Abstraction Is Useful in AI/ML

An AI/ML application may support many models:

```text
Linear Regression
Decision Tree
Random Forest
SVM
Neural Network
Transformer
```

Instead of writing completely different code for each model, we can define a common interface:

```python
train()
predict()
```

Then the rest of the application can work with the abstract interface.

This makes it easier to:

- Add new models.
- Replace existing models.
- Test models.
- Build reusable pipelines.
- Maintain large ML systems.

---

# 🏗️ 9.26 Abstract Class with Class Method

An abstract class can also contain class methods.

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @classmethod
    def framework(cls):
        return "Python ML Framework"

    @abstractmethod
    def predict(self, data):
        pass


class ModelA(Model):

    def predict(self, data):
        print("Model A prediction")


print(ModelA.framework())

model = ModelA()
model.predict([1, 2, 3])
```

**Output:**

```text
Python ML Framework
Model A prediction
```

This demonstrates that abstract classes can contain different kinds of methods.

---

# 🧩 9.27 Abstract Properties

The `abc` module can also be used with properties.

For example:

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

print(rectangle.area)
```

**Output:**

```text
50
```

This creates an abstract property that subclasses are expected to implement.

---

# 🧠 9.28 Abstraction with Properties

The pattern:

```python
@property
@abstractmethod
def area(self):
    pass
```

means that subclasses must provide a property named:

```python
area
```

rather than an ordinary method.

This is useful when the value should be accessed like:

```python
shape.area
```

instead of:

```python
shape.area()
```

---

# 🔐 9.29 Abstraction vs Encapsulation

These two concepts are often confused.

### Encapsulation

Encapsulation focuses on:

```text
Bundling data and methods
+
Controlling access to internal state
```

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
```

The focus is on controlling the object's internal state.

### Abstraction

Abstraction focuses on:

```text
Defining essential behavior
+
Hiding unnecessary implementation details
```

Example:

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

The focus is on defining what a payment system must do.

---

# 📊 9.30 Abstraction vs Encapsulation

| Abstraction | Encapsulation |
|---|---|
| Hides unnecessary complexity | Controls access to internal data |
| Focuses on essential behavior | Focuses on data and implementation protection |
| Defines interfaces | Bundles data and methods |
| Uses `ABC` and `@abstractmethod` | Uses properties, naming conventions, methods |
| Answers "What should this object do?" | Answers "How should its internal state be accessed?" |
| Helps reduce conceptual complexity | Helps protect and manage object state |

Both concepts often work together.

---

# 🤝 9.31 Abstraction + Encapsulation

A class can use both concepts at the same time.

```python
from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount


account = SavingsAccount(5000)

print(account.balance)

account.withdraw(1000)

print(account.balance)
```

**Output:**

```text
5000
4000
```

Here:

### Abstraction

```python
@abstractmethod
def withdraw(self, amount):
    pass
```

defines what the subclass must provide.

### Encapsulation

```python
self._balance
```

and:

```python
@property
def balance(self):
    return self._balance
```

control access to the internal balance.

---

# ⚠️ 9.32 Common Beginner Mistakes

## Mistake 1 — Forgetting `ABC`

Incorrect:

```python
class Animal:

    @abstractmethod
    def sound(self):
        pass
```

Correct:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## Mistake 2 — Forgetting `@abstractmethod`

Incorrect:

```python
class Animal(ABC):

    def sound(self):
        pass
```

This is simply a normal method.

Correct:

```python
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## Mistake 3 — Instantiating an Abstract Class

Incorrect:

```python
animal = Animal()
```

if `Animal` still has unimplemented abstract methods.

A concrete subclass should implement the required methods first.

---

## Mistake 4 — Not Implementing All Abstract Methods

If:

```python
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
```

then a concrete subclass must implement both:

```python
sound()
move()
```

---

## Mistake 5 — Confusing Abstraction with Encapsulation

Remember:

```text
Abstraction
→ Hides unnecessary complexity
→ Defines essential behavior

Encapsulation
→ Controls access to internal state
→ Bundles data and methods
```

---

# 🏆 9.33 Best Practices

1. Use abstract classes when several classes should follow a common interface.
2. Use `ABC` and `@abstractmethod` for formal abstraction.
3. Keep abstract interfaces simple and meaningful.
4. Give abstract methods clear names.
5. Implement all required abstract methods in concrete subclasses.
6. Use normal methods in abstract classes when common behavior can be shared.
7. Use `super()` when an abstract method provides reusable implementation.
8. Use `NotImplementedError` when a formal ABC is unnecessary but subclasses still need to implement a method.
9. Combine abstraction with polymorphism for flexible designs.
10. Use abstraction to reduce unnecessary complexity.
11. Do not create abstract classes without a meaningful reason.
12. Keep the public interface focused on essential behavior.

---

# ⭐ Key Points — Abstraction

- Abstraction hides unnecessary implementation details.
- It focuses on what an object does rather than how it does it.
- Python provides the `abc` module for formal abstraction.
- `ABC` means Abstract Base Class.
- `@abstractmethod` marks a method as abstract.
- Abstract classes cannot normally be instantiated while abstract methods remain unimplemented.
- Concrete subclasses must implement inherited abstract methods.
- Abstract classes can contain both abstract and normal methods.
- Abstract classes can have constructors and attributes.
- Abstract methods can contain implementations.
- `raise NotImplementedError` is another way to indicate required subclass behavior.
- `ABC` provides a more formal interface contract.
- Abstraction works closely with polymorphism.
- Abstract properties can also be created.
- Abstraction and encapsulation are related but different concepts.
- Abstraction is especially useful in large and extensible software systems.

---

# 📊 Quick Revision Table

| Concept | Description |
|---|---|
| Abstraction | Hides unnecessary implementation details |
| `abc` | Python module for abstract base classes |
| `ABC` | Base class used to create abstract classes |
| `@abstractmethod` | Marks a method as abstract |
| Abstract Class | Class defining an incomplete/common interface |
| Concrete Class | Class that implements required abstract behavior |
| Abstract Method | Method subclasses are expected to implement |
| `NotImplementedError` | Exception used to indicate missing implementation |
| Abstract Property | Property that subclasses must implement |
| Encapsulation | Controls access to internal state |
| Polymorphism | Allows common interfaces to have different implementations |

---

# 🧪 Complete Example — Abstract ML Model

```python
from abc import ABC, abstractmethod


class MLModel(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass

    def display_name(self):
        print("Model:", self.name)


class LinearRegression(MLModel):

    def train(self, data):
        print("Training Linear Regression")

    def predict(self, data):
        print("Predicting using Linear Regression")


class NeuralNetwork(MLModel):

    def train(self, data):
        print("Training Neural Network")

    def predict(self, data):
        print("Predicting using Neural Network")


models = [
    LinearRegression("Linear Regression"),
    NeuralNetwork("Neural Network")
]

for model in models:
    model.display_name()
    model.train([1, 2, 3])
    model.predict([4, 5])
    print()
```

**Output:**

```text
Model: Linear Regression
Training Linear Regression
Predicting using Linear Regression

Model: Neural Network
Training Neural Network
Predicting using Neural Network
```

This complete example demonstrates:

- `ABC`
- `@abstractmethod`
- Abstract class
- Concrete subclasses
- Constructor in abstract class
- Normal method in abstract class
- Method overriding
- Polymorphism
- AI/ML-oriented design

---

# 🚀 Summary

**Abstraction** allows us to define what an object should do without requiring users of the object to understand every implementation detail.

Python provides formal abstraction through:

```python
from abc import ABC, abstractmethod
```

A typical abstract class looks like:

```python
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

A concrete subclass then implements the required behavior:

```python
class Dog(Animal):

    def sound(self):
        print("Dog barks")
```

The fundamental structure is:

```text
Abstract Base Class
        ↓
Defines Interface
        ↓
Abstract Methods
        ↓
Concrete Subclasses
        ↓
Different Implementations
        ↓
Polymorphic Behavior
```

Another approach is:

```python
raise NotImplementedError
```

which communicates that subclasses are expected to provide an implementation, but it does not provide the same formal instantiation-time enforcement as `@abstractmethod`.

The most important difference to remember is:

```text
Abstraction
    ↓
What should the object do?

Encapsulation
    ↓
How should internal data be accessed and protected?
```

Abstraction becomes extremely useful when designing systems with multiple interchangeable implementations, such as:

- Payment systems
- File processors
- Database interfaces
- APIs
- Machine learning models
- Data processing pipelines
- Plugin systems
- Large software architectures

A strong understanding of abstraction completes another major pillar of Object-Oriented Programming and prepares the foundation for the final Chapter 11 topic: **Composition**.

# 🧩 Part 9 — Composition

# 🧩 10. Composition

## 🎯 Objective

Composition is an important Object-Oriented Programming concept in which one class **contains an object of another class** and uses that object to perform its work.

By the end of this section, you will understand:

- What composition means
- How composition works
- How to create objects inside another class
- The **HAS-A** relationship
- Composition vs Inheritance
- When composition is preferred
- Practical real-world examples
- Composition in AI/ML systems
- Best practices and common mistakes

---

# 📌 10.1 Basic Concept

## 🔹 What is Composition?

**Composition** is an OOP technique where a class contains an object of another class as one of its attributes.

In simple words:

> **One class is made up of objects of other classes.**

Composition represents a **HAS-A relationship**.

### Example

A `Car` has an `Engine`.

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start()
```

### Output

```text
Engine started
Car started
```

Here:

```python
self.engine = Engine()
```

means that the `Car` object contains an `Engine` object.

Therefore:

```text
Car HAS-A Engine
```

---

# 📌 10.2 HAS-A Relationship

Composition represents a **HAS-A relationship**.

### Examples

| Class | Contains | Relationship |
|---|---|---|
| Car | Engine | Car HAS-A Engine |
| Computer | CPU | Computer HAS-A CPU |
| House | Room | House HAS-A Room |
| Library | Books | Library HAS-A Books |
| Student | Address | Student HAS-A Address |
| NeuralNetwork | Layers | NeuralNetwork HAS-A Layers |
| MLModel | Preprocessor | MLModel HAS-A Preprocessor |

---

# 📌 10.3 Composition vs Inheritance Relationship

Inheritance represents:

```text
IS-A
```

Composition represents:

```text
HAS-A
```

### Example of Inheritance

```python
class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    pass
```

Here:

```text
Dog IS-A Animal
```

because `Dog` inherits from `Animal`.

### Example of Composition

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()
```

Here:

```text
Car HAS-A Engine
```

because `Car` contains an `Engine` object.

---

# 📌 10.4 Basic Working of Composition

The basic structure of composition is:

```python
class Component:
    def some_method(self):
        print("Component method")


class MainClass:
    def __init__(self):
        self.component = Component()

    def use_component(self):
        self.component.some_method()


obj = MainClass()
obj.use_component()
```

### How it works

First, the component class is created:

```python
class Component:
    ...
```

Then the main class creates an object of the component:

```python
self.component = Component()
```

Now the main class can use the component:

```python
self.component.some_method()
```

---

# 📌 10.5 Composition with Constructor Arguments

The contained object can also receive data through its constructor.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def show_power(self):
        print(f"Power: {self.horsepower} HP")


class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)

    def show_details(self):
        print(f"Brand: {self.brand}")
        self.engine.show_power()


car = Car("Toyota", 150)

car.show_details()
```

### Output

```text
Brand: Toyota
Power: 150 HP
```

The `Car` class is responsible for creating and using its `Engine`.

---

# 📌 10.6 Composition Using an Existing Object

Composition does not always require creating the component object inside the constructor.

We can also pass an existing object.

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


engine = Engine()

car = Car(engine)

car.start()
```

### Output

```text
Engine started
```

This approach is useful because the component can be created separately and injected into another class.

---

# 📌 10.7 Composition and Object Collaboration

Composition allows different objects to **work together**.

For example:

```python
class Engine:
    def start(self):
        print("Engine started")


class MusicSystem:
    def play_music(self):
        print("Playing music")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.music_system = MusicSystem()

    def drive(self):
        self.engine.start()
        self.music_system.play_music()
        print("Car is driving")


car = Car()

car.drive()
```

### Output

```text
Engine started
Playing music
Car is driving
```

The `Car` does not implement engine functionality or music functionality itself.

Instead, it **delegates** these responsibilities to its contained objects.

---

# 📌 10.8 Composition Promotes Separation of Responsibilities

Composition is useful because different classes can have different responsibilities.

For example:

```python
class Engine:
    def start(self):
        print("Starting engine")


class GPS:
    def navigate(self):
        print("Navigating route")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.gps = GPS()

    def drive(self):
        self.engine.start()
        self.gps.navigate()
        print("Driving")
```

Here:

- `Engine` handles engine-related functionality
- `GPS` handles navigation
- `Car` coordinates these components

This follows the idea of **separation of responsibilities**.

---

# 📌 10.9 Composition vs Inheritance

Composition and inheritance solve different design problems.

## 🔹 Inheritance

Inheritance is useful when there is a genuine:

```text
IS-A
```

relationship.

Example:

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")
```

Relationship:

```text
Dog IS-A Animal
```

---

## 🔹 Composition

Composition is useful when there is a:

```text
HAS-A
```

relationship.

Example:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()
```

Relationship:

```text
Car HAS-A Engine
```

---

# 📊 Composition vs Inheritance

| Feature | Inheritance | Composition |
|---|---|---|
| Relationship | IS-A | HAS-A |
| Main idea | Extend another class | Contain another object |
| Reuse mechanism | Inherited behavior | Delegated behavior |
| Coupling | Usually tighter | Usually more flexible |
| Flexibility | Can be less flexible | Usually more flexible |
| Best for | Genuine subtype relationships | Building objects from components |
| Example | Dog → Animal | Car → Engine |

---

# 📌 10.10 Why Prefer Composition?

A common software-design principle is:

> **Prefer composition over inheritance when inheritance does not represent a true IS-A relationship.**

Composition often provides more flexibility because components can be replaced independently.

For example:

```python
class PetrolEngine:
    def start(self):
        print("Petrol engine started")


class ElectricEngine:
    def start(self):
        print("Electric engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

Now we can use different engines:

```python
petrol_car = Car(PetrolEngine())
electric_car = Car(ElectricEngine())

petrol_car.start()
electric_car.start()
```

### Output

```text
Petrol engine started
Electric engine started
```

The `Car` class does not need to change.

This makes the design more flexible.

---

# 📌 10.11 Composition Allows Components to Be Replaced

One of the major advantages of composition is that components can often be changed without modifying the main class.

```python
class EmailNotification:
    def send(self):
        print("Sending email")


class SMSNotification:
    def send(self):
        print("Sending SMS")


class UserService:
    def __init__(self, notification):
        self.notification = notification

    def notify_user(self):
        self.notification.send()
```

Now:

```python
email_service = UserService(EmailNotification())
sms_service = UserService(SMSNotification())

email_service.notify_user()
sms_service.notify_user()
```

### Output

```text
Sending email
Sending SMS
```

The `UserService` works with different notification systems.

---

# 📌 10.12 Practical Example — Computer System

A computer can be represented using composition.

```python
class CPU:
    def process(self):
        print("CPU is processing")


class RAM:
    def load(self):
        print("RAM is loading data")


class Storage:
    def read(self):
        print("Reading data from storage")


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.storage = Storage()

    def run(self):
        self.storage.read()
        self.ram.load()
        self.cpu.process()
        print("Computer is running")


computer = Computer()

computer.run()
```

### Output

```text
Reading data from storage
RAM is loading data
CPU is processing
Computer is running
```

### Relationship

```text
Computer
    ├── CPU
    ├── RAM
    └── Storage
```

This is a good example of composition because a computer is **built using multiple components**.

---

# 📌 10.13 Practical Example — Library System

```python
class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(self.title)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display()


book1 = Book("Python")
book2 = Book("Machine Learning")
book3 = Book("Data Structures")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()
```

### Output

```text
Python
Machine Learning
Data Structures
```

Here:

```text
Library HAS-A collection of Books
```

The `Library` object works with multiple `Book` objects.

---

# 📌 10.14 Practical Example — AI Engineer Use Case

Composition is extremely useful in AI/ML software because complex systems are often built from smaller components.

For example, an ML pipeline may contain:

```text
MLPipeline
    ├── DataLoader
    ├── Preprocessor
    ├── Model
    └── Evaluator
```

Each component has a separate responsibility.

```python
class DataLoader:
    def load(self):
        print("Loading dataset")


class Preprocessor:
    def preprocess(self):
        print("Preprocessing data")


class Model:
    def train(self):
        print("Training model")

    def predict(self):
        print("Making predictions")


class Evaluator:
    def evaluate(self):
        print("Evaluating model")


class MLPipeline:
    def __init__(self):
        self.data_loader = DataLoader()
        self.preprocessor = Preprocessor()
        self.model = Model()
        self.evaluator = Evaluator()

    def run(self):
        self.data_loader.load()
        self.preprocessor.preprocess()
        self.model.train()
        self.evaluator.evaluate()


pipeline = MLPipeline()

pipeline.run()
```

### Output

```text
Loading dataset
Preprocessing data
Training model
Evaluating model
```

### Structure

```text
MLPipeline
│
├── DataLoader
├── Preprocessor
├── Model
└── Evaluator
```

This is a practical example of how AI/ML systems can be designed using composition.

---

# 📌 10.15 AI Engineer Use Case — Flexible ML Pipeline

Composition becomes even more useful when components can be replaced.

```python
class StandardPreprocessor:
    def process(self, data):
        print("Standard preprocessing")


class ImagePreprocessor:
    def process(self, data):
        print("Image preprocessing")


class Pipeline:
    def __init__(self, preprocessor):
        self.preprocessor = preprocessor

    def run(self, data):
        self.preprocessor.process(data)


pipeline1 = Pipeline(StandardPreprocessor())
pipeline2 = Pipeline(ImagePreprocessor())

pipeline1.run("data")
pipeline2.run("image data")
```

### Output

```text
Standard preprocessing
Image preprocessing
```

The `Pipeline` does not need to know the internal implementation of the preprocessing component.

It only needs an object that provides the required behavior.

---

# 📌 10.16 Composition and Dependency Injection

When an object is passed into another object instead of being created internally, this is commonly associated with **dependency injection**.

Example:

```python
class Model:
    def predict(self):
        print("Making prediction")


class Predictor:
    def __init__(self, model):
        self.model = model

    def run(self):
        self.model.predict()


model = Model()

predictor = Predictor(model)

predictor.run()
```

Here:

```python
Predictor(model)
```

receives its dependency from outside.

This makes the code easier to test and replace.

---

# 📌 10.17 Composition vs Simple Attribute

Not every attribute necessarily represents meaningful composition.

For example:

```python
class Student:
    def __init__(self):
        self.name = "Sonal"
        self.age = 21
```

Here:

```python
self.name
self.age
```

are simple data attributes.

Composition usually involves one object containing **another object or collection of objects with their own behavior**.

Example:

```python
class Address:
    def show(self):
        print("Lucknow")


class Student:
    def __init__(self):
        self.address = Address()
```

Here:

```text
Student HAS-A Address
```

and `Address` has its own behavior.

---

# 📌 10.18 Composition and Object Lifetime

In typical composition designs, the containing object manages the component as part of its internal structure.

Example:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()
```

When a `Car` object is created, it creates its `Engine` component.

```python
car = Car()
```

The engine is part of the car's internal structure.

However, Python's object lifetime is governed by **references and garbage collection**, so composition should not be understood as a strict ownership/deletion rule in every case.

---

# 📌 10.19 Composition with Lists

Composition can also be used with multiple objects.

```python
class Employee:
    def __init__(self, name):
        self.name = name


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        for employee in self.employees:
            print(employee.name)


company = Company()

company.add_employee(Employee("Aman"))
company.add_employee(Employee("Riya"))
company.add_employee(Employee("Sonal"))

company.show_employees()
```

### Output

```text
Aman
Riya
Sonal
```

Relationship:

```text
Company HAS-A collection of Employees
```

---

# 📌 10.20 Composition with Other OOP Concepts

Composition can work together with many OOP concepts.

For example:

### Composition + Encapsulation

```python
class Engine:
    def __init__(self):
        self.__status = "Off"

    def start(self):
        self.__status = "On"

    def get_status(self):
        return self.__status


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def status(self):
        return self.engine.get_status()
```

Here:

- `Engine` encapsulates its internal state
- `Car` contains an `Engine`
- `Car` uses the public interface of `Engine`

---

# 📌 10.21 Composition + Polymorphism

Composition can also work with polymorphism.

```python
class CSVLoader:
    def load(self):
        print("Loading CSV data")


class JSONLoader:
    def load(self):
        print("Loading JSON data")


class DataPipeline:
    def __init__(self, loader):
        self.loader = loader

    def run(self):
        self.loader.load()


csv_pipeline = DataPipeline(CSVLoader())
json_pipeline = DataPipeline(JSONLoader())

csv_pipeline.run()
json_pipeline.run()
```

### Output

```text
Loading CSV data
Loading JSON data
```

The pipeline works with different loader objects.

---

# 📌 10.22 Composition + Abstraction

Composition can also use abstract classes.

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass


class LinearModel(Model):
    def predict(self, data):
        print("Linear model prediction")


class Predictor:
    def __init__(self, model):
        self.model = model

    def run(self, data):
        self.model.predict(data)


predictor = Predictor(LinearModel())

predictor.run([1, 2, 3])
```

### Output

```text
Linear model prediction
```

Here:

```text
Predictor HAS-A Model
```

and the model follows an abstract interface.

---

# 📌 10.23 Composition vs Inheritance — Practical Decision

When designing a class, ask:

### Question 1

Is the relationship truly:

```text
IS-A
```

If yes, inheritance may be appropriate.

Example:

```text
Dog IS-A Animal
```

---

### Question 2

Is the relationship:

```text
HAS-A
```

If yes, composition is usually more natural.

Example:

```text
Car HAS-A Engine
```

---

### Question 3

Do I only want to reuse some functionality?

Consider composition instead of forcing an inheritance relationship.

---

### Question 4

Could the component need to change independently?

If yes, composition can provide better flexibility.

---

# 📌 10.24 Advantages of Composition

### 1. Better Flexibility

Components can often be replaced independently.

### 2. Loose Coupling

Classes can interact through clearly defined interfaces.

### 3. Reusability

The same component can be used by different classes.

### 4. Easier Testing

Components can be replaced with test or mock objects.

### 5. Better Separation of Responsibilities

Each class can focus on a specific task.

### 6. Easier Maintenance

Changes to one component may not require changes to unrelated classes.

### 7. Supports Complex Systems

Large systems can be constructed from smaller components.

---

# 📌 10.25 Common Beginner Mistakes

## ❌ Mistake 1 — Confusing IS-A and HAS-A

Incorrect reasoning:

```text
Car inherits Engine
```

A car is not an engine.

Correct:

```text
Car HAS-A Engine
```

---

## ❌ Mistake 2 — Creating Unnecessary Inheritance

Do not use inheritance only because it allows code reuse.

Instead, ask whether the child is genuinely a specialized form of the parent.

---

## ❌ Mistake 3 — Accessing Internal Details

Avoid tightly coupling the containing class to the internal implementation of the component.

Prefer:

```python
self.engine.start()
```

instead of directly modifying internal engine state.

---

## ❌ Mistake 4 — Making One Class Responsible for Everything

Avoid creating a huge class containing every possible behavior.

Instead, divide responsibilities among smaller classes.

---

## ❌ Mistake 5 — Overengineering

Composition is useful, but not every two related values need separate classes.

Use it when separate objects provide meaningful behavior or responsibility.

---

# 📌 10.26 Best Practices

### ✅ 1. Use Composition for HAS-A Relationships

Example:

```text
Car HAS-A Engine
```

### ✅ 2. Keep Components Focused

Each class should have a clear responsibility.

### ✅ 3. Depend on Interfaces or Expected Behavior

The main class should care about what a component can do rather than unnecessary implementation details.

### ✅ 4. Use Dependency Injection When Useful

Pass dependencies into constructors when you want flexibility and testability.

```python
class Service:
    def __init__(self, dependency):
        self.dependency = dependency
```

### ✅ 5. Avoid Deep Inheritance Hierarchies

Composition can often provide a simpler alternative.

### ✅ 6. Keep Classes Small and Reusable

Small components are easier to understand, test, and reuse.

---

# ⭐ Key Points

- Composition means **one class contains another object**.
- Composition represents a **HAS-A relationship**.
- Inheritance generally represents an **IS-A relationship**.
- Composition allows objects to collaborate.
- Components can often be replaced independently.
- Composition encourages separation of responsibilities.
- Dependency injection can be used with composition.
- Composition is highly useful for building complex systems.
- AI/ML pipelines can be designed using composition.
- Composition can work together with encapsulation, polymorphism, and abstraction.
- Prefer composition when inheritance does not represent a genuine subtype relationship.

---

# 📊 Quick Revision Table

| Concept | Meaning | Example |
|---|---|---|
| Composition | Object contains another object | Car HAS-A Engine |
| HAS-A | Contains/uses relationship | Computer HAS-A CPU |
| Inheritance | Child extends parent | Dog IS-A Animal |
| Dependency Injection | Dependency passed from outside | `Service(dep)` |
| Delegation | Object forwards work to another object | `self.engine.start()` |
| Loose Coupling | Components depend less on implementation details | Replaceable components |
| AI/ML Pipeline | System built from ML components | Pipeline HAS-A Model |

---

# 🧠 Complete Composition Example

The following example combines several ideas from this section.

```python
class DataLoader:
    def load(self):
        print("Loading data")


class Preprocessor:
    def process(self):
        print("Preprocessing data")


class Model:
    def train(self):
        print("Training model")

    def predict(self):
        print("Making prediction")


class Evaluator:
    def evaluate(self):
        print("Evaluating model")


class MLPipeline:
    def __init__(self, loader, preprocessor, model, evaluator):
        self.loader = loader
        self.preprocessor = preprocessor
        self.model = model
        self.evaluator = evaluator

    def train_pipeline(self):
        self.loader.load()
        self.preprocessor.process()
        self.model.train()
        self.evaluator.evaluate()

    def predict(self):
        self.model.predict()


loader = DataLoader()
preprocessor = Preprocessor()
model = Model()
evaluator = Evaluator()

pipeline = MLPipeline(
    loader,
    preprocessor,
    model,
    evaluator
)

pipeline.train_pipeline()
pipeline.predict()
```

### Output

```text
Loading data
Preprocessing data
Training model
Evaluating model
Making prediction
```

### Structure

```text
MLPipeline
│
├── DataLoader
├── Preprocessor
├── Model
└── Evaluator
```

This is a strong example of composition because the complete system is **built by combining independent objects**.

---

# 🚀 Chapter 11 — Final OOP Advanced Summary

After completing Chapter 11, you have covered the major advanced OOP concepts in Python:

```text
Inheritance
     ↓
super()
     ↓
MRO
     ↓
@classmethod
     ↓
Property Decorators
     ↓
Operator Overloading
     ↓
Encapsulation
     ↓
Polymorphism
     ↓
Abstraction
     ↓
Composition
```

## 🔹 Inheritance

Allows a class to reuse and extend another class.

```text
IS-A
```

---

## 🔹 `super()`

Allows cooperative access to the next implementation according to the MRO.

---

## 🔹 MRO

Defines the order in which Python searches for methods and attributes.

---

## 🔹 `@classmethod`

Works with the class itself using:

```python
cls
```

and is useful for class-level operations and alternative constructors.

---

## 🔹 Property Decorators

Allow controlled access to attributes using:

```python
@property
@attribute.setter
@attribute.deleter
```

---

## 🔹 Operator Overloading

Allows custom objects to work naturally with operators such as:

```python
+
-
*
==
<
>
```

using special methods.

---

## 🔹 Encapsulation

Keeps data and implementation details controlled within a class.

---

## 🔹 Polymorphism

Allows different objects to be used through a common interface or expected behavior.

---

## 🔹 Abstraction

Defines what a class should provide while hiding unnecessary implementation details.

---

## 🔹 Composition

Builds complex objects by combining smaller objects.

```text
HAS-A
```

---

# 🏆 Final OOP Relationship Cheat Sheet

| Concept | Main Idea | Relationship / Purpose |
|---|---|---|
| Inheritance | Reuse and extend a class | IS-A |
| `super()` | Cooperative parent/MRO access | Method delegation |
| MRO | Method lookup order | Search order |
| `@classmethod` | Operates on class | Uses `cls` |
| Property | Controlled attribute access | Getter/Setter/Deleter |
| Operator Overloading | Customize operators | Object behavior |
| Encapsulation | Protect/control implementation | Data hiding |
| Polymorphism | Same interface, different behavior | Many forms |
| Abstraction | Define required behavior | Hide complexity |
| Composition | Build objects from components | HAS-A |

---

# 🚀 Chapter 11 Complete

You have now completed the **OOP Advanced** concepts required for this chapter.

The most important thing is not memorizing every syntax, but understanding how these concepts work together when designing real Python applications.

A well-designed Python application may combine:

```text
Inheritance
      +
Encapsulation
      +
Polymorphism
      +
Abstraction
      +
Composition
```

These concepts become especially useful when building larger projects, APIs, data-processing systems, and AI/ML applications.

---

# 📚 Course Information

**Course:** CodeWithHarry — Python Programming  
**Chapter:** 11  
**Topic:** OOP Advanced  
**Language:** Python

---

# 👨‍💻 Author

**Sonal Rai**