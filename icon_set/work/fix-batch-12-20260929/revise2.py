import revise as a
from author import *
D=a.D
D['bow-tie-suit']['shape']='SQUARE'
D['bow-tie-suit']['code']='''
poly('bow',(14,6),(24,12),(34,6),(34,18),(24,12),(14,18),closed=True)
poly('lapels',(14,18),(24,36),(34,18));join('lapels','bow')
for s in (-1,1):
 x=lambda a:24+s*a
 poly(f'jacket{s}',(x(10),18),(x(18),22),(x(17),42));join(f'jacket{s}','bow')
line('seam',(24,36),(24,42));join('seam','lapels')
'''
D['circular-emblem-with-banner']['code']=D['circular-emblem-with-banner']['code'].replace('(10,26)','(10,25)').replace('(38,26)','(38,25)')
D['curved-showerhead-water-jets']['code']='''
path('pipe',(42,42),[('L',(42,18)),('A',(30,6),12,12,False),('C',(22,8),(26,6),(24,6))])
path('head',(12,12),[('C',(22,8),(15,9),(18,8)),('C',(30,12),(25,8),(28,9)),('C',(30,30),(35,17),(35,25)),('L',(12,12))],True);join('head','pipe')
for j,(x,y) in enumerate([(12,28),(20,36)]):line(f'jet-{j}',(x,y),(x-6,y+6))
'''
D['two-linked-wifi-routers']['code']=D['two-linked-wifi-routers']['code'].replace('(12,14)','(12,15)').replace('(36,30)','(36,31)')
D['two-wheel-cart-with-a-marked-suitcase']['code']=D['two-wheel-cart-with-a-marked-suitcase']['code'].replace("line('mark',(31,22),(33,22))","self.add_dot('mark',(32,22))")
# Split the receiving floor so exact axis separation can certify the mark distance.
D['two-wheel-cart-with-a-marked-suitcase']['code']=D['two-wheel-cart-with-a-marked-suitcase']['code'].replace("('L',(42,30))])","('L',(22,30))]);line('floor',(22,30),(42,30));join('floor','cart')").replace("join('case','cart')","join('case','cart');join('case','floor')")
D['upright-skeleton-key']['code']=D['upright-skeleton-key']['code'].replace('(34,42)','(35,43)')
D['cat-head-affection-component']['code']=D['cat-head-affection-component']['code'].replace('(6,28)','(6,26)').replace('(24,28)','(24,26)').replace('(12,32)','(12,30)').replace('(18,32)','(18,30)').replace('(32,23)','(32,21)').replace('(36,20)','(36,18)').replace('(28,20)','(28,18)')
D['two-opposing-gamepads']['code']=D['two-opposing-gamepads']['code'].replace('p(6,12)','p(6,10)').replace('p(18,12),6,6','p(18,10),6,4').replace('p(30,12)','p(30,10)').replace('p(42,12),6,6','p(42,10),6,4')
if __name__=='__main__':
 import author
 author.D=D
 keys=sys.argv[1:] or [k for k in D if not json.loads((B/'runs.json').read_text())[k]['valid']]+['cat-head-affection-component','two-opposing-gamepads']
 generate(keys)
