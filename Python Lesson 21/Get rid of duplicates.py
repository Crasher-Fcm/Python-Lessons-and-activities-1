student_data = {"id1": {'name': ['Sara'],
                        'class' : ['V'],
                        'subject_integration' : ["English", "Maths", "Science"]},
                        "id2":
                        {'name': ['David'],
                         "class": ['V'],
                         "subject_integration": ["English", "Maths", "Science"]
                         },
                         "id3":
                         {'name': ['Sara'],
                          'class': ['V'],
                          'subject_integration': ["English", "Maths", "Science"]
                          },
                          "id4":
                          {'name': ['John'],
                           'class': ['V'],
                           'subject_integration': ["English", "Maths", "Science"]
                           }
                           }  

result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)