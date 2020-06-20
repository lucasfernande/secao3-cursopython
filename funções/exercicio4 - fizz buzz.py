def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        return num

num = int(input('Digite um número: '))

fizzbuzz(num)