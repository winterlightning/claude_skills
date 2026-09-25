"""curved-saxophone: U-shaped saxophone tube; nested circular bowls and tangent straight sides; diagonal bell remains asymmetric.
Lucide construction: music; original and atomic-debug inspected.
Omissions: Tiny key ticks omitted for tube clearance.
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b1bdd1e-b98f-4cd3-8970-9fc4e618a5e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/instrument saxophone_5b1bdd1e-b98f-4cd3-8970-9fc4e618a5e9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curved-saxophone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curved', 'saxophone')
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

        path('sax',(8,4),[('A',(22,18),14,14,True),('L',(22,30)),('A',(32,30),5,5,False),('L',(32,16)),('L',(40,24)),('L',(40,30)),('A',(12,30),14,14,True),('L',(12,12))])
