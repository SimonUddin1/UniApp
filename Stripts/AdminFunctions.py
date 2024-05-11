from Stripts import DatabaseFunctions as data



# avg mark
def calc_avg_mark(student_id):
  marks = data.get_subjects_and_marks_by_id(student_id)
  total_mark = 0
  sub_count = 0

  for i in range(0, 8, 2):
    if marks[i] != '0':
      total_mark += int(marks[i+1])
      sub_count += 1

  if sub_count == 0:
    return 0
  else:
    return round(total_mark / sub_count, 2)
  



# Pass Fail 
def pass_fail(mark):

  if mark >= 50 and mark <= 100:
        return 'P'
  else:
        return "F"


