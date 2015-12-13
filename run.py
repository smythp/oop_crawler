import functions
import lexicon
import synonyms
import config

if config.DEBUG == True:
    while 1:
        playertypes = raw_input('> ')
        words = playertypes.split()
        print(words)
        sen = functions.parse(words)
        print(sen)
        s = functions.sanitize_sentence(sen)
        print(s)
        s = functions.synonymize(s)
        print("synonyms: ",s)
        functions.check_commands(s)
else:
    while 1:
        playertypes = raw_input('> ')
        words = playertypes.split()
        sen = functions.parse(words)
        s = functions.sanitize_sentence(sen)
        s = functions.synonymize(s)
        functions.check_commands(s)
