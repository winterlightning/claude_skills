"""Blocky tyrannosaurus with squared muzzle and hooked claw. Centerlines (2,5)-(46,43). Deliberately angular and asymmetric; one tooth replaces fine bars."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '072fa441-e2e2-5dcb-8d2a-fb466edee694'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur trex_072fa441-e2e2-5dcb-8d2a-fb466edee694.svg'
AUTHOR = 'gpt-6'


class BlockyTrexHead(Solo48):
    icon_id = 'blocky-trex-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('trex', 'tyrannosaurus', 'dinosaur', 'head', 'teeth', 'geometric', 'prehistoric', 'jaw')

    def build(self) -> None:
        self.add_line('muzzle', (2,22), (2,16))
        self.add_arc('front-corner', (2,16), (10,8), radius_x=8)
        self.add_line('brow-step', (10,8), (17,8))
        self.add_arc('brow', (17,8), (28,5), radius_x=11, radius_y=3)
        self.add_arc('skull', (28,5), (40,10), radius_x=12, radius_y=5)
        self.add_line('back', (40,10), (46,15))
        self.add_contour('upper','muzzle','front-corner','brow-step','brow','skull','back')
        self.add_polyline('mouth', (2,22), (12,22), (12,17))
        self.add_line('mouth-end', (12,22), (23,22))
        self.relate('connect','mouth','mouth-end')
        self.relate('connect','upper','mouth')
        self.add_arc('chin', (2,22), (10,30), radius_x=8,sweep=False)
        self.add_line('jaw', (10,30), (24,30))
        self.add_line('throat', (24,30), (31,34))
        self.add_contour('lower','chin','jaw','throat')
        self.relate('connect','mouth','lower')
        self.add_polyline('claw', (31,34), (38,36), (35,43))
        self.relate('connect','lower','claw')
        self.add_line('neck-back', (46,15), (46,39))
        self.add_line('shoulder', (46,39), (38,36))
        self.add_contour('neck','neck-back','shoulder')
        self.relate('connect','upper','neck')
        self.relate('connect','claw','neck')
        self.add_dot('eye', (29,16))
