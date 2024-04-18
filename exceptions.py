a = [11,22,33]
try:
    a=10/0
    print(a[2])
    print(a[5])            # one type of try at a time
    print(y)
except ZeroDivisionError:  #divided by zero
    print("caught")
except IndexError:         #index error
    print("Index")
except Namerror:           #naming error
  print("undefined variable")  
except:
    print("common block")
finally:
    print("Exceptions were caught")
