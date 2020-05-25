def main():
  print("Hello world")
if __name__ == "__main__":
    main()

f=0
print(f)
f="abc"
print(f)
#pythin does not print stirng with number, u need to convert it into string using in biuld function str
print("this is a string: "+str(123))
# check glbal variable
def function():
  global f
  f="check global"
  print(f)

function()
print(f)
print(function())
print("case wth func name::")
#function is not executed at all, prnting the value of function defn itself-
# which evaluates to the strinf it prints
# this demonstrates that function is an object which is passed to input param of another function
print(function)



# delete global var f by using del f, if you print after deleting it will gv error

def func2(arg1, arg2):
  print (arg1, "", arg2)

def cube(x):
  return x*x*x


func2(10, 20)
print(func2(20, 30))
print(cube(10))


def power(num, x=1):
  res=1
  for i in range(x):
    res=res*num
  return res
 
print(power(10))
# python interpreter allows argument values to take in any order
print("power::"+str(power(x=3, num=2)))


def multi_add(*args):
  res=0
  for i in args:
    res=res+i
  return res

print("multi add::"+str(multi_add(4, 5, 1)))