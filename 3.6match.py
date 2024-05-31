# New in version 3.10.

status = 401
match status:
    case 400:
        print("Bad request")
    case 401 | 403 | 404:  # -> matched
        print("Not allowed")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:  # -> no match with everything
        print("Something's wrong with the internet")
