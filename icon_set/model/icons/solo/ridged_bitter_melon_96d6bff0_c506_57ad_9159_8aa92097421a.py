"""Ridged Bitter Melon Gourd."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96d6bff0-c506-57ad-9159-8aa92097421a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/bitter melon_96d6bff0-c506-57ad-9159-8aa92097421a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ridged-bitter-melon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('ridged', 'bitter', 'melon')

    def build(self):
        # Plan: Supplied bitter melon: pointed gourd with paired lengthwise ridges, scalloped edges and short stem. Mirrored shell and ridge pair. Fine waviness reduced; no useful exact Lucide match.
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

        # Mirrored scalloped shell; a repeated pair of lengthwise ridges.
        path('gourd',(24,10),[('C',(37,20),(35,12),(37,15)),('C',(40,27),(37,23),(40,23)),('C',(36,35),(40,30),(36,32)),('C',(24,44),(36,40),(28,44)),('C',(12,35),(20,44),(12,40)),('C',(8,27),(12,32),(8,30)),('C',(11,20),(8,23),(11,23)),('C',(24,10),(11,15),(13,12))],True)
        line('stem',(24,4),(24,10));join('stem','gourd')
        for x, inward in ((19,1),(29,-1)):
            path(f'ridge-{x}',(x,22),[('C',(x,30),(x+inward,24),(x+inward,27))])
