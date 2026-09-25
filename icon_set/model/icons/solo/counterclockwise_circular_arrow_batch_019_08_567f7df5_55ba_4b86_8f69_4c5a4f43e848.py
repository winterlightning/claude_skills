"""counterclockwise-circular-arrow-batch-019-08: A single smooth near-circular counterclockwise orbit ends in a balanced downward V head; lower-left opening retained.
Lucide construction: rotate-ccw; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '567f7df5-55ba-4b86-8f69-4c5a4f43e848'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/go backward_567f7df5-55ba-4b86-8f69-4c5a4f43e848.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'counterclockwise-circular-arrow-batch-019-08'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('counterclockwise', 'circular', 'arrow', 'batch', '019', '08')
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

        path('orbit',(27,42),[('A',(42,24),15,18,False),('A',(27,6),15,18,False),('A',(12,24),15,18,False)])
        poly('head',(6,18),(12,24),(18,18));join('orbit','head')
