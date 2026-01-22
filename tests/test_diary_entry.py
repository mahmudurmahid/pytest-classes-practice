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
