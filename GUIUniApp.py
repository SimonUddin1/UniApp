import tkinter as tk
from tkinter import ttk, messagebox
from Stripts import StudentFunctions as stufun
from Stripts import DatabaseFunctions as data

student_id = 0

def gui_login():
  email = email_entry.get()
  password = password_entry.get()

  if not stufun.check_registration_email_suffix(email) or not stufun.validate_password_complexity(password):
    messagebox.showerror("Login Failed","Incorrect email or password format.")

  else:

    if not data.is_email_exists(email):
      messagebox.showerror("Login Failed","Student dose not exist.")

    else:
      
      if not password == data.get_pass_by_email(email):
        messagebox.showerror("Login Failed","Incorrect Password.")

      else:
        login_frame.grid_forget() #Remove Login Page
        enrol_frame.grid(row=0, column=0, padx=10, pady=10)
        enrol_label.config(text= "Loged In As : "+data.get_name_by_email(email))



def gui_add_course():
  email = email_entry.get()
  student_id = data.get_id_by_email(email)

  if student_id != '0':
    course_count = data.verify_course_load(student_id)

    if course_count >= 4:
      messagebox.showerror("Enrolment Failed!","Students are allowed to enrol in 4 subjects only.")

    else:
      course_id = stufun.generate_course_id()
      data.add_course_to_data(student_id,course_id,stufun.assign_random_mark())
      msg = "Enrolling in Subject - "+course_id+"\nYou are now enrolled in "+str(data.verify_course_load(student_id))+" out of 4 subjects."
      messagebox.showinfo("Enrolment Successful!", msg)



def gui_sub_list():
  enrol_frame.grid_forget()
  subject_frame.grid(row=0, column=0, padx=10, pady=10)

  email = email_entry.get()
  student_id = data.get_id_by_email(email)
  sub_count = data.verify_course_load(student_id)
  subject_label_log.config(text="Loged In As : "+data.get_name_by_email(email))
  subject_label_text.config(text="Showing "+str(sub_count)+" Subjects.")
  sub_text = ["","","",""]

  if student_id != '0':
    sub_and_mark = data.get_subjects_and_marks_by_id(student_id)
    count = 0
    for i in range(0, 8, 2):
        if sub_and_mark[i] != '0':
          count += 1
          sub_text[count-1] = "Subject  ::  "+sub_and_mark[i]+"  --  Mark =  "+sub_and_mark[i+1]+"  --  grade  =  "+stufun.calculate_grade(int(sub_and_mark[i+1]))+" "
          


    if sub_count == 1:
      subject_label1.config(text=sub_text[0])
      subject_label2.config(text="")
      subject_label3.config(text="")
      subject_label4.config(text="")
          
    if sub_count == 2:
      subject_label1.config(text=sub_text[0])
      subject_label2.config(text=sub_text[1])
      subject_label3.config(text="")
      subject_label4.config(text="")

    if sub_count == 3:
      subject_label1.config(text=sub_text[0])
      subject_label2.config(text=sub_text[1])
      subject_label3.config(text=sub_text[2])
      subject_label4.config(text="")

    if sub_count == 4:
      subject_label1.config(text=sub_text[0])
      subject_label2.config(text=sub_text[1])
      subject_label3.config(text=sub_text[2])
      subject_label4.config(text=sub_text[3])

          
          



def gui_sub_exit():
  subject_frame.grid_forget()
  enrol_frame.grid(row=0, column=0, padx=10, pady=10)



# Gui Starts
root = tk.Tk()
root.title("GUIUniApp")
root.geometry("600x400")
root.resizable(False, False) 



# Student Login
login_frame = ttk.Frame(root, padding="0")
login_frame.grid(row=1, column=0, sticky="nsew", padx=120, pady=60)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

app_label = ttk.Label(login_frame, text="GUIUniApp", font=("Arial", 34))
app_label.grid(row=0, columnspan=2, padx=10, pady=10)

login_label = ttk.Label(login_frame, text="Login Here", font=("Arial", 18))
login_label.grid(row=1, columnspan=2, padx=10, pady=10)

email_label = ttk.Label(login_frame, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

email_entry = ttk.Entry(login_frame, width=40)
email_entry.grid(row=2, column=1, padx=10, pady=10)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

password_entry = ttk.Entry(login_frame, show="*", width=40)
password_entry.grid(row=3, column=1, padx=10, pady=10)

login_button = ttk.Button(login_frame, text="Login", command=gui_login)
login_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")


# Enrol Subjects
enrol_frame = ttk.Label(root, padding="0")

enrol_label = ttk.Label(enrol_frame, text="", font=(10))
enrol_label.grid(row=0, column=1, padx=10, pady=5, sticky="W")

enrol_label2 = ttk.Label(enrol_frame, text="Enrol in subjects from hear")
enrol_label2.grid(row=1, column=1, padx=10, pady=5, sticky="W")

enrol_button = ttk.Button(enrol_frame, text="Enrol", command=gui_add_course)
enrol_button.grid(row=2, column=1, padx=90, pady=120, sticky="w")

subject_button = ttk.Button(enrol_frame, text="Subject List", command=gui_sub_list)
subject_button.grid(row=3, column=1, padx=90, pady=10, sticky="w")


# Subject list
subject_frame = ttk.Label(root, padding="0")

subject_label_log = ttk.Label(subject_frame, text="", font=(10))
subject_label_log.grid(row=0, column=0, padx=10, pady=5, sticky="w")

subject_label_text = ttk.Label(subject_frame, text="")
subject_label_text.grid(row=1, column=0, padx=10, pady=20, sticky="w")

subject_label1 = ttk.Label(subject_frame, text="")
subject_label1.grid(row=3, column=0, padx=10, pady=7, sticky="w")

subject_label2 = ttk.Label(subject_frame, text="")
subject_label2.grid(row=4, column=0, padx=10, pady=7, sticky="w")

subject_label3 = ttk.Label(subject_frame, text="")
subject_label3.grid(row=5, column=0, padx=10, pady=7, sticky="w")

subject_label4 = ttk.Label(subject_frame, text="")
subject_label4.grid(row=6, column=0, padx=10, pady=7, sticky="w")

ret_enrol_button = ttk.Button(subject_frame, text="Subject Enrolment", command=gui_sub_exit)
ret_enrol_button.grid(row=7, column=0, padx=90, pady=115, sticky="w")


root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Run the Tkinter event loop
root.mainloop()
