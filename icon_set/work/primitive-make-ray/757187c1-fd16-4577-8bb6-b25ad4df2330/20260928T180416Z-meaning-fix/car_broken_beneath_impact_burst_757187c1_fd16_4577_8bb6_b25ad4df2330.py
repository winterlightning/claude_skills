"""Restore an open sharp impact burst above one car split by a central zigzag break, with two circular wheels.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The impact became a closed badge and the car halves looked like two separate small cars.
Construction: car.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '757187c1-fd16-4577-8bb6-b25ad4df2330'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-broken-beneath-impact-burst/20260928T175901Z-thuan-mac/reference/car explode_757187c1-fd16-4577-8bb6-b25ad4df2330.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'car-broken-beneath-impact-burst'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('car', 'explode')

    def build(self):

        def path(name,start,commands,closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(commands):
                if end==here and kind=='L':continue
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        L=lambda end:('L',end)
        C=lambda end,c1,c2:('C',end,c1,c2)
        A=lambda end,rx,ry,sweep:('A',end,rx,ry,sweep)
        line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('burst',(6,23),(3,19),(11,19),(8,10),(17,14),(23,4),(27,14),(37,9),(34,19),(44,19),(41,23))
        path('left-car',(21,27),[L((14,27)),L((9,34)),L((6,35)),L((6,41)),L((8,41))])
        poly('left-break',(21,27),(18,33),(24,37),(20,44),(16,44))
        path('right-car',(29,27),[L((35,27)),L((39,34)),C((44,38),(44,34),(44,35)),L((44,41)),L((42,41))])
        poly('right-break',(29,27),(26,33),(32,37),(28,44),(34,44))
        circle('left-wheel',12,42,4);circle('right-wheel',38,42,4)
