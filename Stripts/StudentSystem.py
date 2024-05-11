from colorama import Fore
from Stripts import StudentFunctions as stufun
from Stripts import DatabaseFunctions as data



def student_system():

  while True:
    student_option = input(f"\t{Fore.CYAN}Student System (l/r/x): {Fore.LIGHTWHITE_EX}").lower()

    # Register
    if student_option == "r":
      student_register()
    
    # Login
    elif student_option == "l":
      student_login()

    # Exit
    elif student_option == "x":
      break

    else:
      print(f"\t{Fore.YELLOW}Invalid option. Please choose l, r, or x.")



# The Student System – Register
def student_register():
  print(f"\t{Fore.GREEN}Student Sign Up{Fore.LIGHTWHITE_EX}")

  while True:
    remail = input("\tEmail: ") # email input
    rpassword = input("\tPassword: ") # password input

    # Incorrect email or password format Check
    if not stufun.check_registration_email_suffix(remail) or not stufun.validate_password_complexity(rpassword):
      print(f"{Fore.RED}\tIncorrect email or password format.{Fore.LIGHTWHITE_EX}")

    # Email and password formats are acceptable Check
    else:
      print(f"\t{Fore.YELLOW}Email and password formats are acceptable.{Fore.LIGHTWHITE_EX}")

      rexists = data.is_email_exists(remail)
      rexists_name = data.get_name_by_email(remail)

      # Student already exists Check
      if rexists:
        print(f"{Fore.RED}\tStudent", rexists_name, "already exists.")
        break

      else:
        name = input(f"\t{Fore.LIGHTWHITE_EX}Name : ") # name input

        print(f"{Fore.YELLOW}\tEnrolling Student", name)
        # Student Signup Function
        data.initiate_student_signup(remail, rpassword, name)
        break



# The Student System – Login
def student_login():
  print(f"\t{Fore.GREEN}Student Sign In{Fore.LIGHTWHITE_EX}")

  while True:
    lemail = input("\tEmail: ") # email input
    lpassword = input("\tPassword: ") # password input

    # Incorrect email or password format Check
    if not stufun.check_registration_email_suffix(lemail) or not stufun.validate_password_complexity(lpassword):
      print(f"{Fore.RED}\tIncorrect email or password format.{Fore.LIGHTWHITE_EX}")
    
    # Email and password formats are acceptable Check
    else:
      print(f"\t{Fore.YELLOW}Email and password formats are acceptable.{Fore.LIGHTWHITE_EX}")

      lexists = data.is_email_exists(lemail)

      if not lexists:
        print(f"{Fore.RED}\tStudent dose not exist.{Fore.LIGHTWHITE_EX}")
      
      else:
        data_password = data.get_pass_by_email(lemail)

        if not (lpassword == data_password):
          print(f"{Fore.RED}\tIncorrect Password.{Fore.LIGHTWHITE_EX}")
          break

        else:
          student_login_features(data.get_id_by_email(lemail))
          break


# Loged in students options
def student_login_features(student_id):

  while True:
    student_course = input(f"\t\t{Fore.CYAN}Student Course Menu (c/e/r/s/x) : {Fore.LIGHTWHITE_EX}").lower()

    # Change Pass
    if student_course == "c":
      update_password(student_id)
    
    # Enrole Sub
    elif student_course == "e":
      add_course(student_id)

    # Remove Sub
    elif student_course == "r":
      drop_course(student_id)

    # Subject List
    elif student_course == "s":
      display_current_cnrolment_courses(student_id)

    # Exit
    elif student_course == "x":
      break

    else:
      print(f"\t\t{Fore.YELLOW}Invalid option. Please choose c, e, r, s or x.")



# Change Password of Students
def update_password(student_id):
  print(f"\t\t{Fore.YELLOW}Updating Password.{Fore.LIGHTWHITE_EX}")

  while True:
    newPassword = input("\t\tNew Password: ") # email input
    confirmPassword = input("\t\tConfirm Password: ") # password input

    if stufun.validate_password_complexity(newPassword):

      while True:

        if newPassword != confirmPassword :
          print(f"\t\t{Fore.RED}Password dose not match - Try Again{Fore.LIGHTWHITE_EX}")
          confirmPassword = input("\t\tConfirm Password: ") # password input

        else:
          data.update_password_by_id(student_id, newPassword)
          break
      break
    
    else:
      print(f"{Fore.RED}\t\tIncorrect password format.{Fore.LIGHTWHITE_EX}")
      break



# Enrol in Subjects
def add_course(student_id):
  course_count = data.verify_course_load(student_id)

  if course_count >= 4:
    print(f"\t\t{Fore.RED}Students are allowed to enrol in 4 subjects only.{Fore.LIGHTWHITE_EX}")
  
  else:
    course_id = stufun.generate_course_id()
    data.add_course_to_data(student_id,course_id,stufun.assign_random_mark())
    course_count = data.verify_course_load(student_id)

    print(f"\t\t{Fore.YELLOW}Enrolling in Subject -",course_id)
    print(f"\t\t{Fore.YELLOW}You are now enrolled in",course_count,"out of 4 subjects.")



# Remove subject
def drop_course(student_id):
  subID = input("\t\tRemove Subject by ID: ") # Subject ID input

  if(data.drop_course_by_id(student_id, subID) and subID != '0'):
    print(f"\t\t{Fore.YELLOW}Droping Subject-",subID)
    print(f"\t\t{Fore.YELLOW}You are now enrolled in",data.verify_course_load(student_id), "out of 4 subjects.")
  else:
    print(f"\t\t{Fore.YELLOW}Subject ID -", subID, "dosen't exists.")



# Print Subjects
def display_current_cnrolment_courses(student_id):
  sub_and_mark = data.get_subjects_and_marks_by_id(student_id)
  print(f"\t\t{Fore.YELLOW}Showing ", data.verify_course_load(student_id), "Subjects.")

  for i in range(0, 8, 2):
    if sub_and_mark[i] != '0':
      print(f"\t\t{Fore.LIGHTWHITE_EX}[ Subject::",sub_and_mark[i],"-- mark =",sub_and_mark[i+1],"-- grade = ",stufun.calculate_grade(int(sub_and_mark[i+1])),"]")


