"""Emerald Cut Gemstone.
Plan: Upright octagon with square table, paired facets and clipped corners. Centerline extremes (8,4)-(40,44).
Construction: Lucide gem; broad facet fields.
Reduction: No identifying facets removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07fc8f13-e3e6-4678-83ef-211ae05bdfd1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/shape rhomboid_07fc8f13-e3e6-4678-83ef-211ae05bdfd1.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/shape rhomboid_07fc8f13-e3e6-4678-83ef-211ae05bdfd1.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'emerald-cut-gemstone-with-square-table'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('emerald', 'cut', 'gemstone')

    def build(self):
        outer=[(16,4),(32,4),(40,12),(40,36),(32,44),(16,44),(8,36),(8,12)]
        self.add_polyline('rim',*outer,closed=True)
        self.add_polyline('table',(16,16),(32,16),(32,32),(16,32),closed=True)
        for i,(a,c) in enumerate([((8,12),(16,16)),((40,12),(32,16)),((40,36),(32,32)),((8,36),(16,32))]):
         self.add_line(f'facet-{i}',a,c)
         self.relate('connect',f'facet-{i}','rim')
         self.relate('connect',f'facet-{i}','table')
