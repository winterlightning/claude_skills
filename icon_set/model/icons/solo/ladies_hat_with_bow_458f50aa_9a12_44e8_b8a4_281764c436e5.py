'ladies-hat-with-bow: Narrowed the brim and enlarged both bow openings. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '458f50aa-9a12-44e8-b8a4-281764c436e5'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/hat lady_458f50aa-9a12-44e8-b8a4-281764c436e5.svg'
AUTHOR = 'gpt-6'

class LadiesHatWithBow(Solo48):
    icon_id = 'ladies-hat-with-bow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('ladies', 'hat', 'with', 'bow')

    def build(self) -> None:
        self.add_arc('crown', (8, 26), (36, 26), radius_x=14, radius_y=18)
        self.add_line('brim-left', (8, 26), (4, 34))
        self.add_arc('brim-lower-left', (4, 34), (24, 40), radius_x=20, radius_y=6, sweep=False)
        self.add_arc('brim-lower-right', (24, 40), (44, 34), radius_x=20, radius_y=6, sweep=False)
        self.add_line('brim-right', (44, 34), (40, 28))
        self.add_contour('brim', 'brim-left', 'brim-lower-left', 'brim-lower-right', 'brim-right')
        self.add_line('band', (8, 26), (24, 26))
        self.add_polyline('bow-left', (34, 26), (24, 18), (24, 26), (24, 34), closed=True)
        self.add_polyline('bow-right', (34, 26), (44, 18), (44, 34), closed=True)
        self.relate('connect', 'crown', 'brim')
        self.relate('connect', 'crown', 'band')
        self.relate('connect', 'brim', 'band')
        self.relate('connect', 'bow-left', 'bow-right')
        self.relate('connect', 'band', 'bow-left')
