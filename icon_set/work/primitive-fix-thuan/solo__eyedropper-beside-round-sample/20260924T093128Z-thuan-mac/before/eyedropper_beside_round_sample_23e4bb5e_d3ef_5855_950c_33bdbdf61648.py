"""Eyedropper and Color Sample Circle.
Plan: Diagonal tool with a separate round sample at lower right. Centerline extremes (6,6)-(42,42).
Construction: Lucide pipette; rounded bulb.
Reduction: Collar shortened on the sample side to preserve clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23e4bb5e-d3ef-5855-950c-33bdbdf61648'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color picker 3_23e4bb5e-d3ef-5855-950c-33bdbdf61648.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/color picker 3_23e4bb5e-d3ef-5855-950c-33bdbdf61648.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'eyedropper-beside-round-sample'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('eyedropper', 'and', 'color', 'sample', 'circle')

    def build(self):
        self.add_line('bulb-start',(26,10),(30,6))
        self.add_arc('bulb-round',(30,6),(40,16),radius_x=10)
        self.add_line('bulb-end',(40,16),(36,20))
        self.add_contour('bulb','bulb-start','bulb-round','bulb-end')
        self.add_polyline('body',(26,10),(8,28),(6,36),(14,34),(36,20))
        self.add_polyline('collar',(22,6),(26,10),(36,20))
        for a,c in [('bulb','body'),('bulb','collar'),('body','collar')]:self.relate('connect',a,c)
        _circle(self,'sample',37,37,5)
