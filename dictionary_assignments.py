"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
student_info={'student_name':"rasesh",'age':23,"roll_no":234,'class':'xi','section':'B','percentage':"90%",'college_name':'GIFT'}
print(student_info['percentage'])
"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
# students_info={'stu1':{'student_names':"ram","ages":45,"class":'x','section':'b','university':'gift'},
#                'stu2':{'student_names':"sam","ages":46,"class":'xi','section':'c','university':'gita'},
#                'stu3':{'student_names':"kam","ages":47,"class":'xii','section':'a','university':'giet'}
#                }
D = {
    'students':{
        'students_name':['ram','hari'],
        'students_age':[23,45,56],
        'students_class':['xi','xii','xiii'],
        'students_section':['A','B','C'],
        'students_university':['gift','gita','giet']
        }}
print(D['students']['students_class'][2])
"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
e1={"emp1":{"emp_name":"ram","salary":50000,"desg":"software_engineer"},"emp2":{"emp_name":"sam","salary":60000,"desg":"software_tester"},
    "emp3":{"emp_name":"hari","salary":60000,"desg":"autmation_engineer"},"emp4":{"emp_name":"vasu","salary":70000,"desg":"system_engineer"}}
print(e1["emp3"]["desg"])