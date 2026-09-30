"""The rejected lowering hand is a narrow two-line strip and a diamond. Restore a broad curved hand around a diagonal ballot and a separate horizontal slot.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide hand-helping: curving grasp and rounded palm; diagonal paper over a slot.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6dec0eec-6a7b-45e6-8bf4-6d2af8987802'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-lowering-diagonal-ballot-toward-slot/20260929T105027Z-thuan-mac/reference/election ballot box 1_6dec0eec-6a7b-45e6-8bf4-6d2af8987802.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-lowering-diagonal-ballot-toward-slot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'lowering', 'diagonal', 'ballot', 'toward', 'slot')

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
        poly('paper',(18,16),(6,28),(20,42),(36,26),(30,20))
        path('hand',(32,6),('C',(18,16),(25,11),(21,12)),('A',(24,24),5,5,False),('L',(30,20)),('C',(42,14),(35,22),(36,18)));join('paper','hand')
        poly('slot',(6,42),(20,42),(38,42));join('slot','paper')
