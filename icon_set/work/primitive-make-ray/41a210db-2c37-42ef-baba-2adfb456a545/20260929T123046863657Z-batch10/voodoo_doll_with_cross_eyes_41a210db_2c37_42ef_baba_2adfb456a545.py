"""The rejected doll had a huge horizontal head and tiny pointed feet, and lost the pin. Rebalance the round sewn head over a larger outstretched body and restore a left-side pin; retain cross eyes.
Symbol plan: Original sewn doll; two small crossed eyes, larger round-ended limbs and a pin simplified to its shaft.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '41a210db-2c37-42ef-baba-2adfb456a545'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__voodoo-doll-with-cross-eyes/20260929T122443Z-thuan-mac/reference/voodoo doll_41a210db-2c37-42ef-baba-2adfb456a545.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'voodoo-doll-with-cross-eyes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('voodoo', 'doll', 'with', 'cross', 'eyes')

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

        path('doll',(14,26),[('C',(8,16),(8,25),(8,21)),('A',(24,6),16,10,True),('A',(40,16),16,10,True),('C',(34,26),(40,21),(40,25)),('L',(42,30)),('L',(34,34)),('L',(34,42)),('L',(24,36)),('L',(14,42)),('L',(14,34)),('L',(6,30)),('L',(14,26))],True)
        for x in (18,30):
         poly(f'eye-{x}-a',(x-1,15),(x,16),(x+1,17))
         poly(f'eye-{x}-b',(x-1,17),(x,16),(x+1,15));join(f'eye-{x}-a',f'eye-{x}-b')
        line('pin',(6,18),(14,26));join('pin','doll')
