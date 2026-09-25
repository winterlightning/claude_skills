"""hand-swipe-up-gesture-solo: A side-facing hand with rounded index fingertip and raised thumb sits beneath an upward arrow. Hand anatomy follows the original; shared human-reference guide reviewed; no detached head/body.
Lucide construction: hand; original and atomic-debug inspected.
Omissions: Small palm folds omitted.
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '244a7f4d-148d-4ae8-9b10-c840685823e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-swipe-up-gesture-solo/20260924T171114Z-thuan-mac/reference/gesture swipe vertical up 3_244a7f4d-148d-4ae8-9b10-c840685823e9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'hand-swipe-up-gesture-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hand', 'swipe', 'up', 'gesture', 'solo')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('hand',(4,38),[('L',(4,30)),('C',(7,27),(4,29),(5,28)),('L',(20,22)),('C',(25,24),(23,22),(25,22)),('C',(22,28),(25,26),(23,27)),('L',(40,28)),('A',(40,36),4,4,True),('L',(28,36)),('C',(25,40),(26,36),(27,40)),('L',(7,40)),('A',(4,38),3,2,True)],True)
        poly('arrowhead',(18,14),(24,8),(30,14));line('shaft',(24,8),(24,14));join('shaft','arrowhead')
