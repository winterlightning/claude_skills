from revise6 import *
SPECS[9]['code']=SPECS[9]['code'].replace("(31,29),((32,32),(34,32),(35,29))","(32,29),((33,32),(34,32),(35,29))")
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
