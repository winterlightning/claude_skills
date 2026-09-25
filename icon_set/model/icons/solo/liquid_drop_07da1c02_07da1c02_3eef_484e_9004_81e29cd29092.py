"""liquid-drop-07da1c02: Symmetric pointed drop with tangent shoulders flowing into a circular lower bowl; short reflection retained.
Lucide construction: droplet; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '07da1c02-3eef-484e-9004-81e29cd29092'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__liquid-drop-07da1c02/20260924T165054Z-thuan-mac/reference/blood drop_07da1c02-3eef-484e-9004-81e29cd29092.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'liquid-drop-07da1c02-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('liquid', 'drop', '07da1c02')
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

        path('drop',(24,4),[('C',(40,28),(30,13),(40,21)),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('C',(24,4),(8,21),(18,13))],True)
        line('reflection',(29,32),(26,35))
