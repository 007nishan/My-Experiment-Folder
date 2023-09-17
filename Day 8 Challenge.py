while True:  
  print("\nAffirmations Generator.")
  name = input("What's your name?\n")
  if name.lower() == 'exit':
    break
  if name.lower() == "neha":
      DOW = input(f"Today is which day of the week {name}?\n")
      yon = input(f"Have you observed something special about your liking on {DOW}? \nYes/No\n")
      if yon.lower() == 'yes':
        like = input("What is it?\n")
      
        if DOW.lower() == "monday":
            print(f"You three are going to be make a great Monday, {name}, and {like}")
        elif DOW.lower() == "tuesday":
            print(f"What a wonderful Tuesday it would be with {like} and {name}")
        elif DOW.lower() == "wednesday":
            print(f"Happy Hump Day, {name}. {like} is a wonderful choice. Keep it up.")
        elif DOW.lower() == "thursday":
            print(f"{name}, your week is almost over!, but there is no expiry for {like}")
        elif DOW.lower() == "friday":
            print(f"{name}, It's FRIDAY! and your love for {like} will take you a long way")
        elif DOW.lower() == "saturday":
            print(f"{name}, It's a weekend! and what a day to love {like}")
        elif DOW.lower() == "sunday":
            print(f"{name}, It's the last day of the weekend! May your love for {like} last forever!!")
        else:
          print(f'First enter a valid weekday name {name}')
      else:
        print(f"I suspect if you are not a human!!. Bugger off!! You don't deserve {DOW} or anyday.")
  
  elif name.lower() == "david":
      DOW = input(f"Today is which day of the week {name}?\n")
      yon = input(f"Have you observed something special about your liking on {DOW}? \nYes/No\n")
      if yon.lower() == 'yes':
        like = input("What is it?\n")
      
        if DOW.lower() == "monday":
            print(f"It is going to be a great Monday, {name}, and {like}")
        elif DOW.lower() == "tuesday":
            print(f"What a wonderful Tuesday it would be with {like} and {name}")
        elif DOW.lower() == "wednesday":
            print(f"Happy Hump Day, {name}. {like} is a wonderful choice. Keep it up.")
        elif DOW.lower() == "thursday":
            print(f"{name}, your week is almost over!, but there is no expiry for {like}")
        elif DOW.lower() == "friday":
            print(f"{name}, It's FRIDAY! and your love for {like} will take you a long way")
        elif DOW.lower() == "saturday":
            print(f"{name}, It's a weekend! and what a day to love {like}")
        elif DOW.lower() == "sunday":
            print(f"{name}, It's the last day of the weekend! May your love for {like} last forever!!")
        else:
          print(f'First enter a valid weekday name {name}')
      else:
        print(f"I suspect if you are not a human!!. Bugger off!! You don't deserve {DOW} or anyday.")
  else:
      print("I do not know your name, do register with us first, still I hope you are having a great day!")
