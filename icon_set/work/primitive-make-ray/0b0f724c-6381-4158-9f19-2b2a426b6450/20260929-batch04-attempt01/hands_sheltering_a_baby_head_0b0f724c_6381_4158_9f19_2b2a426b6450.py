"""The rejected protecting hands are a roof over an unmarked ring. Restore curved fingers and wrists around a baby head with a hair cue.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Shared circular baby head and hair curl; Lucide hand-helping for rounded fingertip/hand curves.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0b0f724c-6381-4158-9f19-2b2a426b6450'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-sheltering-a-baby-head/20260929T105027Z-thuan-mac/reference/baby guard protect 2_0b0f724c-6381-4158-9f19-2b2a426b6450.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-sheltering-a-baby-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hands', 'sheltering', 'a', 'baby', 'head')

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
        circle('baby',24,32,10)
        bez('curl',(24,22),((26,24),(25,27),(23,27)));join('curl','baby')
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            path(f'hand-{side}',p(18,26),('C',p(15,14),p(17,22),p(18,18)),('L',p(5,6)),('C',p(7,13),p(1,8),p(4,10)))
