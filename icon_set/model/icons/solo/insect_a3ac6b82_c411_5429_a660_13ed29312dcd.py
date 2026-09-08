"""Right-facing rhinoceros beetle with a domed shell and long rising horn. Centerline extremes (2,5)-(46,43). Profile is deliberately asymmetric; narrow horn gap opened and legs simplified, using Lucide bug attachment principles."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3ac6b82-c411-5429-a660-13ed29312dcd'
SOURCE_PATH = 'pictographic-primitives/animals/insect_a3ac6b82-c411-5429-a660-13ed29312dcd.svg'
AUTHOR = 'gpt-6'


class RhinocerosBeetle(Solo48):
    icon_id = 'rhinoceros-beetle'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('beetle', 'rhinoceros beetle', 'horn', 'insect', 'bug', 'shell', 'legs', 'nature')

    def build(self) -> None:
        self.add_arc('shell', (2, 33), (32, 33), radius_x=15, radius_y=17, sweep=True)
        self.add_line('belly-r', (32, 33), (24, 33))
        self.add_line('belly-m', (24, 33), (10, 33))
        self.add_line('belly-l', (10, 33), (2, 33))
        self.add_contour('body', 'shell', 'belly-r', 'belly-m', 'belly-l', closed=True)
        self.add_arc('horn-back', (32, 33), (43, 5), radius_x=11, radius_y=28, sweep=True)
        self.add_arc('horn-hollow', (43, 5), (46, 23), radius_x=10, radius_y=10, sweep=False)
        self.add_line('head-front', (46, 23), (46, 28))
        self.add_arc('head-chin', (46, 28), (38, 36), radius_x=8, radius_y=8, sweep=True)
        self.add_line('head-base', (38, 36), (32, 33))
        self.add_contour('head', 'horn-back', 'horn-hollow', 'head-front', 'head-chin', 'head-base', closed=False)
        self.relate("connect", 'body', 'head')
        self.add_line('leg-0', (10, 33), (7, 43))
        self.relate("connect", 'body', 'leg-0')
        self.add_line('leg-1', (24, 33), (21, 43))
        self.relate("connect", 'body', 'leg-1')
        self.add_line('leg-2', (32, 33), (34, 43))
        self.relate("connect", 'body', 'leg-2')
        self.relate("connect", 'head', 'leg-2')
