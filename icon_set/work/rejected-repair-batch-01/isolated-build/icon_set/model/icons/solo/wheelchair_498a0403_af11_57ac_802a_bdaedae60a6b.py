'An empty wheelchair is shown from the side with a large rear wheel and smaller front caster. A high push handle rises behind the seat, and the angled front frame ends in a footrest.\n\nConstruction: Empty wheelchair with large rear wheel, small front caster, backrest and foot support. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '498a0403-af11-57ac-802a-bdaedae60a6b'
SOURCE_PATH = 'pictographic-primitives/wayfinding/wheel chair_498a0403-af11-57ac-802a-bdaedae60a6b.svg'
AUTHOR = 'gpt-6'

class Wheelchair(Solo48):
    icon_id = 'wheelchair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('wheelchair', 'mobility', 'wheel', 'accessibility', 'chair', 'medical')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('rear-wheel-top-joint-1', (4, 30), (14, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-top-joint-2', (14, 20), (24, 30), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-bottom', (24, 30), (4, 30), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('caster-top', (34, 36), (42, 36), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('caster-bottom', (42, 36), (34, 36), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('backrest-1', (6, 8), (12, 8))
        self.add_line('backrest-2', (12, 8), (14, 20))
        self.add_line('backrest-3', (14, 20), (28, 20))
        self.add_line('backrest-4', (28, 20), (32, 30))
        self.add_line('backrest-5', (32, 30), (34, 36))
        self.add_line('footrest', (42, 36), (44, 36))
        self.add_contour('rear-wheel', 'rear-wheel-top-joint-1', 'rear-wheel-top-joint-2', 'rear-wheel-bottom', closed=True)
        self.add_contour('caster', 'caster-top', 'caster-bottom', closed=True)
        self.add_contour('backrest', 'backrest-1', 'backrest-2', 'backrest-3', 'backrest-4', 'backrest-5', closed=False)
        self.relate('connect', 'backrest', 'rear-wheel')
        self.relate('connect', 'backrest', 'caster')
        self.relate('connect', 'footrest', 'caster')
