from module import myfunc
# __name__="__main__"  # this is  acheaky lil trick
# print(__name__,type(__name__)) 
if __name__=="__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code from the file it belongs to")