#
# Example file for working with conditional statements
#

def main():
  x, y = 100, 100
  
  # conditional flow uses if, elif, else  
  if(x<y):
    st="x is less than y"
  elif(x==y):
    st="x is the same as y"
  else:
    st="x is grater than y"
  # conditional statements let you use "a if C else b"
  print(st)
  st = "x is than y" if x < y else "x is not less than y"
  print(st)

if __name__ == "__main__":
  main()
