from revise3 import *
SPECS[6]["code"]=SPECS[6]["code"].replace("(18,36),(24,36),(30,36)","(18,37),(24,37),(30,37)").replace("(24,28),(24,36)","(24,28),(24,37)")
if __name__=="__main__":
 for i in map(int,sys.argv[1:]):make(i)
