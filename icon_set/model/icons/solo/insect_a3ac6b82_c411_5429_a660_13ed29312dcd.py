"""Right-facing rhinoceros beetle with a domed shell and long rising horn. Centerline extremes (6,6)-(42,42). Profile is deliberately asymmetric; narrow horn gap opened and legs simplified, using Lucide bug attachment principles."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3ac6b82-c411-5429-a660-13ed29312dcd'
SOURCE_PATH = 'pictographic-primitives/animals/insect_a3ac6b82-c411-5429-a660-13ed29312dcd.svg'
AUTHOR = 'gpt-6'


class RhinocerosBeetle(Solo48):
    icon_id = 'rhinoceros-beetle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('beetle', 'rhinoceros beetle', 'horn', 'insect', 'bug', 'shell', 'legs', 'nature')

    def build(self) -> None:
        self.add_arc('shell',(6,33),(32,33),radius_x=13,radius_y=12)
        self.add_line('belly-r', (32, 33), (24, 33))
        self.add_line('belly-m', (24, 33), (10, 33))
        self.add_line('belly-l', (10, 33), (6, 33))
        self.add_contour('body', 'shell', 'belly-r', 'belly-m', 'belly-l', closed=True)
        self.add_arc('horn-back', (32, 33), (42, 6), radius_x=11, radius_y=28, sweep=True)
        self.add_arc('horn-hollow', (42, 6), (42, 23), radius_x=10, radius_y=10, sweep=False)
        self.add_line('head-front', (42, 23), (42, 28))
        self.add_bezier('head-chin', (42, 28), *(((42, 31.2325716), (40.83874454, 34.39737339), (38, 36)),))
        self.add_line('head-base', (38, 36), (32, 33))
        self.add_contour('head', 'horn-back', 'horn-hollow', 'head-front', 'head-chin', 'head-base', closed=False)
        self.relate("connect", 'body', 'head')
        self.add_line('leg-0', (10, 33), (7, 42))
        self.relate("connect", 'body', 'leg-0')
        self.add_line('leg-1', (24, 33), (21, 42))
        self.relate("connect", 'body', 'leg-1')
        self.add_line('leg-2', (32, 33), (34, 42))
        self.relate("connect", 'body', 'leg-2')
        self.relate("connect", 'head', 'leg-2')
