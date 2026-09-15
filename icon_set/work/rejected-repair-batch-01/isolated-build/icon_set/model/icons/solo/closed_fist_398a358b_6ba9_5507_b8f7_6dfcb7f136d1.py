'A closed fist extends horizontally from the right, with four curled fingers stacked along its left edge. The thumb folds down over the upper fingers and a curved crease crosses the palm.\n\nConstruction: Closed fist in profile, with a folded thumb and two knuckle creases. Bounds (4,8)-(44,40).\nLucide: hand-fist: compact outer mass and thumb fold.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '398a358b-6ba9-5507-b8f7-6dfcb7f136d1'
SOURCE_PATH = 'pictographic-primitives/wayfinding/hand fist bump_398a358b-6ba9-5507-b8f7-6dfcb7f136d1.svg'
AUTHOR = 'gpt-6'

class ClosedFist(Solo48):
    icon_id = 'closed-fist'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('fist', 'hand', 'knuckles', 'gesture', 'closed', 'thumb')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('wrist-top', (44, 16), (38, 16))
        self.add_arc('upper-palm', (38, 16), (26, 8), radius_x=12, radius_y=8, large_arc=False, sweep=False)
        self.add_line('knuckle-top', (26, 8), (12, 8))
        self.add_arc('upper-knuckle', (12, 8), (4, 16), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('knuckle-side-joint-1', (4, 16), (4, 20))
        self.add_line('knuckle-side-joint-2', (4, 20), (4, 30))
        self.add_line('knuckle-side-joint-3', (4, 30), (4, 32))
        self.add_arc('lower-knuckle', (4, 32), (12, 40), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('knuckle-bottom', (12, 40), (26, 40))
        self.add_arc('lower-palm', (26, 40), (38, 32), radius_x=12, radius_y=8, large_arc=False, sweep=False)
        self.add_line('wrist-bottom', (38, 32), (44, 32))
        self.add_arc('thumb-upper', (26, 8), (18, 20), radius_x=8, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('thumb-lower', (18, 20), (26, 28), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('thumb-end', (26, 28), (34, 28))
        self.add_line('upper-crease', (4, 20), (8, 20))
        self.add_line('lower-crease', (4, 30), (12, 30))
        self.add_contour('outline', 'wrist-top', 'upper-palm', 'knuckle-top', 'upper-knuckle', 'knuckle-side-joint-1', 'knuckle-side-joint-2', 'knuckle-side-joint-3', 'lower-knuckle', 'knuckle-bottom', 'lower-palm', 'wrist-bottom', closed=False)
        self.add_contour('thumb', 'thumb-upper', 'thumb-lower', 'thumb-end', closed=False)
        self.relate('connect', 'thumb', 'outline')
        self.relate('connect', 'upper-crease', 'outline')
        self.relate('connect', 'lower-crease', 'outline')
