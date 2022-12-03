

# Break and continue
# Prime number

for n in range(2, 11):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:                                       # else clause is for 'for' loop and not 'if' loop
            print(n, 'is a prime number')
# When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue                            # else can be used here but changing the indent is required
    print("Found an odd number", num)

################################################
""" Defining and passing arguments to a function"""
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# / denotes positional or keyword and * denotes keyword only and anything before the / is a positional only argument, if there is no / then there are no positional only arguments"""




