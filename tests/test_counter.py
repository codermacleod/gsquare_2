from lib.counter import *

def test_count_checker():
    counter = Counter()
    counter.add(7)
    result = counter.report()
    assert result == "Counted to 7 so far."