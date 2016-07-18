"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   - Abstraction: We are hiding the processes that we don't need to see. 
   We can manipulate things while not really needing to know what is happening
   under the hood.

   - Encapsulation: We want to keep functions that affect an object close
   to the data for that object - basically keep everything that it means
   to be a certain object together with that object.

   - Polymorphism: Flexibility of types of objects without using 
   conditionals (a bunch of if, elif statements). 

2. What is a class?

    - A class is a type of a thing. Like how a cat is a type of animal. Classes 
    also are like using smarter dictionaries. You can keep the data that affects
    an object close to that object.

3. What is an instance attribute?

    - An instance attribute is a characteristic that only affects or belongs
    to a certain instance within a class and not the entire class itself.

4. What is a method?
    
    - A method is similar to a function, but it is called on a class.

5. What is an instance in object orientation?

    - An instance is an individual thing within a class. So a cat is a type of animal,
    but within the Cat class, there can be any number of individual instances, like
    a cat named Fluffy, and another cat named Pickles. Each individual cat inside
    the class is an instance.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   - A class attribute is a characteristic that affects or belongs to an entire
   class. An instance attribute is a characteristic that only affects an instance
   within that class. So a class attribute for the Cat class, could be "hungry = True" -
   all cats are hungry and need to eat. But an instance attribute would be the amount
   of hunger for each cat. Not all the cats in our class eat the same amount, each
   instance can have a different hunger level.


"""


# Parts 2 through 5:
# Create your classes and class methods


""" Part 2 """

class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

Jasmine = Student("Jasmine", "Debugger", "0101 Computer Street")
Jaqui = Student("Jaqui", "Console", "888 Binary Ave")



class Question(object):

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate():
        raw_input("")

capital = Question("What is the capital of Alberta?", "Edmonton")
author = Question("Who is the author of Python?", "Guido Van Rossum")



""" Part 3 """

class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []


    def add_question(self, question, correct_answer):
        return self.questions.append(question)



""" Hey Ally - this is as far as I was able to get. I got super confused
and frustrated once Part 3 began. I couldn't figure out how to make the 
Exam and Question classes work together, and then I couldn't continue without
making those work. I'd definitely like to discuss this assessment in our
advising this week. Thanks."""        

















