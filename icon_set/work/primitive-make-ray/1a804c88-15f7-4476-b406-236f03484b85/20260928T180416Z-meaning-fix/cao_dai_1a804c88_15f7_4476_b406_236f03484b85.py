"""Restore the eye contour and centred pupil inside the triangular symbol.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The defining almond-shaped Divine Eye was replaced by a small circle.
Construction: eye.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1a804c88-15f7-4476-b406-236f03484b85'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cao-dai/20260928T175901Z-thuan-mac/reference/cao dai_1a804c88-15f7-4476-b406-236f03484b85.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'cao-dai'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cao', 'dai')

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

        poly('triangle',(24,5),(44,42),(4,42),(24,5),closed=True)
        path('eye',(13,28),[C((35,28),(19,18),(29,18)),C((13,28),(29,38),(19,38))],True)
        self.add_dot('pupil',(24,28))


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'The almond-shaped Divine Eye deliberately approaches the triangle sides as in the source. Its contour and pupil are essential to the Cao Dai symbol. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'f2d2e9e287db9c4e5c83dcbf4adb1d671cfce60add8bd239eb786c0603906658'}
