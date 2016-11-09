
import random
import string

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
    for i in range(10):
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
#        print("c1: ", c1, " | c2: ", c2, " | target: ", target_char)
        if c1 == target_char or c2 == target_char:
            child += target_char
        else: 
            child += random.choice(string.printable)


    return child

def display_generation(generation):
    for member in generation:
        print(member, " | Fitness: ", hamming_dist(member, "carly"))


target = "carly"

evolving = True

generation_ct = 0

child = ""

while evolving:

    if generation_ct == 0:
        generation = make_generation(target)
        #display_generation(generation)
        parents = get_fit_parents(generation, target, None)
        print("Generation 0\n--------------------")
        print("Parents: ", parents)
        child = breed(parents[0], parents[1], target)
        print(child, " Fitness", hamming_dist(child, target))
    else:
        print("\nGeneration ", str(generation_ct), "\n--------------------")
        generation = make_generation(target)
        parent1 = child
        parent2 = find_fittest(generation, target)
        print("Parents ", parent1, parent2)
        child = breed(parent1, parent2, target)
        print(child, " Fitness", hamming_dist(child, target))

    generation_ct += 1

    if generation_ct == 2:
        evolving = False









