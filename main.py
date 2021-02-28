import random


class Questions:
    question = ""
    nr = 0
    answer = ""

    def set_question(self, question):
        self.question = question

    def set_nr(self, nr):
        self.nr = nr

    def set_answer(self, answer):
        self.answer = answer


# Boxes for the question & answers | global
box1 = []
box2 = []
box3 = []
box4 = []
box5 = []


def import_data():
    questionlist = []
    titel = ""
    komma = ','
    f = open('Fragen&Antworten.txt', 'r')
    content = f.read()
    # Getting the the titel
    titel = content.partition(komma)[0]
    f.close()

    con = content.split(',')
    list_length = (len(con) - 1) / 2  # List_length to get the question and answer
    i = 1
    j = 1
    while i <= list_length:
        frage = Questions()
        while j <= 2:
            if j % 2 != 0:
                frage.question = con[j].lstrip()
                j += 1
            else:
                frage.answer = con[j]
                j += 1
        frage.nr = 1
        j = 1
        questionlist.append(frage)
        i += 1

    for i in range(len(questionlist)):
        if questionlist[i].nr == 1:
            box1.append(questionlist[i])
        elif questionlist[i].nr == 2:
            box2.append(questionlist[i])
        elif questionlist[i].nr == 3:
            box3.append(questionlist[i])
        elif questionlist[i].nr == 4:
            box4.append(questionlist[i])
        elif questionlist[i].nr == 5:
            box5.append(questionlist[i])

    print("Thema der Lernkartei:", titel)
    return questionlist


def ausgabe_frage(boxnr):
    tmp = Questions()
    if boxnr == 1:
        tmp = random.choice(box1)
        eingabe = input("Bitte beantworten sie die Frage: " + tmp.question + "\n")
        if eingabe == tmp.question:
            box1.remove(tmp)
            box2.append(tmp)
            print("Frage wurde richtig beantwortet\n")
        else:
            print("Die Antwort is Falsch! Richtig wäre: " + tmp.answer + "\n")
    if boxnr == 2:
        tmp = random.choice(box2)
        eingabe = input("Bitte beantworten sie die Frage: " + tmp.question + "\n")
        if eingabe == tmp.question:
            box2.remove(tmp)
            box3.append(tmp)
            print("Frage wurde richtig beantwortet\n")
        else:
            print("Die Antwort is Falsch! Richtig wäre: " + tmp.answer + "\n")
            box2.remove(tmp)
            box1.append(tmp)
    if boxnr == 3:
        tmp = random.choice(box3)
        eingabe = input("Bitte beantworten sie die Frage: " + tmp.question + "\n")
        if eingabe == tmp.question:
            box3.remove(tmp)
            box4.append(tmp)
            print("Frage wurde richtig beantwortet\n")
        else:
            print("Die Antwort is Falsch! Richtig wäre: " + tmp.answer + "\n")
            box3.remove(tmp)
            box2.append(tmp)
    if boxnr == 4:
        tmp = random.choice(box4)
        eingabe = input("Bitte beantworten sie die Frage: " + tmp.question + "\n")
        if eingabe == tmp.question:
            box4.remove(tmp)
            box5.append(tmp)
            print("Frage wurde richtig beantwortet\n")
        else:
            print("Die Antwort is Falsch! Richtig wäre: " + tmp.answer + "\n")
            box4.remove(tmp)
            box3.append(tmp)
    if boxnr == 5:
        tmp = random.choice(box5)
        eingabe = input("Bitte beantworten sie die Frage: " + tmp.question + "\n")
        if eingabe == tmp.question:
            print("Frage wurde richtig beantwortet\n")
        else:
            print("Die Antwort is Falsch! Richtig wäre: " + tmp.answer + "\n")
            box5.remove(tmp)
            box4.append(tmp)


def application():

    import_data()
    while True:
        print("Box (1) Fragen in der Box:", len(box1), "| Box (2)  Fragen in der Box:", len(box2)
              , "| Box (3) Fragen in der Box:", len(box3), "| Box (4) Fragen in der Box:", len(box4)
              , "| Box (5) Fragen in der Box:", len(box5), "| Programm schließen (0)")
        eingabe = input()
        if eingabe == "1":
            if len(box1) > 0:
                ausgabe_frage(1)
        elif eingabe == "2":
            if len(box2) == 0:
                print("Die Box ist leer\n")
                continue
            ausgabe_frage(2)
        elif eingabe == "3":
            if len(box3) == 0:
                print("Die Box ist leer\n")
                continue
            ausgabe_frage(3)
        elif eingabe == "4":
            if len(box4) == 0:
                print("Die Box ist leer\n")
                continue
            ausgabe_frage(4)
        elif eingabe == "5":
            if len(box5) == 0:
                print("Die Box ist leer\n")
                continue
            ausgabe_frage(5)
        elif eingabe == "0":
            print("Programm wird beendet! Danke für das Lernen")
            break


application()
