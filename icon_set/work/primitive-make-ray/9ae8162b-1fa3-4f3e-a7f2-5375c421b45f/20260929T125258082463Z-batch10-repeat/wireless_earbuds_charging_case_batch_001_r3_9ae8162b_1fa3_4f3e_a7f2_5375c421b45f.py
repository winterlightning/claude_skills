"""The rejected earbuds were split semicircles with a plain status dot. Restore fuller opposed earbud heads and a charging zigzag inside the rounded case.
Symbol plan: Original earbud case; mirrored earbuds and central charging mark.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9ae8162b-1fa3-4f3e-a7f2-5375c421b45f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wireless-earbuds-charging-case-batch-001-r3/20260929T124732Z-thuan-mac/reference/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'wireless-earbuds-charging-case-batch-001-r3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wireless', 'earbuds', 'charging', 'case', 'batch', '001', 'r3')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('case',(6,28),[('L',(42,28)),('L',(42,34)),('A',(34,42),8,8,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,28))],True)
        path('left-bud',(18,28),[('L',(18,12)),('A',(6,12),6,6,False),('A',(18,12),6,6,False)])
        path('right-bud',(30,28),[('L',(30,12)),('A',(42,12),6,6,True),('A',(30,12),6,6,True)])
        join('left-bud','case');join('right-bud','case')
        poly('charge',(26,32),(22,35),(26,35),(22,38))
