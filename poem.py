import random

# Work in progress.
# Add While loop to add 3 different words from each list
# 3 nouns, 3 verbs, 3 adjectives, 1 adverb, 2 prepositions
# Use .format()
# A -> an if first adjective starts with a vowel

nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert', 'gorilla']
verbs = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 'curdles']
adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberant', 'glistening']
prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']
adverbs = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']


def make_poem():
    n = random.choice(nouns)
    v = random.choice(verbs)
    adj = random.choice(adjectives)
    adv = random.choice(adverbs)
    pre = random.choice(prepositions)


    print(f'The poem starts something like this: {n} {v} {adj}, {pre} {adv}')
