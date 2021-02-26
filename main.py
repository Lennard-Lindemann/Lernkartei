class Questions:
    question = ""

    def set_question(self, question):
        self.question = question


def import_data():
    print()


def application():
    titel = ""
    f = open('Fragen&Antworten.txt', 'r')
    content = f.read()
    print(content)
    f.close()
    #while True:
     #   print("Box 1 | Box 2 | Box 3 | Box 4 | Box 5")


application()
