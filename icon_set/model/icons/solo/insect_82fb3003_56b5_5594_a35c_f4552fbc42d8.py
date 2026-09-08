"""Symmetric top-view beetle with six legs, antennae and a divided wing case. Centerline extremes (5,2)-(43,46). Lucide bug informs the capsule and radial leg connections. Thorax band reduced to a single head/body boundary."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82fb3003-56b5-5594-a35c-f4552fbc42d8'
SOURCE_PATH = 'pictographic-primitives/animals/insect_82fb3003-56b5-5594-a35c-f4552fbc42d8.svg'
AUTHOR = 'gpt-6'


class Beetle(Solo48):
    icon_id = 'beetle'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('beetle', 'bug', 'insect', 'shell', 'antennae', 'legs', 'nature', 'wildlife')

    def build(self) -> None:
        self.add_arc('head-top', (16, 14), (32, 14), radius_x=8, radius_y=8, sweep=True)
        self.add_line('head-right', (32, 14), (32, 20))
        self.add_line('head-base-r', (32, 20), (24, 20))
        self.add_line('head-base-l', (24, 20), (16, 20))
        self.add_line('head-left', (16, 20), (16, 14))
        self.add_contour('head', 'head-top', 'head-right', 'head-base-r', 'head-base-l', 'head-left', closed=True)
        self.add_arc('shoulder-l', (16, 20), (13, 25), radius_x=5, radius_y=5, sweep=True)
        self.add_line('wall-l-0', (13, 25), (13, 32))
        self.add_line('wall-l-1', (13, 32), (13, 39))
        self.add_arc('base-l', (13, 39), (24, 46), radius_x=11, radius_y=7, sweep=True)
        self.add_contour('wing-l', 'shoulder-l', 'wall-l-0', 'wall-l-1', 'base-l', closed=False)
        self.relate("connect", 'head', 'wing-l')
        self.add_polyline('leg-l-0', (13, 25), (5, 22))
        self.relate("connect", 'wing-l', 'leg-l-0')
        self.add_polyline('leg-l-1', (13, 32), (5, 32))
        self.relate("connect", 'wing-l', 'leg-l-1')
        self.add_polyline('leg-l-2', (13, 39), (5, 42))
        self.relate("connect", 'wing-l', 'leg-l-2')
        self.add_line('antenna-l', (16, 14), (12, 2))
        self.relate("connect", 'head', 'antenna-l')
        self.add_arc('shoulder-r', (32, 20), (35, 25), radius_x=5, radius_y=5, sweep=False)
        self.add_line('wall-r-0', (35, 25), (35, 32))
        self.add_line('wall-r-1', (35, 32), (35, 39))
        self.add_arc('base-r', (35, 39), (24, 46), radius_x=11, radius_y=7, sweep=False)
        self.add_contour('wing-r', 'shoulder-r', 'wall-r-0', 'wall-r-1', 'base-r', closed=False)
        self.relate("connect", 'head', 'wing-r')
        self.add_polyline('leg-r-0', (35, 25), (43, 22))
        self.relate("connect", 'wing-r', 'leg-r-0')
        self.add_polyline('leg-r-1', (35, 32), (43, 32))
        self.relate("connect", 'wing-r', 'leg-r-1')
        self.add_polyline('leg-r-2', (35, 39), (43, 42))
        self.relate("connect", 'wing-r', 'leg-r-2')
        self.add_line('antenna-r', (32, 14), (36, 2))
        self.relate("connect", 'head', 'antenna-r')
        self.add_line('seam', (24, 20), (24, 46))
        self.relate("connect", 'head', 'seam')
        self.relate("connect", 'wing-l', 'wing-r')
        self.relate("connect", 'wing-l', 'seam')
        self.relate("connect", 'wing-r', 'seam')
