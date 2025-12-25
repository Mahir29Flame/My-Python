numlist = [43,75,90,67,73,80,25]
filtered = filter(lambda x: x%5==0 ,numlist)
print(list(filtered))