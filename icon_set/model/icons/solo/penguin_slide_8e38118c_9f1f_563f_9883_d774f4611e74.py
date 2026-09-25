'Sliding penguin: preserve the low curled body, round head and icy slope; omit the cramped interior flipper.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e38118c-9f1f-563f-9883-d774f4611e74'
SOURCE_PATH = 'pictographic-primitives/animals/penguin slide_8e38118c-9f1f-563f-9883-d774f4611e74.svg'
AUTHOR = 'gpt-6'


class SlidingPenguin(Solo48):
    icon_id = 'sliding-penguin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('penguin', 'slide', 'sliding', 'snow', 'slope', 'ice', 'antarctic', 'motion')

    def build(self) -> None:
        self.add_bezier('rear',(6,14),((6,9),(9,6),(14,6)),((20,6),(23,12),(24,17)))
        self.add_arc('head',(24,17),(42,17),radius_x=9)
        self.add_bezier('front',(42,17),((42,23),(40,26),(35,28)))
        self.add_bezier('belly',(35,28),((28,31),(18,28),(14,26)),((9,23),(6,19),(6,14)))
        self.add_contour('body','rear','head','front','belly',closed=True)
        self.add_line('foot',(14,6),(6,6));self.relate('connect','foot','body')
        self.add_dot('eye',(33,17))
        self.add_line('slope',(6,36),(42,42))
