'Stone bridge: two equal tiers of arches share real vertical piers above a smooth water line; omit the cramped middle deck rule.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/bridge_8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192.svg'
AUTHOR = 'gpt-6'


class ArchedStoneBridge(Solo48):
    icon_id = 'arched-stone-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('bridge', 'arch', 'viaduct', 'river', 'water', 'crossing', 'stone', 'landmark', 'infrastructure')

    def build(self):
        # Reduced the double-storey bridge to one broad rounded arch and two stone piers; Lucide bridge informs simple structural strokes.

        def path(n, start, commands, closed=False):
            names=[];here=start
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                names.append(ident);here=end
            self.add_contour(n,*names,closed=closed)
        def ellipse(n,x,y,rx,ry):
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('stone',(6,42),[('L',(6,6)),('L',(42,6)),('L',(42,42)),('L',(34,42)),('L',(34,26)),('A',(24,16),10,10,False),('A',(14,26),10,10,False),('L',(14,42)),('L',(6,42))],True)
