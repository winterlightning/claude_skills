"""Rooster with scalloped base and three-lobed crown. Lucide bird informs beak attachment. Centerline (5,2)-(43,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbf9d8b6-3b06-5a94-bae2-20a5e5f5188b'
SOURCE_PATH = 'pictographic-primitives/animals/rooster_dbf9d8b6-3b06-5a94-bae2-20a5e5f5188b.svg'
AUTHOR = 'gpt-6'


class RoosterWithScallopedBase(Solo48):
    icon_id = 'rooster-with-scalloped-base'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('rooster', 'cockerel', 'comb', 'wattle', 'beak', 'farm', 'poultry', 'bird')

    def build(self) -> None:
        self.add_arc('body-1', (5, 25), (17, 13), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('body-2', (17, 13), (29, 25), radius_x=12, radius_y=12, sweep=True)
        self.add_line('body-3', (29, 25), (29, 40))
        self.add_arc('body-4', (29, 40), (23, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('body-5', (23, 46), (17, 40), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('body-6', (17, 40), (11, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('body-7', (11, 46), (5, 40), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-8', (5, 40), (5, 25))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', closed=True)
        self.add_arc('comb-1', (9, 16), (7, 6), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('comb-2', (7, 6), (15, 6), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('comb-3', (15, 6), (23, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('comb-4', (23, 6), (31, 6), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('comb-5', (31, 6), (27, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('comb', 'comb-1', 'comb-2', 'comb-3', 'comb-4', 'comb-5', closed=False)
        self.relate("connect", 'body', 'comb')
        self.add_line('beak-1', (29, 23), (43, 34))
        self.add_line('beak-2', (43, 34), (29, 34))
        self.add_contour('beak', 'beak-1', 'beak-2', closed=False)
        self.relate("connect", 'body', 'beak')
        self.add_arc('wattle-1', (29, 34), (36, 39), radius_x=7, radius_y=5, sweep=True)
        self.add_arc('wattle-2', (36, 39), (29, 44), radius_x=7, radius_y=5, sweep=True)
        self.add_contour('wattle', 'wattle-1', 'wattle-2', closed=False)
        self.relate("connect", 'body', 'wattle')
        self.relate("connect", 'beak', 'wattle')
        self.add_dot('eye', (20, 26))
