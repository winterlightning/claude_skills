from revise import *
D['person-with-monocle-and-necktie']['code']=D['person-with-monocle-and-necktie']['code'].replace("path('shoulders',(8,44),[('L',(8,40)),('A',(16,32),8,8,True),('L',(24,32)),('L',(32,32)),('A',(40,40),8,8,True),('L',(40,44))])","path('shoulders',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)])")
if __name__=='__main__':generate(sys.argv[1:])
