#1- import the randome module
import random


#2 - creates subjects list 
subjects = ["The cat", 
            "A dog",
              "The president",
                "A scientist",
                  "The teacher"]
#3 - verbs lists
verbs = ["jumps over", 
          "runs to", 
            "discovers", 
              "teaches", 
                "writes about"]
#4 - objects lists
objects = ["a fence", 
            "the moon", 
              "a new species", 
                "the students", 
                  "a book"]
#5 - functions to generate headline
def generate_headline():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)
    headline = f"{subject} {verb} {object}."
    return headline
#6- print the generated headline 
print(generate_headline())

