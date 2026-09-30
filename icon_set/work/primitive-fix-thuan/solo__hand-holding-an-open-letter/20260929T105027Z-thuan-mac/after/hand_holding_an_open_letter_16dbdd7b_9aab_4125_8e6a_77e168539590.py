"""The rejected open letter lacks the envelope flap and visible message line and barely reads as a hand. Restore a paper sheet above an envelope and a rounded thumb at its right edge.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide book-open and hand-helping: paper planes and a rounded grasp. Asymmetric holding hand.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '16dbdd7b-9aab-4125-8e6a-77e168539590'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-an-open-letter/20260929T105027Z-thuan-mac/reference/read email hand_16dbdd7b-9aab-4125-8e6a-77e168539590.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-an-open-letter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'holding', 'an', 'open', 'letter')

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
        poly('paper',(6,22),(6,6),(30,6),(30,22))
        line('message',(15,15),(21,15))
        poly('envelope',(6,22),(6,38),(17,38))
        path('fold',(6,22),('L',(16,28)),('C',(24,28),(19,30),(21,30)),('L',(30,22)))
        join('paper','envelope');join('fold','paper');join('fold','envelope')
        path('hand',(42,42),('C',(38,32),(38,38),(38,35)),('L',(38,21)),('C',(30,14),(38,18),(34,15)),('L',(30,22)),('L',(25,27)),('A',(25,35),4,4,False),('C',(30,42),(28,38),(27,40)))
        join('hand','paper');join('hand','fold')
