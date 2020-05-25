def main():
    x, y = 10, 100
    if(x<y):
        st="x is less than y"
    elif(x>y):
        st="x is more than y"
    else:
        st="x is equal to y"
    print(st)

    for i in range(5,10):
        if(i % 2 == 0): continue
        print(i)

main()


    

