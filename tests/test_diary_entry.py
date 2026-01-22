from lib.diary_entry import DiaryEntry

"""
format method: when the arguments title and contents are provided,
the method returns a correctly formatted diary entry string
"""
def test_diary_entry_format_returns_formatted_title_and_contents():
    diary_entry = DiaryEntry("My Title", "These are the contents")

    result = diary_entry.format()
    assert result == "My Title: These are the contents"

