from lib.string_builder import StringBuilder

def test_string_builder_is_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_add_string_to_string_builder():
    string_builder = StringBuilder()
    string_builder.add("fantastic") 
    assert string_builder.output() == "fantastic"

def test_length_of_string():
    string_builder = StringBuilder()
    assert string_builder.size() == 0

def test_multiple_add_output():
    string_builder=StringBuilder()
    string_builder.add('good')
    string_builder.add(' morning')
    assert string_builder.output() == 'good morning'
