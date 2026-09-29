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

        poly('burst',(6,17),(3,14),(11,14),(8,7),(17,10),(23,3),(27,10),(37,7),(34,14),(44,14),(41,17))
        path('left-car',(20,23),[L((13,23)),L((9,30)),L((6,31)),L((6,40)),L((8,40))])
        poly('left-break',(20,23),(17,29),(23,34),(20,40),(16,40))
        path('right-car',(29,23),[L((35,23)),L((39,30)),C((44,34),(44,30),(44,31)),L((44,40)),L((42,40))])
        poly('right-break',(29,23),(26,29),(32,34),(29,40),(34,40))
        circle('left-wheel',12,40,4);circle('right-wheel',38,40,4)


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'The car must remain one split vehicle under an impact burst; retain its jagged break, two wheels and compact scene proportions. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '41549745f7e6dd1df1c3a56cd502f4e30b1b5b7ec70afce8bd78b94650b0250f'}
