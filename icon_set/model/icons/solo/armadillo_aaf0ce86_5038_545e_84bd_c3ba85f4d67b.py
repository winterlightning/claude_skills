"""Armadillo with domed shell; centerline extremes (2,11)-(46,37). One shell band and two near legs retained; extra bands and overlapping legs omitted. No useful Lucide match; directional head and tail remain asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aaf0ce86-5038-545e-84bd-c3ba85f4d67b'
SOURCE_PATH = 'pictographic-primitives/animals/armadillo_aaf0ce86-5038-545e-84bd-c3ba85f4d67b.svg'
AUTHOR = 'gpt-6'


class Armadillo(Solo48):
    icon_id = 'armadillo'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('armadillo', 'animal', 'shell', 'armour', 'mammal', 'wildlife', 'banded', 'desert')

    def build(self) -> None:
        # Armadillo with domed shell; centerline extremes (2,11)-(46,37). One shell band and two near legs retained; extra bands and overlapping legs omitted. No useful Lucide match; directional head and tail remain asymmetric.
        self.add_arc('shell-top-left', (14, 29), (28, 11), radius_x=14, radius_y=18, sweep=True)
        self.add_arc('shell-top-right', (28, 11), (42, 29), radius_x=14, radius_y=18, sweep=True)
        self.add_line('bottom-right', (42, 29), (35, 32))
        self.add_line('bottom-mid-right', (35, 32), (28, 32))
        self.add_line('bottom-mid-left', (28, 32), (18, 32))
        self.add_line('bottom-left', (18, 32), (14, 29))
        self.add_contour('shell', 'shell-top-left', 'shell-top-right', 'bottom-right', 'bottom-mid-right', 'bottom-mid-left', 'bottom-left', closed=True)
        self.add_polyline('head', (14, 29), (7, 29), (2, 25), (8, 20), (8, 14), (13, 19), closed=False)
        self.relate("connect", 'head', 'shell')
        self.add_line('band', (28, 11), (28, 32))
        self.relate("connect", 'band', 'shell')
        self.add_polyline('tail', (42, 29), (44, 34), (46, 35), closed=False)
        self.relate("connect", 'tail', 'shell')
        self.add_polyline('front-leg', (18, 32), (17, 37), (14, 37), closed=False)
        self.add_polyline('back-leg', (35, 32), (36, 37), (39, 37), closed=False)
        self.relate("connect", 'front-leg', 'shell')
        self.relate("connect", 'back-leg', 'shell')
