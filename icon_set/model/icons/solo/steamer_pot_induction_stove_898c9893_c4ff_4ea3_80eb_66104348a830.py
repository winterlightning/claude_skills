"""Steamer pot on induction stove."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '898c9893-c4ff-4ea3-80eb-66104348a830'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/stove steamer induction_898c9893-c4ff-4ea3-80eb-66104348a830.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steamer-pot-induction-stove'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('steamer', 'pot', 'induction', 'stove')

    def build(self):
        # Plan: Two-tier steamer with a lid knob and short side handles above a stove line. Lucide cooking-pot informs shared rim and rounded base. Dense heat ticks removed; pot tier and separate stove retained.
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

        path('pot',(10,14),[('L',(24,14)),('L',(38,14)),('L',(38,24)),('L',(38,30)),('A',(34,34),4,4,True),('L',(14,34)),('A',(10,30),4,4,True),('L',(10,24)),('L',(10,14))],True)
        line('tier',(10,24),(38,24));join('tier','pot')
        line('knob',(24,6),(24,14));join('knob','pot')
        for j,(p,q) in enumerate([((6,24),(10,24)),((38,24),(42,24))]):line('handle-'+str(j),p,q);join('handle-'+str(j),'pot')
        line('stove',(6,42),(42,42))
