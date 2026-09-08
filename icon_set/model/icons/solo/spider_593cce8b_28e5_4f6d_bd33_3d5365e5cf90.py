from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '593cce8b-28e5-4f6d-bd33-3d5365e5cf90'
SOURCE_PATH = 'pictographic-primitives/animals/spider_593cce8b-28e5-4f6d-bd33-3d5365e5cf90.svg'
AUTHOR = 'gpt-6'


class Spider(Solo48):
    icon_id = 'spider'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('spider', 'arachnid', 'eight legs', 'bug', 'web', 'halloween', 'tarantula', 'insect')

    def build(self) -> None:
        # Eight angular legs around two body masses; extremes (2,2)-(46,46).
        self.add_arc('thorax0', (18, 17), (24, 10), radius_x=6, radius_y=7, sweep=True)
        self.add_arc('thorax1', (24, 10), (30, 17), radius_x=6, radius_y=7, sweep=True)
        self.add_arc('thorax2', (30, 17), (24, 24), radius_x=6, radius_y=7, sweep=True)
        self.add_arc('thorax3', (24, 24), (18, 17), radius_x=6, radius_y=7, sweep=True)
        self.add_contour('thorax', 'thorax0', 'thorax1', 'thorax2', 'thorax3', closed=True)
        self.add_arc('abdomen0', (15, 35), (24, 24), radius_x=9, radius_y=11, sweep=True)
        self.add_arc('abdomen1', (24, 24), (33, 35), radius_x=9, radius_y=11, sweep=True)
        self.add_arc('abdomen2', (33, 35), (24, 46), radius_x=9, radius_y=11, sweep=True)
        self.add_arc('abdomen3', (24, 46), (15, 35), radius_x=9, radius_y=11, sweep=True)
        self.add_contour('abdomen', 'abdomen0', 'abdomen1', 'abdomen2', 'abdomen3', closed=True)
        self.add_line('l-top-1', (24, 10), (12, 8))
        self.add_line('l-top-2', (12, 8), (12, 2))
        self.add_contour('l-top', 'l-top-1', 'l-top-2', closed=False)
        self.add_line('l-upper-1', (18, 17), (3, 14))
        self.add_line('l-upper-2', (3, 14), (2, 7))
        self.add_contour('l-upper', 'l-upper-1', 'l-upper-2', closed=False)
        self.add_line('l-lower-1', (24, 24), (3, 24))
        self.add_line('l-lower-2', (3, 24), (2, 33))
        self.add_contour('l-lower', 'l-lower-1', 'l-lower-2', closed=False)
        self.add_line('l-bottom-1', (15, 35), (9, 39))
        self.add_line('l-bottom-2', (9, 39), (9, 46))
        self.add_contour('l-bottom', 'l-bottom-1', 'l-bottom-2', closed=False)
        self.add_line('r-top-1', (24, 10), (36, 8))
        self.add_line('r-top-2', (36, 8), (36, 2))
        self.add_contour('r-top', 'r-top-1', 'r-top-2', closed=False)
        self.add_line('r-upper-1', (30, 17), (45, 14))
        self.add_line('r-upper-2', (45, 14), (46, 7))
        self.add_contour('r-upper', 'r-upper-1', 'r-upper-2', closed=False)
        self.add_line('r-lower-1', (24, 24), (45, 24))
        self.add_line('r-lower-2', (45, 24), (46, 33))
        self.add_contour('r-lower', 'r-lower-1', 'r-lower-2', closed=False)
        self.add_line('r-bottom-1', (33, 35), (39, 39))
        self.add_line('r-bottom-2', (39, 39), (39, 46))
        self.add_contour('r-bottom', 'r-bottom-1', 'r-bottom-2', closed=False)
        self.relate("connect", 'thorax', 'abdomen')
        self.relate("connect", 'thorax', 'l-top')
        self.relate("connect", 'thorax', 'l-upper')
        self.relate("connect", 'thorax', 'l-lower')
        self.relate("connect", 'thorax', 'r-top')
        self.relate("connect", 'thorax', 'r-upper')
        self.relate("connect", 'thorax', 'r-lower')
        self.relate("connect", 'abdomen', 'l-lower')
        self.relate("connect", 'abdomen', 'l-bottom')
        self.relate("connect", 'abdomen', 'r-lower')
        self.relate("connect", 'abdomen', 'r-bottom')
        self.relate("connect", 'l-top', 'r-top')
        self.relate("connect", 'l-lower', 'r-lower')
