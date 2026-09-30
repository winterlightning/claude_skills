from revise5 import *
SPECS[10]['code']=SPECS[10]['code'].replace("('C',(24,9),(7,10),(15,8)),('C',(44,8),(33,8),(41,10))","('C',(24,10),(7,15),(16,6)),('C',(44,8),(32,6),(41,15))")
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
