class Word:
    def __init__(self, word="", definition=""):
        self.word = word
        self.definition = definition

    def giveDefinition(self):
        return self.definition

    def setDefinition(self, s):
        self.definition = s




a = Word(word="Python", definition="programming language")
defin = a.giveDefinition()
print(defin)

a.setDefinition("logical")

print(a.giveDefinition())