"""Restore a rounded nose, diagonal fuselage, wing and tail, with a separate flame and two smoke wisps.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The aircraft became a jagged lightning shape and the fire merged into it.
Construction: plane.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '81f5c526-61a1-4426-afae-2fec80a31cb2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__burning-crashed-aircraft/20260928T175901Z-thuan-mac/reference/plane crashed_81f5c526-61a1-4426-afae-2fec80a31cb2.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'burning-crashed-aircraft'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('plane', 'crashed')

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

        path('plane',(8,24),[L((14,27)),L((14,31)),L((36,40)),C((41,35),(43,41),(45,37)),L((31,30)),L((24,19)),L((19,17)),L((20,27)),L((11,23)),L((8,16)),L((6,15)),L((6,22)),C((8,24),(6,23),(7,24))],True)
        path('wing',(20,32),[L((8,40)),L((13,43)),L((29,36))])
        path('flame',(34,24),[C((31,14),(28,22),(31,18)),C((36,7),(35,17),(38,12)),C((42,25),(42,14),(46,20))])
        path('smoke-one',(8,8),[C((9,4),(5,6),(10,6))])
        path('smoke-two',(18,9),[C((19,4),(15,7),(20,6))])
