from multiprocessing  import Process, current_process
import random
import time
from RandomWordGenerator import RandomWord

def analyze_file(file_name:str):
    file = open(file_name, "r+")
    string = file.read().lstrip()

    lenghts = dict([])
    glasnie = ['a', 'e', 'i', 'o', 'u', 'y']
    word, symbsum, maxlen, minlen, col_glasnie, col_soglasnie = 0, 0, 0, 11, 0, 0
    words = string.lower().split()
    
    for w in words:
        word = len(w)
        symbsum+=word

        for i in w:
            if i in glasnie:
                col_glasnie += 1
            else:
                col_soglasnie += 1

        if word > maxlen:
            maxlen = word
        
        if word < minlen:
            minlen = word

        if lenghts.get(str(word))!=None:
            lenghts[str(word)] += 1
        else:
            lenghts[str(word)] = 1
    
    a = ""
    for i in range(11):
        if lenghts.get(str(i)) != None:
            a+="Слов с "+  str(i) +" буквами:  " + str(lenghts.get(str(i)))+"\r\n"
        
    return "\nАнализ для файла " + str(current_process().pid) + ".txt\n" + "Всего символов: " + str(symbsum) + "\n\n" + a + "\n" + "Самое короткое слово: " + str(minlen) + "\nСамое длинное слово: " + str(maxlen) + "\n" + "Всего согласных: " + str(col_soglasnie) + "\nВсего гласных: " + str(col_glasnie)


def create_and_analyze():
    file = open("Process-" + str(current_process().pid) + ".txt","w+")

    r = RandomWord(10, constant_word_size=False, include_digits=False, include_special_chars=False)
    rnd = random.randint(100000, 5000000)

    for i in range(rnd):
        file.write(r.generate() + " ")
    
    file.close()
    
    print(analyze_file("Process-"+str(current_process().pid) + ".txt"))


if __name__ == '__main__':
    for i in range(7):
        t = Process(target = create_and_analyze)
        t.start()
        

    
   
    