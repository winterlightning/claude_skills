"""A house-shaped clock with two hands above a hanging pendulum; nested dial and opening frames omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4034b865-e266-493a-bb67-569bf497aecd'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/clock retro_4034b865-e266-493a-bb67-569bf497aecd.svg'
AUTHOR = 'gpt-6'


class HouseShapedPendulumClock(Solo48):
    icon_id = 'house-shaped-pendulum-clock'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('clock', 'pendulum', 'retro', 'time', 'mantel', 'house', 'case')

    def build(self) -> None:
        self.add_polyline('case',(8,44),(8,44),(8,14),(24,4),(40,14),(40,44),(40,44))
        self.add_line('base',(8,44),(40,44))
        self.relate('connect','case','base')
        self.add_polyline('hands',(24,14),(24,19),(30,19))
        self.add_line('pendulum-stem',(24,27),(24,30))
        self.add_arc('bob-a',(24,30),(24,36),radius_x=3)
        self.add_arc('bob-b',(24,36),(24,30),radius_x=3)
        self.add_contour('bob','bob-a','bob-b',closed=True)
        self.relate('connect','pendulum-stem','bob')
