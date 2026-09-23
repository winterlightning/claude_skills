"""A four-cell district map with a marker in its upper-left cell.

SOLO48 SQUARE; Lucide reference: map: folded panels; map-pin: circular location marker.
Symbol plan: source composition reduced to named outlines and shared geometry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '05fdcf39-465f-410a-82f7-a84fc9bc4534'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/district_05fdcf39-465f-410a-82f7-a84fc9bc4534.svg'
AUTHOR = 'gpt-6'

class DistrictMapMarker(Solo48):
    icon_id = 'district-map-marker'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps/locations'
    aliases = ('Map Layout with Location Marker',)
    keywords = tuple('map layout with location marker'.split())

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
        self.box('map',6,6,42,42)
        self.add_line('vertical',(24,6),(24,42)); self.relate('connect','vertical','map')
        self.add_line('left-row',(6,26),(24,26)); self.relate('connect','left-row','map'); self.relate('connect','left-row','vertical')
        self.add_line('right-row',(24,22),(42,22)); self.relate('connect','right-row','map'); self.relate('connect','right-row','vertical')
        self.add_line('right-column',(33,22),(33,42)); self.relate('connect','right-column','map'); self.relate('connect','right-column','right-row')
        self.add_dot('marker',(15,15))
