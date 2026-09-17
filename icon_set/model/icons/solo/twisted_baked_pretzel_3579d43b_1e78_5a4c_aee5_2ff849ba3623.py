"""Twisted Baked Pretzel."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3579d43b-1e78-5a4c-aee5-2ff849ba3623'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pretzel_3579d43b-1e78-5a4c-aee5-2ff849ba3623.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twisted-baked-pretzel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('twisted', 'baked', 'pretzel')

    def build(self):
        # Plan: Pretzel formed by one continuous dough stroke, two upper loops and a rounded lower loop. Crossing arms share a center node and meet the outer rope at real nodes, leaving three clear openings. Thick outlined rope reduced to a 4-unit stroke; no useful exact Lucide match.
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

        path('rope',(14,34),[('L',(24,24)),('L',(32,14)),('C',(34,6),(28,10),(28,6)),('C',(42,17),(40,6),(42,10)),('C',(34,34),(42,26),(39,30)),('C',(24,42),(30,39),(29,42)),('C',(14,34),(19,42),(18,39)),('C',(6,17),(9,30),(6,26)),('C',(14,6),(6,10),(8,6)),('C',(16,14),(20,6),(20,10)),('L',(24,24)),('L',(34,34))])
