import urllib.request, json

def init_variables(alpha):
    url = f"https://raw.githubusercontent.com/wordset/wordset-dictionary/master/data/{alpha}.json"
    #print(f"Loading dictionary: {alpha}" "\n")
    load_dictionaries(url)

def load_dictionaries(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode()
        data = json.loads(source)
        letter_word_list(data)
    response.close()

def letter_word_list(data):
    letters = ["e", "g", "o", "s", "u", "l", "p", "i", "a", "z"]
    words = []

    for word in data:
        words.append(word)

    n = 0
    #print(letters)
    while n < len(words):
        unscrambler(words[n], letters)
        n +=1

def unscrambler(W, L):
    L = L.copy()
    n = 0
    word_min_lenght = 5
    sorted_list = []

    while n < len(L):
        for i in W:
            for j in L:
                find_index = i.find(j)
                n +=1
                if find_index == 0:
                    sorted_list.append(j)
                    L.remove(j)
                    break
    #output = "".join(final_list)
    output = "".join(sorted_list)
    if len(W) == len(output) and len(output) > word_min_lenght:
        print(output, "\n")
                  
def main():
    running_alpha = []
    alpha = "a"
    alpha_iteration = (x for x in running_alpha)
    for i in range(0, 26):
        running_alpha.append(alpha)
        alpha = chr(ord(alpha) +1)
        init_variables(next(alpha_iteration))

if __name__ == "__main__":
    main()