"""Steaming Roasted Head Kebab."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d9d00d2-561e-4bf5-b3fa-b9a4344a2f26'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/exotic food kebab_3d9d00d2-561e-4bf5-b3fa-b9a4344a2f26.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-roasted-head-kebab'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('steaming', 'roasted', 'head', 'kebab')

    def build(self):
        # Plan: Stylized roasted head-like kebab on a hooked spit with two steam curls. The oval food shape follows the reference; mouth omitted and closed eyes reduced to short marks. Human reference user.svg was inspected for context; no human body or detached head/body pair is depicted.
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

        path('roast',(24,14),[('C',(40,25),(35,14),(40,18)),('C',(24,36),(40,33),(34,36)),('C',(8,25),(14,36),(8,33)),('C',(24,14),(8,18),(13,14))],True)
        path('hook',(24,14),[('L',(24,10)),('A',(28,10),2,6,True)])
        join('hook','roast');line('spit',(24,36),(24,44));join('spit','roast');poly('base',(12,44),(24,44),(36,44));join('base','spit')
        for j,x in enumerate((19,29)):line('eye-'+str(j),(x-1,24),(x+1,24))
        for j,x in enumerate((10,38)):path('steam-'+str(j),(x,4),[('C',(x,8),(x-2,5),(x+2,7))])
