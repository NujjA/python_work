sentence = "All work and no play makes Jack a dull boy"
createword = ""
for word in sentence:
    if word == " ":
        print(createword)
        createword = ""
    else:
        createword += word
print(createword) #print last word
