"""flatboat-with-deck-cabin: Symmetric shallow hull with tangent rounded bilge corners and a plain rectangular deck cabin.
Lucide construction: ship; original and atomic-debug inspected.
Omissions: None
Keyshape HRECT_M: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee2a0599-4ac3-4352-a6e1-46843babfafa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flatboat_ee2a0599-4ac3-4352-a6e1-46843babfafa.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'flatboat-with-deck-cabin'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('flatboat', 'with', 'deck', 'cabin')
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

        path('hull',(4,26),[('L',(14,26)),('L',(34,26)),('L',(44,26)),('L',(41,34)),('C',(35,38),(40,37),(38,38)),('L',(13,38)),('C',(7,34),(10,38),(8,37)),('L',(4,26))],True)
        poly('cabin',(14,26),(14,10),(34,10),(34,26));join('cabin','hull')
