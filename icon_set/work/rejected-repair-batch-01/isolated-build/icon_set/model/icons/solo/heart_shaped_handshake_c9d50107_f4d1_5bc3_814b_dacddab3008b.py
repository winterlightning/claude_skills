"""Clasped hands form a heart. SQUARE extremes 6,6–42,42. Lucide heart-handshake informs integrated thumb/clasp; omit small finger cuts, retain the central hook and heart lobes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9d50107-f4d1-5bc3-814b-dacddab3008b'
SOURCE_PATH = 'pictographic-primitives/social/hand shake heart_c9d50107-f4d1-5bc3-814b-dacddab3008b.svg'
AUTHOR = 'gpt-6'

class HeartShapedHandshake(Solo48):
    icon_id = 'heart-shaped-handshake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/social"
    aliases = ()
    keywords = ('handshake', 'heart', 'hand', 'clasp', 'love', 'friendship', 'partnership')

    def build(self):
        # Mirrored outer lobes, a central clasp, and one finger crease.
        self.add_arc('left-inner', (24,14), (15,6), radius_x=9, radius_y=8, sweep=False)
        self.add_arc('left-outer', (15,6), (6,16), radius_x=9, radius_y=10, sweep=False)
        self.add_arc('left-lower', (6,16), (10,25), radius_x=13, sweep=False)
        self.add_line('left-point', (10,25), (24,42))
        self.add_line('right-point', (24,42), (38,25))
        self.add_arc('right-lower', (38,25), (42,16), radius_x=13, sweep=False)
        self.add_arc('right-outer', (42,16), (33,6), radius_x=9, radius_y=10, sweep=False)
        self.add_arc('right-inner', (33,6), (24,14), radius_x=9, radius_y=8, sweep=False)
        self.add_contour('outline','left-inner','left-outer','left-lower','left-point','right-point','right-lower','right-outer','right-inner',closed=True)
        self.add_line('thumb-top',(24,14),(18,20))
        self.add_arc('thumb-tip',(18,20),(24,26),radius_x=4,sweep=False)
        self.add_polyline('grip',(24,26),(30,22),(38,25))
        self.add_contour('thumb','thumb-top','thumb-tip')
        self.relate('connect','outline','thumb')
        self.relate('connect','thumb','grip')
        self.relate('connect','outline','grip')
