from lib.diary_entry import DiaryEntry

"""
format method: when the arguments title and contents are provided,
the method returns a correctly formatted diary entry string
"""
def test_diary_entry_format_returns_formatted_title_and_contents():
    diary_entry = DiaryEntry("My Title", "These are the contents")

    result = diary_entry.format()
    assert result == "My Title: These are the contents"

"""
count_words method: when the arguments title and contents are provided,
the method returns the number of words used
"""
def test_diary_entry_count_words_returns_number_of_words():
    diary_entry = DiaryEntry("My Title", "These are the contents")

    result = diary_entry.count_words()
    assert result == 6

"""
reading_time method: when the argument wpm is provided,
the method returns a time value in mins of how long it will take to read the contents
"""
def test_diary_entry_reading_time_return_time_needed_to_read_contents_in_mins():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    
    result = diary_entry.reading_time(2)
    assert result == "2 mins"

"""
reading_chunk method: when the arguments wpm and minutes are provided,
the method returns a string of text which a user can read
"""
def test_diary_reading_chunk_returns_string_from_contents():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    
    result = diary_entry.reading_chunk(1, 3)
    assert result == "These are the"