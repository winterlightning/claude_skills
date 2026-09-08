"""Koala face with soft integrated ear lobes. Upright oval nose and eye-free expression retained. Lucide cat informs bilateral silhouette; ear pairs mirror around x=24."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '788e7c5f-faba-5c83-9317-764052ec91d3'
SOURCE_PATH = 'pictographic-primitives/animals/koala_788e7c5f-faba-5c83-9317-764052ec91d3.svg'
AUTHOR = 'gpt-6'


class KoalaHead(Solo48):
    icon_id = 'koala-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('koala', 'face', 'head', 'ears', 'nose', 'marsupial', 'australia', 'cute')

    def build(self) -> None:
        # Exact visible extremes: (0, 6, 48, 42); centerline inset 2.
        self.add_arc('crown', (16, 14), (32, 14), radius_x=16, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ear-right-inner', (32, 14), (39, 8), radius_x=7, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('ear-right-top', (39, 8), (46, 16), radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ear-right-bottom', (46, 16), (38, 24), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('jaw-right', (38, 24), (24, 40), radius_x=14, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('jaw-left', (24, 40), (10, 24), radius_x=14, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('ear-left-bottom', (10, 24), (2, 16), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ear-left-top', (2, 16), (9, 8), radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ear-left-inner', (9, 8), (16, 14), radius_x=7, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('outline', 'crown', 'ear-right-inner', 'ear-right-top', 'ear-right-bottom', 'jaw-right', 'jaw-left', 'ear-left-bottom', 'ear-left-top', 'ear-left-inner', closed=True)
        self.add_arc('nose-right', (24, 21), (24, 33), radius_x=4, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('nose-left', (24, 33), (24, 21), radius_x=4, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('nose', 'nose-right', 'nose-left', closed=True)
