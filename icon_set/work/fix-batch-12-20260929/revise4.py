import revise3 as a
from author import *
D=a.D
D['curved-showerhead-water-jets']['code']=D['curved-showerhead-water-jets']['code'].replace('[(12,30),(20,38)]','[(10,30),(18,38)]').replace('(x-6,y+4)','(x-4,y+4)')
D['two-wheel-cart-with-a-marked-suitcase']['code']=D['two-wheel-cart-with-a-marked-suitcase']['code'].replace("self.add_dot('mark',(32,22))","line('mark',(31,22),(33,22))")
D['upright-skeleton-key']['code']=D['upright-skeleton-key']['code'].split('for y in')[0]+"line('upper-tooth',(28,36),(35,36));join('upper-tooth','key')\nline('lower-tooth',(24,44),(35,44));join('lower-tooth','key')\n"
if __name__=='__main__':
 import author
 author.D=D
 generate(sys.argv[1:] or ['curved-showerhead-water-jets','two-wheel-cart-with-a-marked-suitcase','upright-skeleton-key'])
