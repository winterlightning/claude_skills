"""The text card lost its rounded corners, clear text strokes and natural thumb/palm curves. Restore a thumb wrapping the card edge, rounded palm and two readable text rules.
Plan: HRECT_L; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide hand-helping: round thumb and coherent curved palm; paired text rules.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ec650a8b-1e1e-43c8-9f94-4878310a6be1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-gripping-text-card/20260929T105027Z-thuan-mac/reference/business card hand 2_ec650a8b-1e1e-43c8-9f94-4878310a6be1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-gripping-text-card'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'gripping', 'text', 'card')

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
        path('card',(20,8),('L',(41,8)),('A',(44,11),3,3,True),('L',(44,29)),('A',(41,32),3,3,True),('L',(36,32)),('L',(23,32)),('A',(20,29),3,3,True),('L',(20,24)))
        path('thumb',(4,20),('C',(12,16),(8,20),(8,16)),('L',(20,16)),('A',(20,24),4,4,True),('L',(16,24)),('C',(10,28),(14,26),(12,28)));join('thumb','card')
        bez('palm',(4,36),((8,36),(8,40),(14,40)),((28,40),(30,40),(36,32)));join('palm','card')
        line('text',(33,20),(35,20))
