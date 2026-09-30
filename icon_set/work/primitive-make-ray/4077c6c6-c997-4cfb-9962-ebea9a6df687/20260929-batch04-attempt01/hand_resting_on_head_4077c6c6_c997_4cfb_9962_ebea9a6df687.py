"""The rejected hand is a wedge and shoulders are angular. Restore a rounded patting hand, circular face and smooth broad shoulders.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Shared human user.svg: circular jaw and smooth shoulders; Lucide hand-helping for patting hand.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4077c6c6-c997-4cfb-9962-ebea9a6df687'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-resting-on-head/20260929T105027Z-thuan-mac/reference/pat_4077c6c6-c997-4cfb-9962-ebea9a6df687.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-resting-on-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'resting', 'on', 'head')
    human_construction = "bust"

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
        path('face',(14,20),('L',(14,22)),('A',(34,22),10,10,False),('L',(34,20)))
        path('shoulders',(6,42),('C',(16,36),(6,39),(11,36)),('L',(32,36)),('C',(42,42),(37,36),(42,39)))
        join('face','shoulders')
        path('hand',(42,6),('L',(27,6)),('C',(10,12),(22,7),(15,10)),('A',(14,20),5,5,False),('L',(22,18)),('C',(34,20),(24,21),(30,21)),('L',(42,20)));join('hand','face')
