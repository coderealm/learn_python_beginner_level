# file name: example_479.py

student = {"name": "Alice", "age": 20}

student_grade1 = student.get("grade")          # None

student_grade2 = student.get("grade", "N/A")   # 'N/A'

print(student_grade1)

print(student_grade2)
