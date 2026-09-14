"""elephant-head: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '448ae7e7-230e-5858-9857-5a4d7a93f188'
SOURCE_PATH = 'pictographic-primitives/animals/elephant head_448ae7e7-230e-5858-9857-5a4d7a93f188.svg'
AUTHOR = 'gpt-6'


class ElephantHead(Solo48):
    icon_id = 'elephant-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('elephant', 'head', 'face', 'trunk', 'tusks', 'ears', 'animal', 'wildlife')

    def build(self):
        self.add_bezier('face-1', (14, 8), *(((16.42960017, 6.24779087), (20.30411073, 6), (24, 6)),))
        self.add_bezier('face-2', (24, 6), *(((27.69588927, 6), (31.57039983, 6.24779087), (34, 8)),))
        self.add_arc('face-3', (34, 8), (36, 16), radius_x=2, radius_y=8, sweep=True)
        self.add_arc('face-4', (36, 16), (34, 25), radius_x=2, radius_y=9, sweep=True)
        self.add_arc('face-5', (34, 25), (26, 36), radius_x=8, radius_y=11, sweep=False)
        self.add_arc('face-6', (26, 36), (34, 38), radius_x=8, radius_y=2, sweep=False)
        self.add_bezier('face-7', (34, 38), *(((32.39737339, 40.83874454), (29.2325716, 42), (26, 42)),))
        self.add_bezier('face-8', (26, 42), *(((22.7674284, 42), (19.60262661, 40.83874454), (18, 38)),))
        self.add_line('face-9', (18, 38), (18, 32))
        self.add_arc('face-10', (18, 32), (14, 25), radius_x=4, radius_y=7, sweep=True)
        self.add_arc('face-11', (14, 25), (12, 16), radius_x=2, radius_y=9, sweep=True)
        self.add_arc('face-12', (12, 16), (14, 8), radius_x=2, radius_y=8, sweep=True)
        self.add_contour('face', 'face-1', 'face-2', 'face-3', 'face-4', 'face-5', 'face-6', 'face-7', 'face-8', 'face-9', 'face-10', 'face-11', 'face-12', closed=True)
        self.add_bezier('ear-left-1', (14, 8), *(((8.95896372, 9.32947462), (6, 12.99871542), (6, 17)),))
        self.add_bezier('ear-left-2', (6, 17), *(((6, 21.80465605), (6.24779087, 26.84151977), (8, 30)),))
        self.add_arc('ear-left-3', (8, 30), (14, 25), radius_x=6, radius_y=5, sweep=False)
        self.add_contour('ear-left', 'ear-left-1', 'ear-left-2', 'ear-left-3', closed=False)
        self.relate("connect", 'ear-left', 'face')
        self.add_bezier('ear-right-1', (34, 8), *(((39.04103628, 9.32947462), (42, 12.99871542), (42, 17)),))
        self.add_bezier('ear-right-2', (42, 17), *(((42, 21.80465605), (41.75220913, 26.84151977), (40, 30)),))
        self.add_arc('ear-right-3', (40, 30), (34, 25), radius_x=6, radius_y=5, sweep=True)
        self.add_contour('ear-right', 'ear-right-1', 'ear-right-2', 'ear-right-3', closed=False)
        self.relate("connect", 'ear-right', 'face')
