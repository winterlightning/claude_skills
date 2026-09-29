"""Restore three nested sweeping banana contours, blunt curved tips, and their shared upright stalk.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: Straight triangular wedges replaced the rounded banana fruits.
Construction: banana.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '01dfab52-1214-532b-8f84-ea5dce7a2998'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bunch-of-bananas-batch-010-10/20260928T175901Z-thuan-mac/reference/banana_01dfab52-1214-532b-8f84-ea5dce7a2998.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'bunch-of-bananas-batch-010-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('banana',)

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

        path('outer',(31,6),[L((37,6)),L((37,12)),C((43,28),(42,16),(45,23)),C((22,42),(40,37),(30,44)),C((16,39),(19,42),(17,41)),C((32,13),(30,33),(35,23)),L((31,6))],True)
        path('middle',(32,13),[C((8,32),(30,29),(19,34)),C((16,39),(9,37),(12,39))])
        path('upper',(32,13),[C((6,23),(26,25),(15,26)),C((8,32),(4,27),(6,30))])


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'Three curved bananas must converge at their shared stalk. Preserve the smooth fan and tapered fruit contours rather than triangular wedges. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ddd1bfc1906adf8249e4ada7fc31eb3159ce0e090b22105d4d379f040d808f74'}
