# file name: example_482.py

student = {"name": "Alice", "age": 20}

student.update({"age": 22, "city": "Paris"})

student_age = student.get("age") # 22

student_city = student.get("city") # Paris

print(student_age)

print(student_city)
