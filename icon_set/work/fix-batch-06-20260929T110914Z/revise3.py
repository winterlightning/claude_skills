from revise2 import *
SPECS[3]['code']='''
poly('block',(6,24),(15,26),(24,28),(33,30),(42,32),(42,42),(6,42),closed=True)
path('left-handle',(6,24),[('L',(18,8)),('A',(26,14),5),('L',(15,26))]);join('left-handle','block')
path('right-handle',(24,28),[('L',(33,16)),('A',(41,22),5),('L',(33,30))]);join('right-handle','block')
'''
SPECS[9]['code']=SPECS[9]['code'].replace("(31,29),((32,32),(34,32),(35,29))","(32,31),((33,33),(35,33),(36,31))")
SPECS[13]['code']=SPECS[13]['code'].replace("(38,23),(36,30)","(34,23),(36,30)").replace("((28,18),(29,26),(24,28))","((25,18),(27,23),(24,26))")
SPECS[17]['code']=SPECS[17]['code'].replace("(24,24),(32,24)","(25,24),(32,24)")
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
