"""Steamed Bao Buns."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ac87097-22b4-467e-8616-be55a6c4ad10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/exotic food buns_4ac87097-22b4-467e-8616-be55a6c4ad10.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steamed-bao-bun-group'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('steamed', 'bao', 'bun', 'group')

    def build(self):
        # Plan: Three rounded folded bao buns in an irregular stack. Two left buns share a seam and one sits to the right; pointed dough notches identify the folded tops. Diagonal tilt simplified for clear separation. No useful exact Lucide match.
        # Envelope: HRECT_L; visible ink (2, 6, 46, 42) on SOLO48.

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

        path('left-upper',(8,8),[('L',(14,8)),('L',(18,14)),('L',(22,8)),('A',(26,12),4,4,True),('L',(26,24)),('L',(8,24)),('A',(4,20),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
        path('left-lower',(8,24),[('L',(8,36)),('A',(12,40),4,4,False),('L',(22,40)),('A',(26,36),4,4,False),('L',(26,24))]);join('left-lower','left-upper')
        path('right',(26,24),[('L',(30,18)),('L',(34,24)),('L',(40,20)),('A',(44,24),4,4,True),('L',(44,32)),('A',(40,36),4,4,True),('L',(26,36))]);join('right','left-upper');join('right','left-lower')
