# parset durch den Leiden des jungen Werther
with open('/home/david/Dokumente/werther.txt', 'r') as werther: #please note that you have to specify the correct path for the textfile
    wordcount=0
    search_word="Werther"
    for word in werther:
        if search_word in word.split():
            wordcount +=1

print("Der junge", search_word, "kommt", wordcount, "Mal vor!")
