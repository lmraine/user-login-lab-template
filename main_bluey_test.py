import main

def test_main():
    user_string = "Bluey Heeler 2024"
    assert main.create_login(user_string) == "HeeleB24"