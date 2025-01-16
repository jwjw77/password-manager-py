passwords = []
while True:

     print(" 1.Create a password  \n 2.Delete a password \n 3.Show your passwords")
     ask = input("Type the number below what you want to do with passwords or q to quit: ")

     if ask == "1":
          creating_password = input("Enter a password you want to create: ")
          passwords.append(creating_password)
          yes_no = input("Do you want to check your passwords? Type yes or no: ")
          
          if yes_no.lower() == "yes":

               for password in passwords:
                    print(password)

     elif ask == "2":
          delete_password = int(input("Enter a index of password you want to delete: "))
          passwords.remove(passwords[delete_password])
          yes_no = input("Do you want to check your passwords? Type yes or no: ")
          
          if yes_no.lower() == "yes":

               for password in passwords:
                    print(password)
          
     elif ask == "3":
          for password in passwords:
               print(password)
     elif ask == "q" or "Q":
          quit()
     else:
          print("Incorrect value. Enter your choice again.")