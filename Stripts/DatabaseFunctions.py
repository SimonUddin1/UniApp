import os
import csv
from Stripts import StudentFunctions as stufun




# check or create Student.data
def check_and_create_data():
  expected_columns = ['id', 'name', 'email', 'password', 'sub1', 'mark1', 'sub2', 'mark2', 'sub3', 'mark3', 'sub4', 'mark4']
    
  if os.path.isfile('Student.data'):
    with open('Student.data', 'r', newline='') as csvfile:
      reader = csv.reader(csvfile)
      existing_columns = next(reader, None)
      if existing_columns == expected_columns:
        return

  with open('Student.data', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(expected_columns)


### STUDENT Functions :: Starts###

# check if the Student id already exists
def create_and_check_student_id():
  if os.path.isfile('Student.data'):
    with open('Student.data', 'r', newline='') as datafile:
      reader = csv.reader(datafile)
      next(reader)
      existing_ids = [row[0] for row in reader]
        
    # Check if any of the existing IDs match the newly generated ID
    while True:
      new_student_id = stufun.create_student_id()
      if new_student_id not in existing_ids:
        break

    return new_student_id
  else:
    return None



#checks if the email exists in Student.data
def is_email_exists(email):
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            next(reader)  
            for row in reader:
                if row[2] == email: 
                    return True
    except FileNotFoundError:
        print("Student.data file not found.")
        return False  
    return False



# Get password with email from Student.data
def get_pass_by_email(email):
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            next(reader)  
            for row in reader:
                if row[2] == email: 
                    return row[3]
    except FileNotFoundError:
        print("Student.data file not found.")
        return 'no-pass' 
    return 'no-pass'



# Get name with email from Student.data
def get_name_by_email(email):
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            next(reader)  
            for row in reader:
                if row[2] == email: 
                    return row[1]
    except FileNotFoundError:
        print("Student.data file not found.")
        return 'no-name'  
    return 'no-name'  



# Get id with email from Student.data
def get_id_by_email(email):
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            next(reader)  
            for row in reader:
                if row[2] == email: 
                    return row[0]
    except FileNotFoundError:
        print("Student.data file not found.")
        return '0'  
    return '0'



# Enter Record of Student
def initiate_student_signup(email, password, name):
  student_id = create_and_check_student_id()
  new_row = [student_id, name, email, password, '0', '0', '0', '0', '0', '0', '0', '0']

  try:
    with open('Student.data', 'a', newline='') as datafile:
      writer = csv.writer(datafile)
      writer.writerow(new_row)
  except Exception as e:
    print("\tAn error occurred while adding student:", e)



# Update the password by id
def update_password_by_id(student_id, new_password):
    # Read the existing data from the file
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            rows = list(reader)
    except FileNotFoundError:
        print("Student.data file not found.")
        return False

    # Update the password for the given student ID
    found = False
    for row in rows:
        if row[0] == student_id:  # Assuming ID is at index 0 in each row
            row[3] = new_password  # Assuming password is at index 3 in each row
            found = True
            break
    
    # Write the updated data back to the file
    if found:
        try:
            with open('Student.data', 'w', newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerows(rows)
            return True
        except Exception as e:
            print("An error occurred while updating password.")
            return False
    else:
        return False



# Enrole new course
def add_course_to_data(student_id,course_id,mark):
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            rows = list(reader)

            for row in rows[1:]:
                if row[0] == student_id:
                    for i in range(4, 12, 2):  # Loop through sub and mark columns
                        sub = row[i]
                        if sub != '0':
                            continue  # Skip if sub is not "0"
                        row[i] = course_id
                        row[i + 1] = mark
                        break  # Stop iterating after updating the first non-"0" sub and mark
                    break  # Stop iterating once the row is found

            # Write the updated rows back to the file
            with open('Student.data', 'w', newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerows(rows)
    except FileNotFoundError:
        print("Student.data file not found.")



# Course Count
def verify_course_load(student_id):
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            rows = list(reader)
            count = 0

            for row in rows[1:]:
                if row[0] == student_id:
                    for i in range(4, 12, 2):  # Loop through sub and mark columns
                        sub = row[i]
                        if sub != '0':
                            count += 1  # Skip if sub is "0"
                    break  # Stop iterating once the row is found
            return count
    except FileNotFoundError:
        print("Student.data file not found.")
        return -1
    


# Remove Subject
def drop_course_by_id(student_id, subID):
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            rows = list(reader)

            for row in rows[1:]:
                if row[0] == student_id:
                    for i in range(4, 12, 2):  # Loop through sub and mark columns
                        sub = row[i]
                        if subID == sub:
                            row[i] = '0'
                            row[i + 1] = '0'
                            found =  True
                            break
                        else:
                            found = False
            
        # Write the updated rows back to the file
        with open('Student.data', 'w', newline='') as datafile:
            writer = csv.writer(datafile)
            writer.writerows(rows)
        return found
    except FileNotFoundError:
        print("Student.data file not found.")
        return False



# get subjects by id
def get_subjects_and_marks_by_id(student_id):
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            next(reader)  # Skip header
            for row in reader:
                if row[0] == student_id:
                    return row[4:]  # Return sub1, mark1, sub2, mark2, sub3, mark3, sub4, mark4
        # If student ID not found
        return None
    except FileNotFoundError:
        print("Student.data file not found.")
        return None

### STUDENT Functions :: Ends###




### ADMIN Functions :: Starts###

# Clear The Database
def clear_database():
    try:
        with open('Student.data', 'w', newline='') as datafile:
            writer = csv.writer(datafile)
            writer.writerow(["id", "name", "email", "password", "sub1", "mark1", "sub2", "mark2", "sub3", "mark3", "sub4", "mark4"])
    except Exception as e:
        print("An error occurred while clearing the database:")



# Remove student by id
def remove_student_by_id(student_id):
    try:
        # Read the existing data from the file
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            rows = list(reader)

        # Find and remove the row with the specified ID
        removed = False
        for row in rows:
            if row[0] == student_id:
                rows.remove(row)
                removed = True
                break

        # Write the updated data back to the file
        if removed:
            with open('Student.data', 'w', newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerows(rows)
            return True
        else:
            return False

    except FileNotFoundError:
        print("Student.data file not found.")


# Take student data
def read_student_data():
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            data = list(reader)
        return data
    except FileNotFoundError:
        print("Student.data file not found.")
        return None
    


#student Count
def student_count():
    try:
        with open('Student.data', 'r', newline='') as datafile:
            reader = csv.reader(datafile)
            next(reader)  # Skip the header row
            row_count = sum(1 for _ in reader)  # Count the rows
            return row_count

    except FileNotFoundError:
        print("Student.data file not found.")
        return 0



