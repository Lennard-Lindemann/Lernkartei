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
    print()


def ausgabe_frage(boxnr):
    tmp = Questions()
    if boxnr == 1:
        tmp = random.choice(box1)
        print(tmp.question)
        eingabe = input("Bitte Beantorten sie die Frag: ")
        if eingabe == tmp.question:
            box1.remove(tmp)
            box2.append(tmp)
            print(box2)


def application():
    titel = ""
    komma = ','
    questionlist = []
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

    print(box1)
    print("Thema der Lernkartei:", titel)
    print(content)
    ausgabe_frage(1)
    # while True:
    # print("Box 1 | Box 2 | Box 3 | Box 4 | Box 5")


application()
