# random module import
import random

#create three lists, one of verbs, one of adjectives, and one of nouns
verbs = ['Leverage','Sync','Target','Gamify','Offline','Crowd-sourced','24/7','Lean-in','30,000 foot']
adjectives = ['A/B Tested','Freemium','Hyperlocal','Siloed','B-to-B','Oriented','Cloud-based','API-based','Smart','Extensible']
nouns = ['Early Adopter','Low-hanging Fruit','Pipeline','Splash Page','Productivity','Process','Tipping Point','Paradigm','Solution','Architecture','Core Competency','Strategy','Mindshare','Portal','Space']

# randomly select one of each list
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# combine the three lists into a single string
phrase = verb + ' ' + adjective + ' ' + noun

# print the string
print(phrase)
