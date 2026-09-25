from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b4d2b50-1b9c-4414-9e32-19d3aa7a41d9'
SOURCE_PATH = 'pictographic-primitives/babies/urinal baby_5b4d2b50-1b9c-4414-9e32-19d3aa7a41d9.svg'
AUTHOR = 'gpt-6'

class BabyPotty(Solo48):
    icon_id = 'baby-potty'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    aliases = ()
    keywords = ('potty', 'toilet', 'training', 'baby', 'toddler', 'bathroom', 'pot', 'hygiene')

    # Designed to centerline extremes (6, 6)–(42, 42).
    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_arc('tub-1', (6, 22), (21, 6), radius_x=15, radius_y=16, sweep=True)
        self.add_arc('tub-2', (21, 6), (36, 12), radius_x=15, radius_y=6, sweep=True)
        self.add_line('tub-3', (36, 12), (42, 18))
        self.add_line('tub-4', (42, 18), (42, 34))
        self.add_arc('tub-5', (42, 34), (6, 34), radius_x=18, radius_y=8, sweep=True)
        self.add_line('tub-6', (6, 34), (6, 22))
        self.add_contour('tub', 'tub-1', 'tub-2', 'tub-3', 'tub-4', 'tub-5', 'tub-6', closed=True)
        self.add_arc('rim-1', (6, 22), (36, 22), radius_x=16, radius_y=6, sweep=True)
        self.add_arc('rim-2', (36, 22), (6, 22), radius_x=16, radius_y=6, sweep=True)
        self.add_contour('rim', 'rim-1', 'rim-2', closed=True)
        self.relate("connect", "tub", "rim")
