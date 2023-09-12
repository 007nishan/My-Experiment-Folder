while True:
  print("SECURE LOGIN")
  username = input("Username > ")
  if username == "exit" or username == "Exit" or username == 'end' or username == "End" or username == 'quit' or username == "Quit":
    break  # This will exit the while loop

  if username == "mark":
    print("Welcome Mark!\nPlease enter your password:")
    password = input()
    for i in range(len(password)):
      print('*', end = '')
    if password == 'password':
      print("\nHola! you are successfully logged in/n")
    else:
      print("\nThat is an incorrect password!! Visit again after 30 minutes\n")
  
  elif username == "suzanne":
    print("Hey there Suzanne!\nPlease enter your password:")
    password = input()
    for i in range(len(password)):
      print('*', end = '')
    if password == 'password':
      print("\nHola! you are successfully logged in\n")
    else:
      print("\nThat is an incorrect password!! Visit again after 30 minutes\n")
  
  elif username == "joe":
    print("Hello! Joe\nPlease enter your password:")
    password = input()
    for i in range(len(password)):
      print('*', end = '')
    if password == 'password':
      print("\nHola! you are successfully logged in\n")
    else:
      print("\nThat is an incorrect password!! Visit again after 30 minutes\n")
  
  else:
    print("You don't have any account with us. First register yourself.\n")
