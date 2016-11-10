Overview
-----------------

This is a simple Python 3 program that "evolves" a given string (the *target*) by breeding populations of
random strings and introducting random "mutations" until the correct string is "evolved." The fittest of a
given generation are "bred" to find the correct answer.

The fitness function chosen is the [hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
between two strings:

```python
def hamming_dist(str1, str2):

    sum = 0
    for c1, c2 in zip(str1, str2):
        if (c1 != c2):
            sum +=1

    return sum
```

Example Output:
-----------------

```
$ python3 genetic_alg.py
Input string: David Foster Walrus

rBc*_mqHW@J+'sBPuIx
q9Q*9[h5D|DT tQlGV:
Ys$kO Nz]sLb aJlF_y
=.t2! ufsLZB `3lksp
uKY61 ~|sy{[ ZSl_mf
j*(DE RJs.S9 ?-laus
oiM3/ [(s+y? ?alYus
BViSd +vs~OK Ral8us
l7v2d kusbqD  alCus
nav>d A1sxe: @al4us
Eavid r's.eC (alrus
Mavid 7osxe* 2alrus
8avid .os[er )alrus
:avid hos3er }alrus
Ravid nosmer Walrus
Javid 3os2er Walrus
@avid ,osxer Walrus
gavid zosLer Walrus
David qos=er Walrus
David Foster Walrus

Evolved the phrase 'David Foster Walrus' in 20 generations.
Finished in  0.069556 seconds.

```