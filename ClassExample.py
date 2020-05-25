class myClass():
    def m1(self):
        print("m1 method")
    def m2(self, arg1):
        print(arg1+"m2 method")
    
class myClassChild(myClass):
    def m1(self):
        myClass.m1(self)
        print("child m1 method")
    def m2(self, arg1):
        print(arg1+" child m2 method")
def main():
    c=myClass()
    c.m1()
    c.m2("hello ")
    
    c2=myClassChild()
    c2.m1()
    c2.m2("hello hello ")

if __name__ == "__main__":
    main()


