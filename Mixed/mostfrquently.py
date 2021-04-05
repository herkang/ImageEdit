from collections import Counter
text="I am a commuter at the University of Minnesota Twin Cities. I use the bus system " \
    "as my transportation.I live in the east side of Saint Paul so it takes more than an"\
    "hour to come to the University. eastside of Saint Paul"
words=text.split()
counter=Counter(words)
top_three=counter.most_common(3)
print(top_three)
