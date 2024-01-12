import main

def test_main():
    user_string = "Michael Jordan 1991"
    assert main.create_login(user_string) == "JordaM91"