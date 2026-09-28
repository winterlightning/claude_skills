"""Steamed Chinese Dim Sum Dumpling."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8496c4d1-f3a3-5211-b8f3-e720e38ca603'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/dimsum chinese dumpling_8496c4d1-f3a3-5211-b8f3-e720e38ca603.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chinese-dim-sum-dumpling'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('chinese', 'dim', 'sum', 'dumpling')

    def build(self):
        # Plan: Dim sum dumpling with a broad base and a short gathered neck. Mirrored outline with three separated downward folds. Fine neck wrinkles reduced to a single crown nub; no useful exact Lucide match.
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

        path('dumpling',(24,6),[('L',(30,10)),('L',(30,14)),('C',(42,31),(30,19),(42,23)),('C',(24,42),(42,40),(34,42)),('C',(6,31),(14,42),(6,40)),('C',(18,14),(6,23),(18,19)),('L',(18,10)),('L',(24,6))],True)
        for j,x in enumerate((16,24,32)):line('fold-'+str(j),(x,29),(x,31))
