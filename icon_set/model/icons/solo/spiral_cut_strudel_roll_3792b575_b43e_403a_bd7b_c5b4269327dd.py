"""spiral-cut-strudel-roll: The pastry cross-section is a continuous spiral with tangent quarter-circle corners; a diagonal back surface preserves depth.
Lucide construction: cylinder; original and atomic-debug inspected.
Omissions: One clear spiral turn retained instead of closely nested turns.
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3792b575-b43e-403a-bd7b-c5b4269327dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/strudel_3792b575-b43e-403a-bd7b-c5b4269327dd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'spiral-cut-strudel-roll'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('spiral', 'cut', 'strudel', 'roll')
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

        path('spiral',(16,30),[('L',(20,30)),('A',(24,26),4,4,False),('L',(24,24)),('A',(16,16),8,8,False),('L',(14,16)),('A',(6,24),8,8,False),('L',(6,34)),('A',(14,42),8,8,False),('L',(26,42)),('A',(34,34),8,8,False),('L',(34,24))])
        path('back',(14,16),[('L',(24,6)),('L',(34,6)),('A',(42,14),8,8,True),('C',(40,18),(42,16),(41,17)),('L',(34,24))]);join('back','spiral')
