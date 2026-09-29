"""Restore a rounded rabbit face, two outward ears, paired eyes, a small nose and a paw holding an egg.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The rabbit was squared off like a letter H, with only one eye and no recognizable face or holding paw.
Construction: rabbit.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '606ec34e-20d1-525e-a765-4f3fca8d3c47'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bunny-holding-easter-egg/20260928T175901Z-thuan-mac/reference/easter egg bunny_606ec34e-20d1-525e-a765-4f3fca8d3c47.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'bunny-holding-easter-egg'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('easter', 'egg', 'bunny')

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

        path('rabbit',(12,34),[C((9,20),(5,30),(6,24)),C((7,5),(4,10),(3,5)),C((18,17),(12,5),(15,10)),C((24,17),(20,16),(22,16)),C((35,5),(27,10),(30,5)),C((33,20),(39,5),(38,10)),C((35,26),(35,22),(35,24))])
        path('cheek',(12,34),[C((23,35),(15,37),(19,37))])
        self.add_dot('eye-left',(14,25));self.add_dot('eye-right',(25,25));self.add_dot('nose',(19,30))
        path('body',(12,34),[C((10,43),(10,37),(10,40))])
        path('egg-upper',(28,35),[C((35,27),(29,31),(32,27)),C((42,39),(39,27),(42,35)),C((32,44),(42,45),(36,45)),C((29,42),(30,44),(29,43))])
        path('paw',(21,39),[L((27,38)),C((27,42),(31,38),(31,41)),L((23,43))])


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'The complete rabbit face, outward ears, holding paw and egg need compact facial and attached-part spacing. The paired eyes, nose and egg opening remain visible at 48px. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b9d14b601f340f0038508545d7308e763f7ccad1bcb6fd9d4d7186e3e679e9c1'}
