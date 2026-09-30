"""The rejected ballot and hand merge into an abstract angular symbol. Restore a clearly tilted sheet entering a box with a curved gripping thumb and back of hand.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide hand-helping: rounded thumb around a tilted ballot, broad ballot box below.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '060b8775-d227-46ed-8367-77a66c4a5282'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-inserting-tilted-ballot-into-box/20260929T105027Z-thuan-mac/reference/election ballot box 2_060b8775-d227-46ed-8367-77a66c4a5282.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-inserting-tilted-ballot-into-box'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'inserting', 'tilted', 'ballot', 'into', 'box')

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
        poly('box',(6,30),(22,30),(42,30),(42,42),(6,42),closed=True)
        poly('paper',(22,30),(6,14),(14,6),(23,15));join('paper','box')
        path('thumb',(42,22),('L',(35,22)),('L',(29,22)),('A',(29,14),4,4,True),('L',(36,14)))
        line('paper-right',(35,22),(22,30));join('paper-right','thumb');join('paper-right','box')
        bez('hand-back',(23,15),((27,7),(32,6),(42,9)));join('hand-back','paper')
