from lib.gratitudes import Gratitudes

def test_check_for_empty_list():
    gr = Gratitudes()
    assert gr.format() == "Be grateful for: "

def test_added_gratitude():
    gr = Gratitudes()
    gr.add("Fluffy")
    assert gr.format() == "Be grateful for: Fluffy"

def test_added_gratitude2():
    gr = Gratitudes()
    gr.add("Fluffy")
    assert gr.gratitudes == ['Fluffy']
