import main

def test_main():
    user_string = "Kermit Frog 1955"
    assert main.create_login(user_string) == "FrogK55"