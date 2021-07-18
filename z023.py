#!/usr/bin/env python


def if_valid_password(str_pass):
    # convert string of multiple passwords separated by coma to list
    pass_list = str_pass.split(",")
    print(pass_list)
    for password in pass_list:
        if len(password) < 6 or len(password) > 12:
            print(password + "is too short or too long")
            continue
        count = 0
        for c in password:
            # if c not in small or capital or numbers or special:
            if c in "qwertyuioplkjhgfdsazxcvbnm":
                a = 1
            elif c not in "qwertyuioplkjhgfdsazxcvbnm":
                b = 1
            elif c not in "0123456789":
                c = 1
            elif c not in "@#":
                d = 1
            else:
                count += 1
        print(count)
        if count == len(password):
            print(password + " is a valid password")
        else:
            print(password + " is NOT a valid password")


# p = input("Type password: ")
str_pass = "ABd1234@1,a F#,2w3E*,2We3345"
# print(if_valid_password(str_pass))
if_valid_password(str_pass)
