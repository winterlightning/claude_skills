"""Traditional Chef Hat."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7682f43-a7e7-5da6-949a-3a0960f72c5d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear hat_c7682f43-a7e7-5da6-949a-3a0960f72c5d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'traditional-chef-toque'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('traditional', 'chef', 'toque')

    def build(self):
        # Plan: Traditional chef toque with three puffy crown lobes and a tall banded body. Lucide chef-hat informs the crown/body transition and lower band; tiny inward curl simplified.
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

        path('hat',(12,34),[('L',(12,26)),('C',(6,18),(8,26),(6,22)),('C',(15,12),(6,12),(10,10)),('C',(24,6),(17,7),(20,6)),('C',(33,12),(28,6),(31,7)),('C',(42,18),(38,10),(42,12)),('C',(36,26),(42,22),(40,26)),('L',(36,34)),('L',(36,42)),('L',(12,42)),('L',(12,34))],True)
        line('band',(12,34),(36,34));join('band','hat')
