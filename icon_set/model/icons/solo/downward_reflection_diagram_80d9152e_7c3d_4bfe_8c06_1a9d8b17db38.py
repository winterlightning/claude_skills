"""downward-reflection-diagram: Mirrored open triangles face a horizontal axis; a semicircular arrow expresses downward reflection.
Lucide construction: flip-vertical-2; original and atomic-debug inspected.
Omissions: None
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80d9152e-7c3d-4bfe-8c06-1a9d8b17db38'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/reflect down_80d9152e-7c3d-4bfe-8c06-1a9d8b17db38.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'downward-reflection-diagram'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('downward', 'reflection', 'diagram')
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

        poly('upper',(4,8),(24,8),(14,16),closed=True)
        poly('lower',(4,40),(24,40),(14,32),closed=True)
        line('axis',(4,24),(24,24))
        path('turn',(34,12),[('A',(44,24),10,12,True),('A',(34,36),10,12,True)])
        poly('head',(34,28),(34,36),(42,36));join('head','turn')
