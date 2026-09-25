"""key-shaped-blank-solo-b017: Toothless key blank with a circular bow and diagonal broad shaft; the bow transitions mirror across the shaft axis and the tiny center dot is retained.
Lucide construction: key-round; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0f0a99d8-5904-46c1-950e-8134fc37ff93'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/key 2_0f0a99d8-5904-46c1-950e-8134fc37ff93.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'key-shaped-blank-solo-b017'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/everyday'
    aliases = ()
    keywords = ('key', 'shaped', 'blank', 'solo', 'b017')
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

        path('key',(21,19),[('L',(34,6)),('L',(42,6)),('L',(42,14)),('L',(29,27)),('C',(30,30),(30,28),(30,29)),('A',(18,42),12,12,True),('A',(6,30),12,12,True),('A',(18,18),12,12,True),('C',(21,19),(19,18),(20,18))],True)
        self.add_dot('bow-dot',(18,30))
