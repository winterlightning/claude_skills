"""Hand Drawn Sweeping Broom.
Plan: Flared broom with leaning handle and two sweeping strokes. Centerline extremes (6,6)-(42,42).
Construction: Lucide brush; broad brush head and narrow shaft.
Reduction: Individual bristles and extra collar band omitted; attachment is the brush top edge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54990bb9-0286-5ac5-8342-7498801cef00'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/astrology broom_54990bb9-0286-5ac5-8342-7498801cef00.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/astrology broom_54990bb9-0286-5ac5-8342-7498801cef00.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'angled-broom-with-sweeping-strokes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hand', 'drawn', 'sweeping', 'broom')

    def build(self):
        self.add_line('handle',(34,6),(26,22))
        self.add_polyline('brush',(22,20),(26,22),(30,24),(26,42),(6,34),(22,20),closed=True)
        self.relate('connect','handle','brush')
        self.add_line('sweep-0',(38,26),(42,30))
        self.add_line('sweep-1',(36,38),(40,42))
