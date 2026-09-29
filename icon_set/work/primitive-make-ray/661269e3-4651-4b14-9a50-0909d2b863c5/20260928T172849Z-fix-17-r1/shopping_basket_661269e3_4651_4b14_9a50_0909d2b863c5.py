"""Mirrored basket handles, a straight rim and evenly spaced interior slots.
Reference comparison: Current basket has a bowed/kinked rim and unequal bottom corners. Use a straight rim, mirrored tapered walls and equal handles and slots.
Construction reference: Lucide wallet: coherent rounded enclosure.
SOLO48 keyshape HRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='661269e3-4651-4b14-9a50-0909d2b863c5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__shopping-basket/20260928T172849Z-thuan-mac/reference/shopping basket_661269e3-4651-4b14-9a50-0909d2b863c5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='shopping-basket'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('shopping', 'basket')

    def build(self):

        # Typed path helpers own continuous contours, repeated radii and real junctions.
        def path(name,start,commands,closed=False):
            here=start;members=[]
            for i,c in enumerate(commands):
                kind,end,*args=c; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C':
                    c1,c2=args
                    self.add_bezier(ident,here,(c1,c2,end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('basket',(4,21),[('L',(44,21)),('L',(38,37)),('C',(34,40),(37,40),(36,40)),('L',(14,40)),('C',(10,37),(12,40),(11,40)),('L',(4,21))],True)
        line('left-handle',(10,21),(16,8));line('right-handle',(38,21),(32,8));join('basket','left-handle');join('basket','right-handle')
        line('left-slot',(19,29),(19,32));line('right-slot',(29,29),(29,32))
