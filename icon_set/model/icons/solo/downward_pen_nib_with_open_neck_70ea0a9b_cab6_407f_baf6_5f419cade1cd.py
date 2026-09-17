"""Fountain Pen Nib.
Plan: Symmetric downward nib with open neck, circular breather and slit. Centerline extremes (8,4)-(40,44).
Construction: Lucide pen-tool; breather connected to slit.
Reduction: No defining features removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70ea0a9b-cab6-407f-baf6-5f419cade1cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/vectors pen_70ea0a9b-cab6-407f-baf6-5f419cade1cd.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/vectors pen_70ea0a9b-cab6-407f-baf6-5f419cade1cd.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'downward-pen-nib-with-open-neck'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('fountain', 'pen', 'nib')

    def build(self):
        axis=24
        self.add_polyline('neck-left',(14,4),(16,12))
        self.add_polyline('neck-right',(34,4),(32,12))
        self.add_polyline('outline',(16,12),(32,12),(40,24),(24,44),(8,24),(16,12),closed=True)
        for side in ('left','right'):self.relate('connect','neck-'+side,'outline')
        _circle(self,'breather',axis,24,4)
        self.add_line('slit',(axis,28),(axis,44))
        self.relate('connect','slit','breather')
        self.relate('connect','slit','outline')
