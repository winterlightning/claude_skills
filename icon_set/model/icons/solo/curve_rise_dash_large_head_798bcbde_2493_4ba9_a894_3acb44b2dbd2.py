"""curve-rise-dash-large-head: Three coherent dashed curves lead to a vertical arrow; intentionally asymmetric winding trajectory.
Lucide construction: move-up-right; original and atomic-debug inspected.
Omissions: Short dash count reduced to preserve clean visible gaps.
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '798bcbde-2493-4ba9-a894-3acb44b2dbd2'
SOURCE_PATH = 'pictographic-primitives/arrows/curve rise dash large head_798bcbde-2493-4ba9-a894-3acb44b2dbd2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curve-rise-dash-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('curve', 'rise', 'dash', 'large', 'head')
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

        path('start',(4,12),[('C',(12,14),(7,10),(10,11))])
        path('middle',(17,23),[('C',(18,31),(17,25),(17,28))])
        path('bend',(25,39),[('C',(29,40),(26,40),(27,40)),('C',(38,30),(35,40),(38,36))])
        line('shaft',(38,21),(38,8))
        poly('head',(32,14),(38,8),(44,14));join('shaft','head')
