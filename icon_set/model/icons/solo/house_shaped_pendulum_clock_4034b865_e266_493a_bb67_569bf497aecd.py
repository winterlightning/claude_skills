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
        self.add_polyline('case',(5,46),(8,46),(8,14),(24,2),(40,14),(40,46),(43,46))
        self.add_line('base',(8,46),(40,46))
        self.relate('connect','case','base')
        self.add_polyline('hands',(24,12),(24,20),(30,20))
        self.add_line('pendulum-stem',(24,30),(24,33))
        self.add_arc('bob-a',(24,33),(24,39),radius_x=3)
        self.add_arc('bob-b',(24,39),(24,33),radius_x=3)
        self.add_contour('bob','bob-a','bob-b',closed=True)
        self.relate('connect','pendulum-stem','bob')
