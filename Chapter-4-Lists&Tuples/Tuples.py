mr_tuple = (45678,"NJ", 29.0, 7, "BZS","Noob","NJ")
print(mr_tuple.count("NJ")) # Niiice

print("BZS" in mr_tuple)

code, name, SSC_batch, something, School, level, Name = mr_tuple
print(code)
print(name)
print(SSC_batch)
print(something)
print(School)
print(level)
print(Name)

_5xmr_tuple = mr_tuple * 5
print(_5xmr_tuple)
print(mr_tuple.index(29.0))
print(len(mr_tuple))

another_tuple = (1, 2, 3)
combined_tuple = mr_tuple + another_tuple
print(combined_tuple)
print(mr_tuple[1:4])
