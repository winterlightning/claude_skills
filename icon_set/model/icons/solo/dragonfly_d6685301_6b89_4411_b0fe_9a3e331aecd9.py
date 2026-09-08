"""dragonfly-with-round-eyes: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6685301-6b89-4411-b0fe-9a3e331aecd9'
SOURCE_PATH = 'pictographic-primitives/animals/dragonfly_d6685301-6b89-4411-b0fe-9a3e331aecd9.svg'
AUTHOR = 'gpt-6'


class DragonflyWithRoundEyes(Solo48):
    icon_id = 'dragonfly-with-round-eyes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('dragonfly', 'insect', 'wings', 'eyes', 'damselfly', 'bug', 'nature', 'pond')

    def build(self):
        self.add_arc('eye-left-1', (21, 2), (21, 8), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-left-2', (21, 8), (21, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('eye-left', 'eye-left-1', 'eye-left-2', closed=True)
        self.add_arc('eye-right-1', (27, 2), (27, 8), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-right-2', (27, 8), (27, 2), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('eye-right', 'eye-right-1', 'eye-right-2', closed=True)
        self.relate("connect", 'eye-left', 'eye-right')
        self.add_line('body', (24, 5), (24, 46))
        self.relate("connect", 'body', 'eye-left')
        self.relate("connect", 'body', 'eye-right')
        self.add_line('upper-left-1', (24, 17), (2, 12))
        self.add_arc('upper-left-2', (2, 12), (9, 24), radius_x=7, radius_y=12, sweep=False)
        self.add_line('upper-left-3', (9, 24), (24, 17))
        self.add_contour('upper-left', 'upper-left-1', 'upper-left-2', 'upper-left-3', closed=True)
        self.add_line('lower-left-1', (24, 27), (4, 34))
        self.add_arc('lower-left-2', (4, 34), (13, 40), radius_x=10, radius_y=6, sweep=False)
        self.add_line('lower-left-3', (13, 40), (24, 27))
        self.add_contour('lower-left', 'lower-left-1', 'lower-left-2', 'lower-left-3', closed=True)
        self.relate("connect", 'body', 'upper-left')
        self.relate("connect", 'body', 'lower-left')
        self.add_line('upper-right-1', (24, 17), (46, 12))
        self.add_arc('upper-right-2', (46, 12), (39, 24), radius_x=7, radius_y=12, sweep=True)
        self.add_line('upper-right-3', (39, 24), (24, 17))
        self.add_contour('upper-right', 'upper-right-1', 'upper-right-2', 'upper-right-3', closed=True)
        self.add_line('lower-right-1', (24, 27), (44, 34))
        self.add_arc('lower-right-2', (44, 34), (35, 40), radius_x=10, radius_y=6, sweep=True)
        self.add_line('lower-right-3', (35, 40), (24, 27))
        self.add_contour('lower-right', 'lower-right-1', 'lower-right-2', 'lower-right-3', closed=True)
        self.relate("connect", 'body', 'upper-right')
        self.relate("connect", 'body', 'lower-right')
        self.relate("connect", 'upper-left', 'upper-right')
        self.relate("connect", 'lower-left', 'lower-right')
