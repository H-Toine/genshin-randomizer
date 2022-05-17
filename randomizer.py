import json
import random

def main():
    characters = get_characters("characters.json")
    included_characters = []
    excluded_characters = []
    for key in characters:
        if characters[key]:
            included_characters.append(key)
        else:
            excluded_characters.append(key)

    if len(excluded_characters) > 0 :
        print("Excluded characters: " + "\r\n".join(excluded_characters) )

    print(randomize(included_characters,int(input("How many characters? "))))
    input()

def randomize(characters, result_amount):
    result=[]
    for i in range(result_amount):
        char=random.choice(characters)
        result.append(char)
        characters.remove(char)
    return result

def get_characters(file):
    return json.loads(open(file).read())

if __name__ == "__main__":
    main()