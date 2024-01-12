def create_login(user_string):
    values = user_string.split()
    login = ""
    first_name_comp = values[0][0:1]
    last_name_comp = values[1][:5]
    digit_comp = values[2][-2:]
    
    login = last_name_comp + first_name_comp + digit_comp

    return login


if __name__ == '__main__':
    #remove pass and your code goes here
    user_string = str(input())
    login = create_login(user_string)
    print(login)
    