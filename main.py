
import time
dt = int(0)
log = []
while True:
  print("""
  WELCOME TO TEXT REVERSE
  
  
  
  MENU:
  1. TEXT REVERSE
  2. TEXT REVERSE READER
  """)
  option = input("ENTER YOUR OPTION: ")
  if option == "1":
    while True:
      print("""
      >TEXT REVERSE
      
      EXAMPLE:
      
      TEXT REVERSE:
        ENTER TEXT : GOOD
        RESULT IS : DOOG
      
      TEXT REVERSE READER:
        ENTER TEXT: OLLEH
        RESULT IS : HELLO
      """)
      option1 = input("ENTER TEXT: ")
      time.sleep(1)
      option1 = option1[::-1]
      print("RESULT IS:",option1)
      print("""
      1. TRY AGAIN
      2. REVERSE TEXT READER
      """)
      option2 = input("ENTER: ")
      if option2 == "1":
        continue
      elif option2 == "2":
        dt += 1
        break
      else:
        continue
  if option == "2" or dt == 1:
    while True:
      dt -= 1
      print("""
      > REVERSE READER
      
      EXAMPLE:
      
      TEXT REVERSE:
        ENTER TEXT : GOOD
        RESULT IS : DOOG
      
      TEXT REVERSE READER:
        ENTER TEXT: OLLEH
        RESULT IS : HELLO
      """)
      option3 = input("ENTER TEXT: ")
      time.sleep(1)
      option3 = option3[::-1]
      print("RESULT IS:",option3)
      print("""
      1. TRY AGAIN
      2. BACK
      """)
      option4 = input("ENTER OPTION: ")
      if option4 == "1":
        continue
      elif option4 == "2":
        break
      else:
        continue
  else:
    continue
