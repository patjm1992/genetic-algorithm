
import random
import string
import sys
import timeit
from time import sleep

def hamming_dist(str1, str2):
    sum = 0
    for c1, c2 in zip(str1, str2):
        if (c1 != c2):
            sum +=1

    return sum            

def generate_str(length):
        ran_string = ""
        for i in range(length):
            ran_string += random.choice(string.printable)

        return ran_string           

def make_generation(target):
    generation = []
    for i in range(50):
        generation.append(generate_str(len(target)))

    return generation

def find_fittest(generation, target):
    fittest = ""
    lowest_score = len(target)

    for member in generation:
        score = hamming_dist(member, target)
        if score <= lowest_score:
            fittest = member
            lowest_score = score

    return fittest            

def get_fit_parents(generation, target, child):
    parents = []
    for i in range(2):
        fittest = find_fittest(generation, target)
        index = generation.index(fittest)
        parent = generation.pop(i)
        parents.append(parent)
        
    
    return parents        

def breed(str1, str2, target):
    child = ""
    i = 0

    for c1, c2, target_char in zip(str1, str2, target):

        if c1 == target_char or c2 == target_char:
            child += target_char
        else: 
            child += random.choice(string.printable)

    return child

target = "ayy lmao lol"

evolving = True

generation_ct = 0

child = ""
score = None

start_time = timeit.default_timer()

while evolving:
    if generation_ct == 0:
        generation = make_generation(target)
        parents = get_fit_parents(generation, target, None)
        child = breed(parents[0], parents[1], target)
        print(child)
    else:
        generation = make_generation(target)
        parent1 = child
        parent2 = find_fittest(generation, target)
        child = breed(parent1, parent2, target)
        score = hamming_dist(child, target)
        if score == 0:
            print(child)
            evolving = False
        else:
            print(child)

    generation_ct += 1

    
elapsed = timeit.default_timer() - start_time    
print("\nEvolved the phrase", "'" + target + "'", "in", generation_ct, "generations.")
print("Finished in%10f seconds." % elapsed)






