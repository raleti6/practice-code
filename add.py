if __name__ == '__main__':
 n = int(input())
if n % 100 != 0 and n %4 == 0 or n % 400 == 0:
 print("it is a leap year")
else:
    print("it is not a leap year")