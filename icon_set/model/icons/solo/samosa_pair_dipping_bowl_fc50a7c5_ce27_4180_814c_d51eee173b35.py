"""Samosas with Dipping Bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc50a7c5-ce27-4180-814c-d51eee173b35'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/salmosa_fc50a7c5-ce27-4180-814c-d51eee173b35.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'samosa-pair-dipping-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('samosa', 'pair', 'dipping', 'bowl')

    def build(self):
        # Plan: Two triangular samosas step diagonally beside a lower-left sauce bowl. Repeated triangular construction preserves the pair; fine corner rounding and oval bowl rim simplified. No useful exact Lucide match.
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

        poly('back-samosa',(6,24),(16,6),(24,24),closed=True)
        poly('front-samosa',(24,42),(34,24),(42,42),closed=True)
        path('dip',(6,33),[('L',(18,33)),('A',(6,33),6,9,True)],True)
