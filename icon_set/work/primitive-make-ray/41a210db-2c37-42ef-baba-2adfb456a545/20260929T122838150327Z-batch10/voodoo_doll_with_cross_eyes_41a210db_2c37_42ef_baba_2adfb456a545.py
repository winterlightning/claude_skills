"""The rejected voodoo doll was an upright broad-headed ornament with the pin missing. Restore the diagonally tilted sewn doll, cross eyes, and the pin entering from the upper left.
Symbol plan: Original tilted sewn doll; round-ended toy contours and pin; no useful exact Lucide match.
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

        path('doll',(26,23),[('C',(25,13),(24,20),(25,15)),('C',(33,6),(25,9),(28,6)),('C',(42,14),(39,6),(42,8)),('C',(35,23),(42,20),(40,23)),('L',(41,29)),('A',(35,35),4,4,True),('L',(30,30)),('L',(21,42)),('L',(15,37)),('L',(11,40)),('A',(6,34),4,4,True),('L',(18,23)),('L',(12,17)),('A',(18,11),4,4,True),('L',(26,23))],True)
        # One crossed eye preserves the sewn-toy expression at this scale.
        poly('eye-h',(31,14),(33,16),(35,18))
        poly('eye-v',(31,18),(33,16),(35,14));join('eye-h','eye-v')
        circle('pin-head',8,8,2)
        line('pin',(10,10),(20,20));join('pin','pin-head');join('pin','doll')
