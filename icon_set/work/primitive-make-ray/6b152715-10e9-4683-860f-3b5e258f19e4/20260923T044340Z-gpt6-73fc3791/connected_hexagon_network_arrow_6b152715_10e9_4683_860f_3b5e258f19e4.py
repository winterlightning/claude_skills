"""Three connected hexagon nodes point to a downward arrow.

SOLO48 HRECT_L; Lucide reference: network: branching shared junction.
Symbol plan: source composition reduced to named outlines and shared geometry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6b152715-10e9-4683-860f-3b5e258f19e4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/elemental mediaconnect 1_6b152715-10e9-4683-860f-3b5e258f19e4.svg'
AUTHOR = 'gpt-6'

class ConnectedHexagonNetworkArrow(Solo48):
    icon_id = 'connected-hexagon-network-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'data/networks'
    aliases = ('Connected Hexagon Network with Downward Arrow',)
    keywords = tuple('connected hexagon network with downward arrow'.split())

    def ring(self, name, x, y, r):
        self.add_arc(name+'-ne',(x,y-r),(x+r,y),radius_x=r,sweep=True)
        self.add_arc(name+'-se',(x+r,y),(x,y+r),radius_x=r,sweep=True)
        self.add_arc(name+'-sw',(x,y+r),(x-r,y),radius_x=r,sweep=True)
        self.add_arc(name+'-nw',(x-r,y),(x,y-r),radius_x=r,sweep=True)
        self.add_contour(name,*(name+'-'+s for s in ('ne','se','sw','nw')),closed=True)

    def box(self, name, x1, y1, x2, y2):
        self.add_polyline(name,(x1,y1),(x2,y1),(x2,y2),(x1,y2),closed=True)

    def round_box(self, name, x1, y1, x2, y2, r):
        parts=[]
        def line(s,a,b):
            n=name+'-'+s; self.add_line(n,a,b); parts.append(n)
        def arc(s,a,b):
            n=name+'-'+s; self.add_arc(n,a,b,radius_x=r,sweep=True); parts.append(n)
        line('top',(x1+r,y1),(x2-r,y1))
        arc('ne',(x2-r,y1),(x2,y1+r))
        line('right',(x2,y1+r),(x2,y2-r))
        arc('se',(x2,y2-r),(x2-r,y2))
        line('bottom',(x2-r,y2),(x1+r,y2))
        arc('sw',(x1+r,y2),(x1,y2-r))
        line('left',(x1,y2-r),(x1,y1+r))
        arc('nw',(x1,y1+r),(x1+r,y1))
        self.add_contour(name,*parts,closed=True)

    def heart(self,name,x,y):
        self.add_arc(name+'-left',(x,y-2),(x-6,y-4),radius_x=4,radius_y=4,sweep=False)
        self.add_arc(name+'-left-side',(x-6,y-4),(x-6,y+2),radius_x=4,radius_y=4,sweep=False)
        self.add_line(name+'-left-tip',(x-6,y+2),(x,y+8))
        self.add_line(name+'-right-tip',(x,y+8),(x+6,y+2))
        self.add_arc(name+'-right-side',(x+6,y+2),(x+6,y-4),radius_x=4,radius_y=4,sweep=False)
        self.add_arc(name+'-right',(x+6,y-4),(x,y-2),radius_x=4,radius_y=4,sweep=False)
        self.add_contour(name,*(name+s for s in ('-left','-left-side','-left-tip','-right-tip','-right-side','-right')),closed=True)

    def build(self) -> None:
        self.add_polyline('top-node',(24,8),(30,11),(30,17),(24,20),(18,17),(18,11),closed=True)
        self.add_polyline('left-node',(8,22),(14,25),(14,31),(8,34),(4,31),(4,25),closed=True)
        self.add_polyline('right-node',(40,22),(44,25),(44,31),(40,34),(34,31),(34,25),closed=True)
        self.add_polyline('link-left',(18,15),(14,18),(10,18))
        self.add_polyline('link-right',(30,15),(34,18),(38,18))
        self.add_polyline('down-arrow',(24,22),(24,40),(18,34))
        self.add_line('down-head',(24,40),(30,34))
