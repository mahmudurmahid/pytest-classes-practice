class GrammarStats:
    def __init__(self):
        self.texts_checked = 0
        self.texts_passed = 0

    def check(self, text):
        self.texts_checked += 1

        if text and text[0].isupper() and text[-1] in ".!?":
            self.texts_passed += 1
            return True
        else:
            return False

    def percentage_good(self):
        if self.texts_checked == 0:
            return 0

        percentage = (self.texts_passed * 100) // self.texts_checked
        return percentage


stats = GrammarStats()
print(stats.check("Hello, World!"))
print(stats.percentage_good())