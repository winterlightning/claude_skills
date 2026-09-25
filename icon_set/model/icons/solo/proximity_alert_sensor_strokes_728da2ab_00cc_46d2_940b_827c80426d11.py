"""proximity-alert-sensor-strokes: The source contains only three separated sensor marks; reconstruct those as exact straight runs with the same directions and arrangement.
Lucide construction: radar; original and atomic-debug inspected.
Omissions: None; intentionally sparse reference preserved.
Keyshape HRECT_M: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '728da2ab-00cc-46d2-940b-827c80426d11'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__proximity-alert-sensor-strokes/20260924T171114Z-thuan-mac/reference/audi pre sense warning_728da2ab-00cc-46d2-940b-827c80426d11.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'proximity-alert-sensor-strokes'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('proximity', 'alert', 'sensor', 'strokes')
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

        line('left',(4,14),(4,38))
        line('top',(22,10),(28,10))
        line('right',(38,21),(44,25))
