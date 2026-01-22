class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.count_title = len(self.title.split())
        self.count_contents = len(self.contents.split())

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # count_title = len(self.title.split())
        # count_contents = len(self.contents.split())

        return self.count_title + self.count_contents

    def reading_time(self, wpm):
        time = self.count_contents // wpm
        return f"{time} mins"

    def reading_chunk(self, wpm, minutes):
        number_of_words = wpm * minutes
        return " ".join(self.contents.split()[:number_of_words])

result = DiaryEntry("My Title", "These are the contents")
format = result.format()
count_words = result.count_words()
reading_time = result.reading_time(2)
reading_chunk = result.reading_chunk(2, 2)
print(reading_chunk)