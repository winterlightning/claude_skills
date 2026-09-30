import revise2 as a
from author import *
D=a.D
D['curved-showerhead-water-jets']['code']='''
path('pipe',(42,42),[('L',(42,16)),('A',(32,6),10,10,False),('L',(30,6)),('L',(22,14))])
path('head',(10,18),[('C',(22,14),(14,14),(18,14)),('C',(26,34),(33,14),(34,26)),('L',(10,18))],True);join('head','pipe')
for j,(x,y) in enumerate([(12,30),(20,38)]):line(f'jet-{j}',(x,y),(x-6,y+4))
'''
D['two-wheel-cart-with-a-marked-suitcase']['code']='''
path('cart',(6,6),[('A',(14,14),8,8,True),('L',(14,26)),('A',(18,30),4,4,False),('L',(22,30))])
line('floor',(22,30),(42,30));join('floor','cart')
path('case',(22,30),[('L',(22,18)),('A',(26,14),4,4,True),('L',(38,14)),('A',(42,18),4,4,True),('L',(42,30))]);join('case','cart');join('case','floor')
poly('handle',(26,14),(26,6),(38,6),(38,14));join('handle','case')
self.add_dot('mark',(32,22))
for x in (18,38):oval(f'wheel{x}',x,40,2,2)
'''
if __name__=='__main__':
 import author
 author.D=D
 generate(sys.argv[1:] or ['curved-showerhead-water-jets','two-wheel-cart-with-a-marked-suitcase','upright-skeleton-key'])
