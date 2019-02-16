"""
 * An animal shelter holds only dogs and cats, and operates on a strictly
 * "first in, first out" basis. People must adopt either the "oldest"
 * (based on arrival time) of all animals at the shelter, or they can
 * select whether they would prefer a dog or a cat (and will receive
 * the oldest animal of that type). They cannot select which specific
 * animal they would like. Create the data structures to maintain this
 * system and implement operations such as enqueue, dequeueAny, dequeueDog
 * and dequeueCat.You may use the built-in LinkedList data structure.
"""
import time
class animalshelter(object):
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, pet):
        if isinstance(pet, dog):
            self.dogs.append([pet.name, pet.time])
        elif isinstance(pet, cat):
            self.cats.append([pet.name, pet.time])
        else:
            raise ValueError("Invalid Pet Type")

    def dequeueany(self):
        if not self.dogs and not self.cats:
            raise ValueError("No pets to adopt")
        elif not self.dogs:
            return self.catdequeue()
        elif not self.cats:
            return self.dogdequeue()
        else:
            firstcattime = self.cats[0][1]
            firstdogtime = self.dogs[0][1]
            if firstdogtime < firstcattime:
                return self.dogdequeue()
            else:
                return self.catdequeue()

    def dogdequeue(self):
        if not self.dogs:
            raise IndexError("No dogs to adopt!")
        else:
            return self.dogs.pop(0)

    def catdequeue(self):
        if not self.cats:
            raise IndexError("No cats to adopt!")
        else:
            return self.cats.pop(0)


class animal(object):
    def __init__(self, name=None):
        self.name = name
        self.time = "%12.9f" % time.time()

class dog(animal):
    def __init__(self, name=None):
        animal.__init__(self, name)

class cat(animal):
    def __init__(self, name=None):
        animal.__init__(self, name)


dog0 = dog("burrow")
cat0 = cat("kitty")
dog1 = dog("tom")
cat1 = cat("jerry")
dog2 = dog("jim")
cat2 = cat("meow")
dog3 = dog("colorful")
anim = animalshelter()
anim.enqueue(dog0)
anim.enqueue(cat0)
anim.enqueue(dog1)
anim.enqueue(cat1)
anim.enqueue(dog2)
anim.enqueue(cat2)
anim.enqueue(dog3)
print(anim.dogdequeue()[0])
print(anim.dequeueany()[0])
print(anim.dogdequeue()[0])
print(anim.catdequeue()[0])
print(anim.dequeueany()[0])
print(anim.catdequeue()[0])
print(anim.dogdequeue()[0])
