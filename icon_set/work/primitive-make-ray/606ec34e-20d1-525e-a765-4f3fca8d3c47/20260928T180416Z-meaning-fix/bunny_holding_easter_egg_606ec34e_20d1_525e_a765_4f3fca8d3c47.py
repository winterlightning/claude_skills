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

        path('rabbit',(12,34),[C((9,20),(5,30),(6,24)),C((8,6),(4,11),(4,3)),C((18,17),(12,3),(15,9)),C((24,17),(20,16),(22,16)),C((34,6),(28,6),(32,3)),C((33,20),(38,3),(39,10)),C((35,26),(35,22),(36,24))])
        path('cheek',(12,34),[C((24,35),(16,38),(21,37))])
        self.add_dot('eye-left',(14,25));self.add_dot('eye-right',(25,25));self.add_dot('nose',(19,30))
        path('body',(12,34),[C((10,44),(10,38),(10,40))])
        path('egg',(35,27),[C((42,39),(39,27),(42,35)),C((28,40),(42,47),(30,47)),C((35,27),(26,35),(31,27))],True)
        path('paw',(21,39),[L((27,38)),C((29,41),(30,37),(31,40)),L((23,43))])
