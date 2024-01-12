import main

def test_main():
    user_string = "Pete Cat 1991"
    assert main.create_login(user_string) == "CatP91"