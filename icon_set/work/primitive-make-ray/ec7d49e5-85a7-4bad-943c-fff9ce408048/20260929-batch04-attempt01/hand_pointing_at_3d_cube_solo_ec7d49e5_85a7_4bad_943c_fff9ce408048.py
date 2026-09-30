"""The pointing hand became a small hook and the cube lost its open lower-left reference arrangement. Restore an extended index finger and broad palm below a clear perspective cube.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide hand: round finger tip and broad palm; exact shared cube vertices.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ec7d49e5-85a7-4bad-943c-fff9ce408048'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-at-3d-cube-solo/20260929T105027Z-thuan-mac/reference/hand point cube_ec7d49e5-85a7-4bad-943c-fff9ce408048.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-pointing-at-3d-cube-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'pointing', 'at', '3d', 'cube', 'solo')

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
        poly('cube',(24,11),(33,6),(42,11),(42,22),(33,27),(33,16),(24,11),(24,20))
        line('ridge',(33,16),(42,11));join('ridge','cube')
        path('hand',(6,39),('L',(6,35)),('A',(10,35),2,2,True),('L',(10,26)),('A',(18,26),4,4,True),('L',(18,36)),('C',(26,42),(24,36),(26,38)))
