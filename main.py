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


def import_data():
    print()


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
                frage.question = con[j]
                j += 1
            else:
                frage.answer = con[j]
                j += 1
        frage.nr = 1
        j = 1
        questionlist.append(frage)
        i += 1

    print(questionlist)
    print("Thema der Lernkartei:", titel)
    print(content)
    # while True:
    # print("Box 1 | Box 2 | Box 3 | Box 4 | Box 5")


application()
