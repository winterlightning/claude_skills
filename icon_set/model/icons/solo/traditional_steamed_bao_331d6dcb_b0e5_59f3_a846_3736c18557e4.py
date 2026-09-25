"""Traditional Steamed Bao Bun."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '331d6dcb-b0e5-59f3-a846-3736c18557e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/bao steam bun_331d6dcb-b0e5-59f3-a846-3736c18557e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'traditional-steamed-bao'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('traditional', 'steamed', 'bao')

    def build(self):
        # Plan: Traditional steamed bao with a broad domed body and two curved folds beneath a pinched peak. Shared peak and mirrored body; no small surface details added. No useful exact Lucide match.
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

        path('bun',(24,6),[('C',(42,29),(31,10),(42,16)),('C',(24,42),(42,39),(35,42)),('C',(6,29),(13,42),(6,39)),('C',(24,6),(6,16),(17,10))],True)
        path('fold-left',(24,6),[('C',(15,23),(23,15),(22,20))]);join('fold-left','bun')
        path('fold-right',(24,6),[('C',(33,23),(25,15),(26,20))]);join('fold-right','bun')
