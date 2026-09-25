"""Play last playlist (music), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa83f82a-d435-56a8-a44a-f2497ad79910'
SOURCE_PATH = 'pictographic-primitives/music/play last playlist_aa83f82a-d435-56a8-a44a-f2497ad79910.svg'
AUTHOR = 'gpt-6'

class PlayLastPlaylist(Solo48):
    icon_id = 'play-last-playlist'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    categories = ('primitives', 'music')
    aliases = ()
    keywords = ('play', 'last', 'playlist', 'music')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (25, 13), (44, 13))
        self.add_line('e1', (27, 26), (42, 26))
        self.add_line('e2', (25, 38), (44, 38))
        self.add_line('e3', (9, 11), (17, 21))
        self.add_line('e4', (18, 27), (8, 38))
        self.add_line('e5', (4, 38), (4, 13))
        self.add_arc('e6-1', (4, 13), (5, 9), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e6-2', (5, 9), (6, 8), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('e6-3', (6, 8), (9, 11), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e7', (17, 21), (18, 27), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('e8-1', (8, 38), (6, 40))
        self.add_arc('e8-2', (6, 40), (4, 38), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e6-1', 'e6-2', 'e6-3', 'e3', 'e7', 'e4', 'e8-1', 'e8-2', 'e5'), closed=True)
