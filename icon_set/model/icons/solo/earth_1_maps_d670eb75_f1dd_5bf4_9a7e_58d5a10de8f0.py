"""earth-1-maps: Circular rim with smooth west and east continent boundaries, split at exact rim attachments. Geographic asymmetry retained.
Lucide construction: earth; original and atomic-debug inspected.
Omissions: Fine coastline detail omitted while keeping the three land boundaries.
Keyshape CIRCLE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd670eb75-f1dd-5bf4-9a7e-58d5a10de8f0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__earth-1-maps/20260924T165054Z-thuan-mac/reference/earth 1_d670eb75-f1dd-5bf4-9a7e-58d5a10de8f0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'earth-1-maps-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    categories = ('maps', 'primitives')
    aliases = ()
    keywords = ('earth', '1', 'maps')
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

        path('rim',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        path('north',(24,4),[('C',(18,16),(24,11),(23,14)),('C',(4,24),(13,18),(7,18))])
        path('south',(4,24),[('C',(20,30),(11,24),(20,24)),('C',(12,40),(20,34),(12,35))])
        path('east',(36,8),[('C',(31,20),(32,12),(31,16)),('C',(44,24),(31,25),(38,24))])
        for part in ['north','south','east']:join(part,'rim')
        join('north','south')
