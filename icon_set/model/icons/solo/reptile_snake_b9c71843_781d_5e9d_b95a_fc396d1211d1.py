"""Flat switchback snake with a rounded hanging head. The source supplies pose; small eyes are omitted. Centerline extremes (2,2)-(46,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9c71843-781d-5e9d-b95a-fc396d1211d1'
SOURCE_PATH = 'pictographic-primitives/animals/reptile snake_b9c71843-781d-5e9d-b95a-fc396d1211d1.svg'
AUTHOR = 'gpt-6'


class SlitheringSnake(Solo48):
    icon_id = 'slithering-snake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('snake', 'slither', 'serpent', 'reptile', 'zigzag', 'coil', 'python', 'wild')

    def build(self) -> None:
        self.add_line('body-1', (14, 16), (8, 16))
        self.add_arc('body-2', (8, 16), (2, 22), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('body-3', (2, 22), (8, 28), radius_x=6, radius_y=6, sweep=False)
        self.add_line('body-4', (8, 28), (14, 28))
        self.add_arc('body-5', (14, 28), (18, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_line('body-6', (18, 32), (18, 39))
        self.add_arc('body-7', (18, 39), (24, 46), radius_x=6, radius_y=7, sweep=False)
        self.add_arc('body-8', (24, 46), (30, 39), radius_x=6, radius_y=7, sweep=False)
        self.add_line('body-9', (30, 39), (28, 31))
        self.add_arc('body-10', (28, 31), (32, 26), radius_x=5, radius_y=5, sweep=True)
        self.add_line('body-11', (32, 26), (39, 26))
        self.add_arc('body-12', (39, 26), (46, 19), radius_x=7, radius_y=7, sweep=False)
        self.add_arc('body-13', (46, 19), (39, 12), radius_x=7, radius_y=7, sweep=False)
        self.add_line('body-14', (39, 12), (22, 12))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', 'body-13', 'body-14', closed=False)
        self.add_arc('tail-1', (14, 16), (10, 10), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('tail-2', (10, 10), (18, 2), radius_x=8, radius_y=8, sweep=True)
        self.add_line('tail-3', (18, 2), (38, 2))
        self.add_arc('tail-4', (38, 2), (30, 12), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('tail', 'tail-1', 'tail-2', 'tail-3', 'tail-4', closed=False)
        self.relate("connect", 'body', 'tail')
