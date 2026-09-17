"""Slotted Kitchen Spatula."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50edc7df-070e-5467-8616-d359725d3c48'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/spatula_50edc7df-070e-5467-8616-d359725d3c48.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'slotted-kitchen-spatula-wide'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('slotted', 'kitchen', 'spatula', 'wide')

    def build(self):
        # Plan: Wide chamfered spatula head with round stroke joins, three short slots and a centered handle. Straight side walls give all three slots the required clear spacing.
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

        poly('head',(10,4),(38,4),(40,6),(40,24),(34,28),(24,28),(14,28),(8,24),(8,6),closed=True)
        line('handle',(24,28),(24,44));join('head','handle')
        for j,x in enumerate((16,24,32)):line('slot-'+str(j),(x,13),(x,19))
