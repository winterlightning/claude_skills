from revise4 import *
D['person-with-monocle-and-necktie']['code']="""
oval('face',24,17,13,13)
path('shoulders',(8,44),[('A',(24,34),16,10,True),('A',(40,44),16,10,True)]);join('face','shoulders')
oval('monocle',25,17,3,3);line('temple',(28,17),(37,17));join('temple','face');join('temple','monocle')
poly('tie',(24,34),(16,39),(24,44),(32,39),(24,34));join('tie','shoulders')
"""
if __name__=='__main__':generate(sys.argv[1:])
