def crypt(mode, s, key, abc = "abcdefghijklmnopqrstuvwxyz"):
    upper = []
    
    s = list(s)
    key = list(key)
    
    i = 0
    while i < len(s):
        if s[i].isupper():
            upper.append(i)
            s[i] = s[i].lower()
        if (s[i] in abc) & (key[i % len(key)] in abc):
            a = abc.index(s[i])
            b = abc.index(key[i % len(key)])
            if mode.lower() == "encrypt":
                s[i] = abc[(a + b) % len(abc)]
            else:
                s[i] = abc[(a - b) % len(abc)]
            #s[i] = abc[abc.index(s[i]) + abc.index(key[i % len(key)])]
        i += 1
    
    for i in upper:
        s[i] = s[i].upper()
    
    temp = ""
    return temp.join(s)

def cryptfile(mode, file, newfile, key, cryptfunction, abc = "abcdefghijklmnopqrstuvwxyz"):
    file = open(file, "r")
    fcont = file.read()
    file.close()
    newfile = open(newfile, "w")
    try:
        newfile.write(cryptfunction(mode, fcont, key, abc))
    except Exception as e:
        print(str(e) + " when trying to write to the new file!")
    newfile.close()
