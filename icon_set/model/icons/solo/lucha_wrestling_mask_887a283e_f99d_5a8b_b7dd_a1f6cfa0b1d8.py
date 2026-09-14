'A rounded lucha libre wrestling mask.\nConstruction: Vertical centerlines (8,6)-(40,42) suit an upright head. Mirrored angled eye slits and mouth remain; rounded mask retains a central crown seam, pointed mask retains its V crown. Remove closed eye loops, doubled jaw surrounds and fine forehead decoration.\nLucide: No useful exact match; mirrored eyes within one smooth head contour.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '887a283e-f99d-5a8b-b7dd-a1f6cfa0b1d8'
SOURCE_PATH = 'pictographic-primitives/sports/wrestling mask_887a283e-f99d-5a8b-b7dd-a1f6cfa0b1d8.svg'
AUTHOR = 'gpt-6'

class LuchaWrestlingMask(Solo48):
    icon_id = 'lucha-wrestling-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('lucha', 'wrestling', 'mask', 'sport')

    def build(self):
        self.add_arc('top-l', (8, 20), (24, 6), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('top-r', (24, 6), (40, 20), radius_x=16, radius_y=16, sweep=True)
        self.add_line('r', (40, 20), (40, 28))
        self.add_arc('bottom', (40, 28), (8, 28), radius_x=16, radius_y=16, sweep=True)
        self.add_line('l', (8, 28), (8, 20))
        self.add_contour('outline', 'top-l', 'top-r', 'r', 'bottom', 'l', closed=True)
        self.add_line('mask-seam', (24, 6), (24, 12))
        self.relate("connect", 'mask-seam', 'outline')
        self.add_line('eye-left', (17, 21), (20, 24))
        self.add_line('eye-right', (31, 21), (28, 24))
        self.add_line('mouth', (21, 35), (27, 35))
