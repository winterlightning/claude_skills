"""Suitcase lost its marking and tiny solid wheels; restore one clear case mark and hollow wheels.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: luggage: rounded case and paired wheels
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f459a46b-5237-46ac-a92e-22dd7641c816'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-wheel-cart-with-a-marked-suitcase/20260929T131521Z-thuan-mac/reference/baggage cart 2_f459a46b-5237-46ac-a92e-22dd7641c816.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-wheel-cart-with-a-marked-suitcase'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'wheel', 'cart', 'with', 'a', 'marked', 'suitcase')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('cart',(6,6),[('A',(14,14),8,8,True),('L',(14,26)),('A',(18,30),4,4,False),('L',(42,30))])
        path('case',(22,30),[('L',(22,18)),('A',(26,14),4,4,True),('L',(38,14)),('A',(42,18),4,4,True),('L',(42,30))]);join('case','cart')
        poly('handle',(26,14),(26,6),(38,6),(38,14));join('handle','case')
        line('mark',(31,22),(33,22))
        for x in (18,38):oval(f'wheel{x}',x,40,2,2)
