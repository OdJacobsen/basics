from random import choice

nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert', 'gorilla']
verbs = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 'curdles']
adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberant', 'glistening']
prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']
adverbs = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']


def make_poem():
    """Create a randomly generated poem, returned as a multi-line string.
    While loops keep looping until first noun is not second noun, as well for noun 3.
    """
    # Pull three nouns randomly
    n1 = choice(nouns)
    n2 = choice(nouns)
    n3 = choice(nouns)
    #Make sure that all are different 
    while n1 == n2:
        n2 = choice(nouns)
    while n1 == n3 or n2 == n3:
        n3 = choice(nouns)
    
    # Pull three random verbs
    v1 = choice(verbs)
    v2 = choice(verbs)
    v3 = choice(verbs)
    while v1 == v2:
        v2 = choice(nouns)
    while v1 == v3 or v2 == v3:
        n3 = choice(verbs)

    # Pull three adjectives 
    adj1 = choice(adjectives)
    adj2 = choice(adjectives)
    adj3 = choice(adjectives)
    while adj1 == adj2:
        adj2 = choice(nouns)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = choice(adjectives)

    #Pull one adverb
    adv1 = choice(adverbs)
    
    #Pull two prepositions
    pre1 = choice(prepositions)
    pre2 = choice(prepositions)
    while pre1 == pre2:
        pre2 = choice(prepositions)

    if 'aeiou'.find(adj1[0]) != -1:  # first letter is a vowel
        article = "An"
    else:
        article = "A"

    # add line to poem
    poem = f'{article} {adj1} {n1}\n\n'  # title of poem
    poem = poem + f'{article} {adj1} {n1} {v1} {pre1} the {adj2} {n2}\n'
    poem = poem + f'{adv1} the {n2} {v2}\n'
    poem = poem + f'the {n2} {v3} {pre2} a {adj3} {n3}'

    return poem

print(make_poem())
