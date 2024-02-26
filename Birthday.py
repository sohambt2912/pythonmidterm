def days_since_birthday(birthday):

    birth_year = int(birthday.split("-")[2])

    current_year = int(input("What is the current year? "))


    years_passed = current_year - birth_year - 1

    days_passed = years_passed * 365

    return days_passed



birthday = input("What is your birthday? (DD-MM-YYYY) ")
print(days_since_birthday(birthday))