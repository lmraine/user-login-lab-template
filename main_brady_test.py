import main

def test_main():
    user_string = "Tom Brady 2003"
    assert main.create_login(user_string) == "BradyT03"