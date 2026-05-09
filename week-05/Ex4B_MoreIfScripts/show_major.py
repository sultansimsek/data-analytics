student_name = input("What is your name? ")
student_major = input("What is your major? ")
majors_db = {
    "CSCI": {
        "name": "Computer Science",
        "dept_office": "Sheppard Hall, Room 314"
    },
    "BIOL": {
        "name": "Biology",
        "dept_office": "Science Bldg, Room 310"
    },
    "ENG": {
        "name": "English",
        "dept_office": "Kerr Hall, Room 201"
    },
    "MKT": {
        "name": "Marketing",
        "dept_office": "Westly Hall, Room 310"
    },
    "HIST": {
        "name": "History",
        "dept_office": "Kerr Hall, Room 114"
    },
    "unknown": {
        "name": "Unknown",
        "dept_office": ""
    }
}
if student_major in majors_db:
    print(f"Hello {student_name}! Your major is {majors_db[student_major]['name']}. \n The office for your department is located at {majors_db[student_major]['dept_office']}.")
else:    print(f"Hello {student_name}! Your major is not in our database. Please contact the registrar's office for more information about your major.")