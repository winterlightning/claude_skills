"""Soft Serve Ice Cream Cone."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f10393a-c90e-5b69-bcbc-4aabc3f701f1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ice cream cone_1f10393a-c90e-5b69-bcbc-4aabc3f701f1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'soft-serve-cone'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('soft', 'serve', 'cone')

    def build(self):
        # Plan: Soft-serve swirl with two rounded tiers and a plain tapered cone. Lucide ice-cream-cone informs the broad shared rim and rounded cream contour. Three crowded tiers reduced to two; tip curls asymmetrically.
        # Envelope: VRECT_M; visible ink (8, 2, 40, 46) on SOLO48.

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

        path('cream',(14,26),[('C',(10,22),(12,26),(10,24)),('C',(14,16),(10,18),(12,16)),('C',(21,9),(14,11),(17,10)),('C',(27,4),(25,8),(27,7)),('C',(32,14),(31,6),(34,10)),('C',(38,22),(36,14),(38,18)),('C',(34,26),(38,24),(36,26)),('L',(14,26))],True)
        path('swirl',(14,16),[('C',(32,14),(20,18),(29,17))]);join('swirl','cream')
        poly('cone',(14,26),(24,44),(34,26));join('cone','cream')
