from colorama import Fore
from Stripts import DatabaseFunctions as data
from Stripts import StudentFunctions as stufun
from Stripts import AdminFunctions as admfun



def admin_system():

  while True:
    admin_option = input(f"\t{Fore.CYAN}Admin System (c/g/p/r/s/x): {Fore.LIGHTWHITE_EX}").lower()

    # Clear Student.data
    if admin_option == "c":
      clear_student_data_file()

    # Grade Grouping
    elif admin_option == "g":
      sort_students_by_grades()

    # Pass Fail Cetagory
    elif admin_option == "p":
      categorize_students_by_performance()

    # Delate students
    elif admin_option == "r":
      delete_student_record()

    # Print Students
    elif admin_option == "s":
      overview_students()

    # Exit
    elif admin_option == "x":
      break

    else:
      print(f"\t{Fore.YELLOW}Invalid option. Please choose c, g, p, r, s or x.")



# Clear Student.data
def clear_student_data_file():
  print(f"\t{Fore.YELLOW}Clearing student database.")
  admin_choice = input(f"\t{Fore.RED}Are you sure you want to clear the database (Y)ES / (N)o: {Fore.LIGHTWHITE_EX}").upper()

  if admin_choice == "Y":
    data.clear_database()
    print(f"\t{Fore.YELLOW}Student data cleared.")

  elif admin_choice == "N":
    return
  
  else:
    print(f"\t{Fore.YELLOW}Invalid option. Please choose Y or N.")



# Delete Student Record
def delete_student_record():
  student_id = input(f"\t{Fore.LIGHTWHITE_EX}Remove by ID: ")

  if(data.remove_student_by_id(student_id)):
    print(f"\t{Fore.YELLOW}Removing Student",student_id,"Account.")

  else:
    print(f"\t{Fore.RED}Student",student_id,"dose not exists.")



# Print Students
def overview_students():
  print(f"\t{Fore.YELLOW}Student List")
  students = data.read_student_data()

  if data.student_count() <= 1:
    print(f"\t\t{Fore.LIGHTWHITE_EX} < Nothing to Display >")

  else:
    for i in students[1:]:
      print(f"\t{Fore.LIGHTWHITE_EX}",i[1],"::",i[0],"-->",i[2])



# Pass Fail Cetagory
def categorize_students_by_performance():
  print(f"\t{Fore.YELLOW}PASS/FAIL Partition")
  students = data.read_student_data()
  pass_students = ""
  fail_students = ""

  if data.student_count() >= 1:

    for i in students[1:]:

      if admfun.pass_fail(admfun.calc_avg_mark(i[0])) == 'P':
        pass_students += i[1] + " :: " + i[0] + " --> GRADE: " + stufun.calculate_grade(admfun.calc_avg_mark(i[0])) + " - MARK: " + str(admfun.calc_avg_mark(i[0])) + " , "
    
      else:
        fail_students += i[1] + " :: " + i[0] + " --> GRADE: " + stufun.calculate_grade(admfun.calc_avg_mark(i[0])) + " - MARK: " + str(admfun.calc_avg_mark(i[0])) + " , "

  pass_students = "[ " + pass_students[:-2] + "]"
  fail_students = "[ " + fail_students[:-2] + "]"

  print(f"\t{Fore.LIGHTWHITE_EX}FAIL -->",fail_students)
  print(f"\t{Fore.LIGHTWHITE_EX}PASS -->",pass_students)



# sort students by grades
def sort_students_by_grades():
  print(f"\t{Fore.YELLOW}Grade Grouping")
  students = data.read_student_data()
  grade_HD = "HD --> [ "
  grade_D = "D --> [ "
  grade_C = "C --> [ "
  grade_P = "P --> [ "
  grade_Z = "Z --> [ "

  if data.student_count() > 1:

    for i in students[1:]:
      student_grade = stufun.calculate_grade(admfun.calc_avg_mark(i[0]))

      if student_grade == 'HD':
        grade_HD += i[1] + " :: " + i[0] + " --> GRADE: " + stufun.calculate_grade(admfun.calc_avg_mark(i[0])) + " - MARK: " + str(admfun.calc_avg_mark(i[0])) + " , "

      elif student_grade == ' D':
        grade_D += i[1] + " :: " + i[0] + " --> GRADE: " + stufun.calculate_grade(admfun.calc_avg_mark(i[0])) + " - MARK: " + str(admfun.calc_avg_mark(i[0])) + " , "

      elif student_grade == ' C':
        grade_C += i[1] + " :: " + i[0] + " --> GRADE: " + stufun.calculate_grade(admfun.calc_avg_mark(i[0])) + " - MARK: " + str(admfun.calc_avg_mark(i[0])) + " , "

      elif student_grade == ' P':
        grade_P += i[1] + " :: " + i[0] + " --> GRADE: " + stufun.calculate_grade(admfun.calc_avg_mark(i[0])) + " - MARK: " + str(admfun.calc_avg_mark(i[0])) + " , "
      
      else:
        grade_Z += i[1] + " :: " + i[0] + " --> GRADE: " + stufun.calculate_grade(admfun.calc_avg_mark(i[0])) + " - MARK: " + str(admfun.calc_avg_mark(i[0])) + " , "

  all_grades = [grade_HD, grade_D, grade_C, grade_P, grade_Z]

  for grades in all_grades:
    if len(grades) >= 10:
      grades = grades[:-2] + "]"
      print(f"\t{Fore.LIGHTWHITE_EX}",grades)

