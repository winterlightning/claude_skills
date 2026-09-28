"""Spicy Tabasco Sauce Bottle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae34173e-d095-4e1b-a298-37c5f2918127'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/spicy tabasco sauce_ae34173e-d095-4e1b-a298-37c5f2918127.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tabasco-sauce-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('tabasco', 'sauce', 'bottle')

    def build(self):
        # Plan: Hot sauce bottle with tall capped neck, sloping shoulders and a diamond label. Mirrored body and diamond; tiny label dash omitted. No useful exact Lucide match.
        # Envelope: VRECT_L; visible ink (6, 2, 42, 46) on SOLO48.

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

        path('bottle',(20,4),[('L',(28,4)),('L',(28,12)),('L',(28,15)),('C',(40,22),(28,18),(40,16)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,22)),('C',(20,15),(8,16),(20,18)),('L',(20,12)),('L',(20,4))],True)
        line('cap',(20,12),(28,12));join('cap','bottle')
        poly('label',(24,23),(30,29),(24,35),(18,29),(24,23),closed=True)
