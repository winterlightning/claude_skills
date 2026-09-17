"""Round Bitten Cookie."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae992af4-2c81-5b7b-895c-bfe6592e342a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cookie_ae992af4-2c81-5b7b-895c-bfe6592e342a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-bitten-cookie'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('round', 'bitten', 'cookie')

    def build(self):
        # Plan: Lucide cookie: large circular outline interrupted by two inward bites. Plain face retained exactly as the supplied reference.
        # Envelope: CIRCLE; visible ink (2, 2, 46, 46) on SOLO48.

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

        path('cookie',(24,4),[('A',(4,24),20,20,False),('A',(24,44),20,20,False),('A',(44,24),20,20,False),('A',(34,14),10,10,True),('A',(24,4),10,10,True)],True)
