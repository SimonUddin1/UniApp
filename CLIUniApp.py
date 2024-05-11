from colorama import Fore
from Stripts import AdminSystem as adm
from Stripts import StudentSystem as stu
from Stripts import DatabaseFunctions as data



def main():
  data.check_and_create_data()

  while True:
    user_type = input(f"{Fore.CYAN}University System: (A)dmin, (S)tudent, or X : {Fore.LIGHTWHITE_EX}").upper()

    # AdminSystem
    if user_type == "A":
      adm.admin_system()

    # StudentSystem
    elif user_type == "S":
      stu.student_system()

    # Exit
    elif user_type == "X":
      print(f"{Fore.YELLOW}Thank You{Fore.LIGHTWHITE_EX}") 
      break

    # Other
    else:
      print(f"{Fore.YELLOW}Invalid option. Please choose A, S, or X.")



if __name__ == "__main__":
    main()
