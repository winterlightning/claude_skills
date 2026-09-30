"""The identity card is square, the portrait a dot and the supporting hand an abstract loop. Restore rounded card, circular portrait, text rule and a natural supporting thumb/palm.
Plan: VRECT_L; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide hand-helping: curved palm and thumb, rounded card with circular identity mark.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0369547d-4203-4fc3-ae0f-00ab63619bad'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-presenting-identity-card/20260929T105027Z-thuan-mac/reference/business card hand 1_0369547d-4203-4fc3-ae0f-00ab63619bad.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-presenting-identity-card'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'presenting', 'identity', 'card')

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
        path('card',(19,4),('L',(37,4)),('A',(40,7),3,3,True),('L',(40,33)),('A',(37,36),3,3,True),('L',(26,36)),('L',(19,36)),('A',(16,33),3,3,True),('L',(16,30)),('L',(16,7)),('A',(19,4),3,3,True),closed=True)
        circle('portrait',28,15,2)
        line('text',(25,26),(31,26))
        path('hand',(16,30),('C',(10,22),(12,30),(14,20)),('C',(8,28),(8,22),(8,24)),('C',(14,44),(8,36),(9,44)),('L',(18,44)),('A',(26,36),8,8,False));join('hand','card')
