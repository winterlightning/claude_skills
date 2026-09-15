"""Notes flip (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd68affa5-659e-5b1e-8361-c17d53d111df'
SOURCE_PATH = 'pictographic-primitives/content/notes flip_d68affa5-659e-5b1e-8361-c17d53d111df.svg'
AUTHOR = 'gpt-6'

class NotesFlip(Solo48):
    icon_id = 'notes-flip'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('notes', 'flip', 'content')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (17, 13), (31, 13))
        self.add_line('e1', (17, 21), (31, 21))
        self.add_line('e2', (17, 29), (29, 29))
        self.add_line('e3', (8, 39), (8, 8))
        self.add_line('e4', (12, 4), (36, 4))
        self.add_line('e5', (40, 9), (40, 40))
        self.add_line('e6', (35, 44), (10, 44))
        self.add_arc('e7', (8, 8), (12, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e8-1', (36, 4), (40, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e8-2', (40, 8), (40, 9), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_arc('e9-1', (40, 40), (36, 44), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e9-2', (36, 44), (35, 44), radius_x=36, radius_y=36, large_arc=False, sweep=False)
        self.add_line('e10', (10, 44), (8, 39))
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3', 'e7', 'e4', 'e8-1', 'e8-2', 'e5', 'e9-1', 'e9-2', 'e6', 'e10'), closed=True)
