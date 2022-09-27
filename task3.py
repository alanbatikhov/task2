# 1task
# def say_hello_bye(text, number):
    # if number == 1:
        # print(f'Hello {text}')
    # else number == 0:
        # print(f'Bye {text}')
# say_hello_bye('alan', 1)
# say_hello_bye('alan', 0)  
#3task
def sum_three(a, b, c):
    if a == b or b == c or a==c:
        sum = 0
    else:
        sum = a + b + c
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))