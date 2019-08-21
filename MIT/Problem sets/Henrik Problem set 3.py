def search(words,key):
    if len(words) > 2:
        mid = int(len(words)/2)
        return search(words[:mid],key) + search(words[mid:],key)
    if len(words)==2:
        if key == words[0] and key == words[1]:
            return 2
            print("2")
        elif key == words[0] or key == words[1]:
            return 1
            print("1")
        else:
            return 0
            print("0")
    elif len(words) == 1 and words[0]==key:
        return 1
        print("1")
    else:
        return 0
        print("0")

word = ["hi","there","my","name","is","Henrik","My","favorite","word","is","hi"]

search(["hi","no"],"hi")
