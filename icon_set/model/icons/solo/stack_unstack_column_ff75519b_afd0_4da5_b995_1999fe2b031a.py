"""stack-unstack-column: Five repeated square cells descend in three staggered columns; two smooth return arrows repeat alongside them.
Lucide construction: blocks; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ff75519b-afd0-4da5-b995-1999fe2b031a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stack-unstack-column/20260924T171114Z-thuan-mac/reference/stack unstack column_ff75519b-afd0-4da5-b995-1999fe2b031a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'stack-unstack-column'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('stack', 'unstack', 'column')
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

        # Single boundary and dividers: no duplicated cell edges.
        poly('stack',(8,4),(16,4),(16,20),(20,20),(20,36),(24,36),(24,44),(16,44),(16,36),(12,36),(12,20),(8,20),closed=True)
        for name,a,b in [('first',(8,12),(16,12)),('second',(12,28),(20,28)),('join-first',(12,20),(16,20)),('join-second',(16,36),(20,36))]:
            line(name,a,b);join(name,'stack')
        path('turn-upper',(25,4),[('C',(40,11),(34,4),(40,6)),('C',(28,18),(40,16),(34,18))])
        poly('head-upper',(32,14),(28,18),(32,22));join('turn-upper','head-upper')
        path('turn-lower',(33,31),[('C',(40,37),(37,31),(40,33)),('C',(33,42),(40,40),(37,42))])
        poly('head-lower',(37,38),(33,42),(39,44));join('turn-lower','head-lower')
