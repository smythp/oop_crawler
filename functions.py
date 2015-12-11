import lexicon
import synonyms
import cc

##import mobs

synonyms = synonyms.synonym_list
tokens = lexicon.tokens


def update_direction(direction,currentloc):
    if direction == 'W':
        return (currentloc[0] - 1,currentloc[1])
    if direction == 'N':
        return (currentloc[0],currentloc[1] + 1)
    if direction == 'E':
        return (currentloc[0] + 1,currentloc[1])
    if direction == 'S':
        return (currentloc[0],currentloc[1] - 1)


def check_commands(s):
    try:

## This first command needs to be fixed to be similar to the one after. Add similarize function to the loop?
        if s[0] == 'GO' and s[1] in tokens['DIRECTIONS']:
            cc.p.move((s[1]).upper())
            print('walking ',s[1].lower())
        if s[0] in tokens['DIRECTIONS']:
            if cc.p.check_move((s[0]).upper()) == False:
                print("Can't go in that direction!")
            else:
                cc.p.move((s[0]).upper())
                print('walking ',s[0].lower())         
        elif s[0] == 'LOOK' and 'L':
            print("You're at the",cc.Room.lookup[cc.p.c][0]," at location ",cc.p.c)
        elif s[0] == 'QUIT':
            print("Goodbye!")
            exit()
            
        else:
            print("Can't do that!")
    except IndexError:
        print("Index Error")


def synonymize(s):
    if isinstance(s,str):
        if s in synonyms.keys():
            return synonyms[s]
    if isinstance(s,list):
        for num in range(0,len(s)):
            if s[num] in synonyms.keys():
                s[num] = synonyms[s[num]]
        return s
    else:
        return None
    

def sanitize_sentence(sentence):
    try:
        while 1:
            if 'xxx' in sentence:
                sentence.remove('xxx')
            else:
                break
        return sentence
    except ValueError:
        return sentence

def parse(words):
    sentence = ['xxx','xxx','xxx']
    for word in words:
        if word.upper() in tokens['DIRECTIONS']:
            if sentence[1] == 'xxx':
                sentence[1] = word.upper()
        if word.upper() in tokens['VERBS']:
            if sentence[0] == 'xxx':
                sentence[0] = word.upper()
        if word.upper() in tokens['NOUNS']:
            if sentence[2] == 'xxx':
                sentence[2] = word.upper()
    return(sentence)



def debug_parse(words):
    sentence = ['xxx','xxx','xxx']
    for word in words:
        if word.upper() in tokens[0][1]:
            print(word,' is a direction')
            print('putting it in the sentence')
            if sentence[1] == 'xxx':
                sentence[1] = word.upper()
                print(sentence)
        if word.upper() in tokens[1][1]:
            print(word,' is a verb')
            print('putting it in the sentence')
            if sentence[0] == 'xxx':
                sentence[0] = word.upper()
                print(sentence)
        if word.upper() in tokens[2][1]:
            print(word,' is a noun')
            print('putting it in the sentence')
            if sentence[2] == 'xxx':
                sentence[2] = word.upper()
                print(sentence)
    return(sentence)
