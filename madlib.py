#Madlibs game
#word game where you create a story
#by filling in blanks with random words
import nltk


#User inputs
word_map = {
    "adjective": ["JJ", "JJR", "JJS"],
    "noun": ["NN", "NNS", "NNP", "NNPS"],
    "verb": ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"],
    "verb_past": ["VBD", "VBN"]
}
def is_valid_pos(tagged_tokens, expected_type):
    valid_tags = word_map[expected_type]

    # Check ALL words instead of just first
    for word, tag in tagged_tokens:
        if tag in valid_tags:
            return True
    return False

def get_valid_input(prompt, expected_output):
    while True:
        word = input(prompt).strip()

        #Tokenize: breaking raw text into smaller units and Tagging: assigned grammatical labels to each token
        tokens = nltk.word_tokenize(word)
        tagged =  nltk.pos_tag(tokens)

        if is_valid_pos(tagged, expected_output):
            return word
        else:
            print(f" That doesn't seem like a {expected_output}. Try again.")

def play_madlib():
    print("Welcome to Madlib \n Fill in the blanks\n")
    adjective1 = get_valid_input("Adjective: ", "adjective")
    animal = get_valid_input("Animal (noun): ", "noun")
    place = input("Place: ")
    emotion = get_valid_input("Emotion (adjective): ", "adjective")
    verb1 = get_valid_input("Verb or action (can be a phrase): ", "verb")
    adjective2 = get_valid_input("Another Adjective: ", "adjective")
    noun1 = get_valid_input("Noun: ", "noun")
    noun2 = get_valid_input("Another Noun: ", "noun")
    verb2 = get_valid_input("Verb (past tense 'ed'): ", "verb")
    food = get_valid_input("Food (noun): ", "noun")


    story = f"""
    One day, a very {adjective1} {animal} went to {place}.
    It was feeling quite {emotion}, so it decided to {verb1}.
    
    Along the way, it found a {adjective2} {noun1} next to a {noun2}.
    Curious, the {animal} {verb2} it and suddenly turned into a giant {food}!
    
    Everyone in {place} couldn't believe their eyes.
    And that is how a {animal} became the most legendary {food} ever.
    """

    print("\nHere is your Mad Libs story:\n")
    print(story)

play_madlib()

