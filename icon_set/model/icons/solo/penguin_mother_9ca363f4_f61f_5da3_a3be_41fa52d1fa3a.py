"""Bent head and downward bill distinguish this tall penguin. Lucide bird informs arc-led head geometry. Ground line omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ca363f4-f61f-5da3-a3be-41fa52d1fa3a'
SOURCE_PATH = 'pictographic-primitives/animals/penguin mother_9ca363f4-f61f-5da3-a3be-41fa52d1fa3a.svg'
AUTHOR = 'gpt-6'


class PenguinLookingDown(Solo48):
    icon_id = 'penguin-looking-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('penguin', 'bending', 'looking', 'down', 'bird', 'antarctic', 'nurture', 'care')

    def build(self) -> None:
        self.add_arc('outline-1', (8, 18), (20, 2), radius_x=12, radius_y=16, sweep=True)
        self.add_arc('outline-2', (20, 2), (35, 17), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('outline-3', (35, 17), (37, 39), radius_x=70, radius_y=70, sweep=True)
        self.add_line('outline-4', (37, 39), (40, 46))
        self.add_line('outline-5', (40, 46), (27, 46))
        self.add_arc('outline-6', (27, 46), (20, 18), radius_x=15, radius_y=35, sweep=True)
        self.add_line('outline-7', (20, 18), (12, 27))
        self.add_line('outline-8', (12, 27), (8, 18))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', closed=True)
        self.add_dot('eye', (18, 12))
