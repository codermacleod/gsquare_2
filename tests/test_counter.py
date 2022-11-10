from lib.counter import *

def test_count_checker_reports_zero():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counter_adds_number():
    counter = Counter()
    counter.add(7)
    assert counter.report() == "Counted to 7 so far."

def test_counter_adds_multiple_numbers_to_count():
    counter = Counter()
    counter.add(5)
    counter.add(2)
    assert counter.report() == "Counted to 7 so far."