"""Rejected spoon is a long angular trough and cubes are oversized. Restore a rounded deep bowl at left with a narrow handle, under a compact three-cube stack.
Plan: SQUARE envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5ff5b62c-7e8c-4295-9a82-60061ddaee94'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__three-sugar-cubes-above-deep-spoon/20260929T130116Z-thuan-mac/reference/drinks extra add sugar_5ff5b62c-7e8c-4295-9a82-60061ddaee94.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='three-sugar-cubes-above-deep-spoon'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('drinks', 'extra', 'add', 'sugar')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        def box(name,l,t,r,b,rad=0):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:
                path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        self.add_polyline('cubes',(6,22),(6,14),(14,14),(14,6),(22,6),(22,14),(30,14),(30,22),(6,22),closed=True)
        self.add_line('top-base',(14,14),(22,14));join('top-base','cubes')
        self.add_line('divider',(18,14),(18,22));join('divider','cubes');join('divider','top-base')
        path('bowl',(6,34),[('A',(28,34),11,4,True),('A',(6,34),11,8,True)],True)
        self.add_line('handle',(28,34),(42,34));join('handle','bowl')
