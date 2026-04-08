student = {
    "name":"Anurag",
    "age": 22,
    "Course" :"python",
    "marks":[87,90,78]
}

with open("report.txt","w") as f:
    f.write(f"Name:{student['name']}\n")
    f.write(f"Age{student['age']}\n")
    f.write(f"Age{student['Course']}\n")
    f.write(f"Age{student['marks']}\n")
    f.write(f"Average: {sum(student['marks'])/len(student['marks'])}")
