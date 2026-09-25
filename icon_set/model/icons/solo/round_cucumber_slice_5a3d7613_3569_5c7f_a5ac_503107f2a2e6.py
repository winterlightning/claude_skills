"""Round Cucumber Slice."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a3d7613-3569-5c7f-a5ac-503107f2a2e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cucumber slice_5a3d7613-3569-5c7f-a5ac-503107f2a2e6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-cucumber-slice'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('round', 'cucumber', 'slice')

    def build(self):
        # Plan: Supplied cucumber: circular skin with five radial seed strokes. Tiny teardrop outlines simplified to open strokes with generous surrounding flesh. No useful exact Lucide match.
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

        oval('skin',24,24,20,20)
        seeds=(((24,13),(24,16)),((34,21),(31,22)),((30,32),(29,30)),((18,32),(19,30)),((14,21),(17,22)))
        for i,(a,b) in enumerate(seeds):line(f'seed-{i}',a,b)
