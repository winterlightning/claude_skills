"""Front-facing lamb with eight broad fleece lobes and oval face. Lucide cloud informs the wool scallops. Folded ears integrated into the face silhouette to preserve open space. Source twins deliberately share geometry and retain independent provenance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9703bb75-a343-538b-9854-1d21a9bbd1b5'
SOURCE_PATH = 'pictographic-primitives/animals/lamb_9703bb75-a343-538b-9854-1d21a9bbd1b5.svg'
AUTHOR = 'gpt-6'


class WoollyLambFront(Solo48):
    icon_id = 'woolly-lamb-front'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('lamb', 'sheep', 'wool', 'fluffy', 'face', 'farm', 'livestock', 'front')

    def build(self) -> None:
        # Exact visible extremes: (0, 0, 48, 48); centerline inset 2.
        self.add_arc('tuft-top', (16, 9), (32, 9), radius_x=8, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('tuft-upper-right', (32, 9), (40, 17), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('tuft-right', (40, 17), (40, 31), radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('tuft-lower-right', (40, 31), (32, 39), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('tuft-bottom', (32, 39), (16, 39), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('tuft-lower-left', (16, 39), (8, 31), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('tuft-left', (8, 31), (8, 17), radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('tuft-upper-left', (8, 17), (16, 9), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('fleece', 'tuft-top', 'tuft-upper-right', 'tuft-right', 'tuft-lower-right', 'tuft-bottom', 'tuft-lower-left', 'tuft-left', 'tuft-upper-left', closed=True)
        self.add_arc('face-top', (17, 21), (31, 21), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('ear-right-top', (31, 21), (36, 26))
        self.add_arc('ear-right-bottom', (36, 26), (31, 27), radius_x=6, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('jaw-right', (31, 27), (24, 34), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('jaw-left', (24, 34), (17, 27), radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('ear-left-bottom', (17, 27), (12, 26), radius_x=6, radius_y=3, sweep=True, large_arc=False)
        self.add_line('ear-left-top', (12, 26), (17, 21))
        self.add_contour('face', 'face-top', 'ear-right-top', 'ear-right-bottom', 'jaw-right', 'jaw-left', 'ear-left-bottom', 'ear-left-top', closed=True)
        self.add_line('leg-left', (16, 39), (16, 46))
        self.add_line('leg-right', (32, 39), (32, 46))
        self.relate("connect", 'leg-left', 'fleece')
        self.relate("connect", 'leg-right', 'fleece')
