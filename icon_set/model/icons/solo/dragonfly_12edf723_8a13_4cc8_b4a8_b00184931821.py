"""dragonfly: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12edf723-8a13-4cc8-b4a8-b00184931821'
SOURCE_PATH = 'pictographic-primitives/animals/dragonfly_12edf723-8a13-4cc8-b4a8-b00184931821.svg'
AUTHOR = 'gpt-6'


class Dragonfly(Solo48):
    icon_id = 'dragonfly'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('dragonfly', 'insect', 'wings', 'symmetry', 'damselfly', 'bug', 'nature', 'pond')

    def build(self):
        self.add_arc('head-1', (24, 2), (24, 12), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', (24, 12), (24, 2), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('body', (24, 12), (24, 46))
        self.relate("connect", 'head', 'body')
        self.add_arc('wings-left-1', (24, 22), (12, 16), radius_x=14, radius_y=9, sweep=False)
        self.add_arc('wings-left-2', (12, 16), (2, 22), radius_x=10, radius_y=6, sweep=False)
        self.add_arc('wings-left-3', (2, 22), (10, 27), radius_x=8, radius_y=5, sweep=False)
        self.add_line('wings-left-4', (10, 27), (5, 33))
        self.add_arc('wings-left-5', (5, 33), (11, 39), radius_x=6, radius_y=6, sweep=False)
        self.add_line('wings-left-6', (11, 39), (17, 39))
        self.add_arc('wings-left-7', (17, 39), (24, 30), radius_x=7, radius_y=9, sweep=False)
        self.add_line('wings-left-8', (24, 30), (24, 22))
        self.add_contour('wings-left', 'wings-left-1', 'wings-left-2', 'wings-left-3', 'wings-left-4', 'wings-left-5', 'wings-left-6', 'wings-left-7', 'wings-left-8', closed=True)
        self.add_line('division-left', (10, 27), (24, 22))
        self.relate("connect", 'division-left', 'wings-left')
        self.relate("connect", 'body', 'division-left')
        self.relate("connect", 'body', 'wings-left')
        self.add_arc('wings-right-1', (24, 22), (36, 16), radius_x=14, radius_y=9, sweep=True)
        self.add_arc('wings-right-2', (36, 16), (46, 22), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('wings-right-3', (46, 22), (38, 27), radius_x=8, radius_y=5, sweep=True)
        self.add_line('wings-right-4', (38, 27), (43, 33))
        self.add_arc('wings-right-5', (43, 33), (37, 39), radius_x=6, radius_y=6, sweep=True)
        self.add_line('wings-right-6', (37, 39), (31, 39))
        self.add_arc('wings-right-7', (31, 39), (24, 30), radius_x=7, radius_y=9, sweep=True)
        self.add_line('wings-right-8', (24, 30), (24, 22))
        self.add_contour('wings-right', 'wings-right-1', 'wings-right-2', 'wings-right-3', 'wings-right-4', 'wings-right-5', 'wings-right-6', 'wings-right-7', 'wings-right-8', closed=True)
        self.add_line('division-right', (38, 27), (24, 22))
        self.relate("connect", 'division-right', 'wings-right')
        self.relate("connect", 'body', 'division-right')
        self.relate("connect", 'body', 'wings-right')
        self.relate("connect", 'wings-left', 'wings-right')
        self.relate("connect", 'division-left', 'division-right')
