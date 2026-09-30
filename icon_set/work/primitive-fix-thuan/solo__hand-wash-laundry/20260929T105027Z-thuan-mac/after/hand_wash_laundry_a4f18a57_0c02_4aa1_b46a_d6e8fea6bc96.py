"""The rejected hand is an angular bracket above a basin. Restore recognizably descending fingers above a wave and tub.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide hand: rounded finger tips; shared series creates calm water waves.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a4f18a57-0c02-4aa1-b46a-d6e8fea6bc96'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-wash-laundry/20260929T105027Z-thuan-mac/reference/laundry hand wash_a4f18a57-0c02-4aa1-b46a-d6e8fea6bc96.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-wash-laundry'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'wash', 'laundry')

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
        path('hand',(10,6),('L',(10,17)),('A',(18,17),4,4,False),('L',(18,10)),('L',(26,10)),('L',(26,17)),('A',(34,17),4,4,False),('L',(34,13)),('L',(42,13)))
        path('basin',(6,32),('L',(10,42)),('L',(38,42)),('L',(42,32)))
        path('water',(6,32),('A',(18,32),6,2,False),('A',(30,32),6,2,True),('A',(42,32),6,2,False));join('water','basin')
