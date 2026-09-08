"""Golden Temple with three pointed domes and arched entrance. Centerline extremes (2,2)-(46,46). Secondary domes reduced to pointed caps; roof bands omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b9ea39c-632b-54a0-8793-8c843fef4fab'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/golden temple_5b9ea39c-632b-54a0-8793-8c843fef4fab.svg'
AUTHOR = 'gpt-6'

class GoldenTemple(Solo48):
    icon_id = 'golden-temple'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('golden temple', 'amritsar', 'india', 'sikh', 'gurdwara', 'dome', 'landmark', 'religion')

    def build(self) -> None:
        self.add_arc('onion-left', (24, 2), (16, 15), radius_x=12, radius_y=11, sweep=False)
        self.add_arc('onion-base-left', (16, 15), (24, 20), radius_x=8, radius_y=5, sweep=False)
        self.add_arc('onion-base-right', (24, 20), (32, 15), radius_x=8, radius_y=5, sweep=False)
        self.add_arc('onion-right', (32, 15), (24, 2), radius_x=12, radius_y=11, sweep=False)
        self.add_contour('onion', 'onion-left', 'onion-base-left', 'onion-base-right', 'onion-right', closed=True)
        self.add_line('dome-neck', (24, 20), (24, 26))
        self.add_polyline('body', (2, 26), (24, 26), (46, 26), (46, 46), (28, 46), (20, 46), (2, 46), closed=True)
        self.add_line('door-left', (20, 46), (20, 39))
        self.add_arc('door-arch', (20, 39), (28, 39), radius_x=4, radius_y=4, sweep=True)
        self.add_line('door-right', (28, 39), (28, 46))
        self.add_contour('door', 'door-left', 'door-arch', 'door-right', closed=False)
        self.add_polyline('left-dome', (2, 26), (2, 16), (6, 10), (10, 16), (10, 26), closed=False)
        self.add_polyline('right-dome', (38, 26), (38, 16), (42, 10), (46, 16), (46, 26), closed=False)
        self.relate("connect", 'onion', 'dome-neck')
        self.relate("connect", 'dome-neck', 'body')
        self.relate("connect", 'body', 'door')
        self.relate("connect", 'body', 'left-dome')
        self.relate("connect", 'body', 'right-dome')
