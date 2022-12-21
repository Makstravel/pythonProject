# This is a study Python script.
def chetn(x):
    return x%2==0


while True:
    x = int(input())
    if x==1:
        break
    if chetn(x):
        print(x)
