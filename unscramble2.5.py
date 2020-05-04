import urllib.request, json

def init_variables(alpha, user_input):
    url = f"https://raw.githubusercontent.com/wordset/wordset-dictionary/master/data/{alpha}.json"
    load_dictionaries(url, user_input)

def load_dictionaries(url, user_input):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode()
        data = json.loads(source)
        letter_word_list(data, user_input)
    response.close()

def letter_word_list(data, user_input):
    letters = list(user_input)
    #letters = ["e", "g", "o", "s", "u", "l", "p", "i", "a", "z"]
    words = []

    for word in data:
        words.append(word)

    n = 0
    #print(letters)
    while n < len(words):
        unscrambler(words[n], letters)
        n +=1

def unscrambler(W, L):
    l = L.copy()
    n = 0
    word_min_lenght = 5
    sorted_list = []

    while n < len(l):
        for i in W:
            for j in l:
                find_index = i.find(j)
                n +=1
                if find_index == 0:
                    sorted_list.append(j)
                    l.remove(j)
                    break
    output = "".join(sorted_list)
    if len(W) == len(output) and len(output) > word_min_lenght:
        print(L, "\t", output, "\n")
                  
def main():
    user_input = input("Give the string of letters to be solved: ")
    running_alpha = []
    alpha = "a"
    alpha_iteration = (x for x in running_alpha)
    for i in range(0, 26):
        running_alpha.append(alpha)
        alpha = chr(ord(alpha) +1)
        init_variables(next(alpha_iteration), user_input)

if __name__ == "__main__":
    main()
