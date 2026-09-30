"""The rejected water protection icon resembles a diamond stand with a tiny drop. Restore larger droplet and two distinct cupped hands.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide hand-helping: two mirrored cupped hands; larger teardrop with a round base.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e4877261-473e-44ea-bd3c-dbd7199f163e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-protecting-water/20260929T105027Z-thuan-mac/reference/water protection drop hold_e4877261-473e-44ea-bd3c-dbd7199f163e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-protecting-water'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hands', 'protecting', 'water')

    def build(self):

        def path(n,start,*commands,closed=False):
            here=start; members=[]
            for j,cmd in enumerate(commands):
                k=f'{n}-{j}';kind,end,*args=cmd
                if kind=='L': self.add_line(k,here,end)
                elif kind=='A': self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def bez(n,a,*parts):self.add_bezier(n,a,*parts)
        def arc(n,a,b,r,ry=None,s=True):self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(a,b):self.relate('connect',a,b)
        def rect(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        path('drop',(24,6),('C',(18,18),(22,10),(18,14)),('A',(30,18),6,6,False),('C',(24,6),(30,14),(26,10)),closed=True)
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            path(f'hand-{side}',p(18,42),('L',p(18,30)),('A',p(10,30),4,4,side<0),('L',p(10,34)),('C',p(4,42),p(10,37),p(6,38)))
