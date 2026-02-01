from lib.grammar_stats import GrammarStats

"""
check method: when a text starts with a capital letter and ends with a valid punctuation mark,
the method returns True
"""
def test_grammar_stats_check_returns_true_for_valid_sentence():
    stats = GrammarStats()
    
    result = stats.check("Hello world.")
    assert result is True

"""
check method: when a text starts with a lowercase letter,
the method returns False
"""
def test_grammar_stats_check_returns_false_for_lowercase_start():
    stats = GrammarStats()
    
    result = stats.check("hello world.")
    assert result is False

"""
check method: when a text ends without punctuation,
the method returns False
"""
def test_grammar_stats_check_returns_false_for_missing_punctuation():
    stats = GrammarStats()
    
    result = stats.check("Hello world")
    assert result is False

"""
check method: when a text ends with an exclamation mark,
the method returns True
"""
def test_grammar_stats_check_returns_true_for_exclamation_mark():
    stats = GrammarStats()
    
    result = stats.check("Wow!")
    assert result is True

"""
percentage_good method: after multiple texts are checked, 
the method returns the percentage of texts that passed the check
"""
def test_grammar_stats_percentage_good_returns_correct_percentage():
    stats = GrammarStats()
    stats.check("Hello world.")       # passes
    stats.check("hello world.")       # fails
    stats.check("How are you?")       # passes
    
    result = stats.percentage_good()
    assert result == 66

"""
percentage_good method: when no texts have been checked,
the method returns 0
"""
def test_grammar_stats_percentage_good_returns_zero_when_no_texts_checked():
    stats = GrammarStats()
    
    result = stats.percentage_good()
    assert result == 0

"""
percentage_good method: when all texts fail the check,
the method returns 0
"""
def test_grammar_stats_percentage_good_returns_zero_when_all_fail():
    stats = GrammarStats()
    stats.check("hello")
    stats.check("world")
    
    result = stats.percentage_good()
    assert result == 0

"""
percentage_good method: when all texts pass the check,
the method returns 100
"""
def test_grammar_stats_percentage_good_returns_hundred_when_all_pass():
    stats = GrammarStats()
    stats.check("Hello.")
    stats.check("Wow!")
    
    result = stats.percentage_good()
    assert result == 100