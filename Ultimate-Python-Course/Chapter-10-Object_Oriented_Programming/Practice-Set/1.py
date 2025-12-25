class Programmer:
    Company = "Microsoft"
    Job = "Software Developer"
    salary = 10000000
    def __init__(self,name,language,sector):
        self.name = name
        self.language = language
        self.sector = sector
        print("The name is",name,",The language is",language,"and The sector is.",sector)
Taufiq = Programmer("Taufiq","Python","AI")        
print("\n")
NJ = Programmer("NJ","Python and C++","Robotics")