#
# Example file for working with classes
#
class myClass():
  def method1(self):
    print("myclass method1")
  def method2(self,somestring):
    print("myclass method2 " + somestring)

class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("another method1")
  def method2(self,somestring):
    print("another method2 ")

def main():
  c=myClass()
  c.method1()
  c.method2("this is a string")
  c2=anotherClass()
  c2.method1()
  c2.method2("this is a string")

  
if __name__ == "__main__":
  main()
