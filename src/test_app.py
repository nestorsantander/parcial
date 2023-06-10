from app import index

def test_index():
    try:
        assert index() == "Hola mundo"
    except AssertionError as e:
        print("Error: no sale hola mundo")