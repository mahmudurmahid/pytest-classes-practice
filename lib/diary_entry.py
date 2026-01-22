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
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass


result = DiaryEntry("My Title", "These are the contents")
format = result.format()
count_words = result.count_words()
reading_time = result.reading_time(2)
print()