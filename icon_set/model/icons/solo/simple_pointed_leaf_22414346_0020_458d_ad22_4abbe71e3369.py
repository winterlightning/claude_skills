"""Simple Pointed Leaf."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22414346-0020-458d-ad22-4abbe71e3369'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hubbard squash_22414346-0020-458d-ad22-4abbe71e3369.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-pointed-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('simple', 'pointed', 'leaf', 'sub icon')

    def build(self):
        # Plan: Broad diagonal pointed leaf with a sweeping central vein continuing above its upper-right tip. Lucide leaf informs the long organic contour and single vein. No secondary veins added.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('leaf',(6,42),[('C',(10,18),(6,32),(6,23)),('C',(36,10),(17,10),(27,6)),('C',(35,32),(40,16),(41,24)),('C',(6,42),(28,42),(15,42))],True)
        path('vein',(6,42),[('C',(36,10),(14,25),(26,18)),('C',(42,6),(39,10),(41,8))]);join('leaf','vein')


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('1157517b-90dd-480d-990d-dd252676e00e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf right_1157517b-90dd-480d-990d-dd252676e00e.svg')]
