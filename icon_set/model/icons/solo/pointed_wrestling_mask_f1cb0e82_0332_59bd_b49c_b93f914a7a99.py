'A pointed lucha libre wrestling mask.\nConstruction: Vertical centerlines (8,6)-(40,42) suit an upright head. Mirrored angled eye slits and mouth remain; rounded mask retains a central crown seam, pointed mask retains its V crown. Remove closed eye loops, doubled jaw surrounds and fine forehead decoration.\nLucide: No useful exact match; mirrored eyes within one smooth head contour.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1cb0e82-0332-59bd-b49c-b93f914a7a99'
SOURCE_PATH = 'pictographic-primitives/sports/wrestling mask_f1cb0e82-0332-59bd-b49c-b93f914a7a99.svg'
AUTHOR = 'gpt-6'

class PointedWrestlingMask(Solo48):
    icon_id = 'pointed-wrestling-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('pointed', 'wrestling', 'mask', 'sport')

    def build(self):
        self.add_line('crown-1', (8, 28), (8, 6))
        self.add_line('crown-2', (8, 6), (24, 14))
        self.add_line('crown-3', (24, 14), (40, 6))
        self.add_line('crown-4', (40, 6), (40, 28))
        self.add_arc('chin', (40, 28), (8, 28), radius_x=16, radius_y=16, sweep=True)
        self.add_contour('outline', 'crown-1', 'crown-2', 'crown-3', 'crown-4', 'chin', closed=True)
        self.add_line('eye-left', (17, 21), (20, 24))
        self.add_line('eye-right', (31, 21), (28, 24))
        self.add_line('mouth', (21, 35), (27, 35))
