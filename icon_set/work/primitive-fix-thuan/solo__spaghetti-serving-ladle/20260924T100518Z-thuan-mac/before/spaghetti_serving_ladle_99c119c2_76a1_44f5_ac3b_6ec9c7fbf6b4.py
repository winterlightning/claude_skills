"""Spaghetti Serving Ladle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99c119c2-76a1-44f5-ac3b-6ec9c7fbf6b4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ladle spaghetti_99c119c2-76a1-44f5-ac3b-6ec9c7fbf6b4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spaghetti-serving-ladle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('spaghetti', 'serving', 'ladle')

    def build(self):
        # Plan: Hook-handled ladle with a deep round bowl and a single generous pasta loop draped over the rim. Lucide cooking-pot informs bowl/rim structure; repeated pasta loops reduced to one.
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

        path('handle',(6,12),[('A',(18,12),6,6,True),('L',(18,26))])
        path('bowl',(18,26),[('L',(30,26)),('L',(40,26)),('L',(42,26)),('A',(30,38),12,12,True),('A',(18,26),12,12,True)],True);join('handle','bowl')
        path('pasta',(30,42),[('L',(30,21)),('A',(40,21),5,5,True),('L',(40,26))]);join('pasta','bowl')
