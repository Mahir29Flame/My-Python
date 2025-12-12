name = input("Enter your name : ")
Date = "1/1/26"
print(
f'''
Dear {name},
You are selected!
{Date}
'''
)

# alter way
print("in MR. Harry's way :")
letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", name).replace("<|Date|>", Date))