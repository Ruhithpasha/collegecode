# Sample program demonstrating dictionary usage in Python

# Creating a dictionary
student = {
    'name': 'Ruhith',
    'age': 20,
    'course': 'Python Programming'
}

# Accessing values
print('Name:', student['name'])
print('Age:', student['age'])
print('Course:', student['course'])

# Adding a new key-value pair
student['grade'] = 'A'
print('Updated student:', student)

# Updating a value
student['age'] = 21
print('After updating age:', student)

# Removing a key-value pair
removed = student.pop('course')
print('Removed course:', removed)
print('After removal:', student)

# Iterating through dictionary
for key, value in student.items():
    print(key, ':', value)
