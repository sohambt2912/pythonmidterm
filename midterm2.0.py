def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

result1 = palindrome("0974101607733149676776769413377061014790")
result2 = palindrome("7798338247658278460338648728567428338977")
result3 = palindrome("4257304920394478392772938744930294037524")
result4 = palindrome("2704702208931031198668911301398022074072")

print(result1)
print(result2)
print(result3)
print(result4)