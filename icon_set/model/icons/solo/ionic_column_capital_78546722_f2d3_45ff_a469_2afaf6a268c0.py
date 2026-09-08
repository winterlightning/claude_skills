"""Ionic capital with paired volutes and three shaft strokes. Centerline extremes (2,2)-(46,46). Scrolls simplified to open circular curls; centre dash omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78546722-f2d3-45ff-a469-2afaf6a268c0'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/historical building pillar_78546722-f2d3-45ff-a469-2afaf6a268c0.svg'
AUTHOR = 'gpt-6'

class IonicColumnCapital(Solo48):
    icon_id = 'ionic-column-capital'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('column', 'pillar', 'ionic', 'capital', 'volute', 'classical', 'greek', 'roman', 'architecture')

    def build(self) -> None:
        self.add_line('abacus', (12, 2), (36, 2))
        self.add_arc('left-outer', (12, 2), (12, 22), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('left-inner', (12, 22), (12, 10), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('right-outer', (36, 2), (36, 22), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('right-inner', (36, 22), (36, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_line('shaft16', (16, 29), (16, 46))
        self.add_line('shaft24', (24, 29), (24, 46))
        self.add_line('shaft32', (32, 29), (32, 46))
        self.relate("connect", 'abacus', 'left-outer')
        self.relate("connect", 'abacus', 'right-outer')
        self.relate("connect", 'left-outer', 'left-inner')
        self.relate("connect", 'right-outer', 'right-inner')
