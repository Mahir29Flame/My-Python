marks  = {
    'Sami': 99,
    'Arik': 98,
    'Rabbi': 97,
    'Tanvir': 96,
    "Others by roll": [95,94,93,92,91,90.5,90]
}
print(marks.items())
print(marks.keys())
print(marks.values())
print("\n")
marks.update({'Sami': 99.5, 'Siam': 96})
print(marks)
print("\n")
print(marks.get('Mahir'))
# print(marks('Mahir'))
# marks.clear()
# print(marks)
