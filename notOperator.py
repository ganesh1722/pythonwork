a=0
if not a:
    print("Boolean of a is true")
if not (a%3==0 or a%5==0):
    print(f'{a} is not divisible by either 3 or 5')
else:
    print(f'{a} is divisible by either 3 or 5')