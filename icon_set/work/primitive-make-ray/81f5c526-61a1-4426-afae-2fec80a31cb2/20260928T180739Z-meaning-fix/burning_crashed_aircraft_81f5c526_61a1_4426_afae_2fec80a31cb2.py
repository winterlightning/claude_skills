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

        path('plane',(9,20),[L((15,23)),L((15,29)),L((22,32)),L((9,40)),L((14,43)),L((30,36)),L((38,40)),C((41,34),(44,43),(46,37)),L((18,24)),L((14,16)),L((9,14)),L((9,20))],True)
        path('flame',(32,26),[C((30,16),(26,23),(29,20)),C((35,8),(34,19),(37,14)),C((42,25),(41,14),(45,20))])
        path('smoke-one',(5,10),[C((6,4),(2,8),(7,7))])
        path('smoke-two',(17,10),[C((18,4),(14,8),(19,7))])
