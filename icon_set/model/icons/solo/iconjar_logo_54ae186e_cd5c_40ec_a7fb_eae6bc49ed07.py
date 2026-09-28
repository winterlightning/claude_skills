"""A rounded jar with a curvy body and a separate lid topped by a small twisted knob.

Plan: Symmetric curved jar and separate domed lid with centered knob.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: bot: shared radii and simplified enclosed body.
Simplification: Twisted knob and arched lid reduce to centered handle and horizontal lid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54ae186e-cd5c-40ec-a7fb-eae6bc49ed07'
SOURCE_PATH = 'pictographic-primitives/logos/iconjar logo_54ae186e-cd5c-40ec-a7fb-eae6bc49ed07.svg'
AUTHOR = 'gpt-6'


class IconjarLogo(Solo48):
    icon_id = 'iconjar-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('iconjar', 'jar', 'icons', 'logo', 'brand', 'organizer', 'design')

    def build(self):
        self.add_polyline('lid',(10,12),(24,12),(38,12))
        self.add_line('knob',(24,4),(24,12))
        self.relate('connect','lid','knob')
        self.add_line('rim',(8,21),(40,21))
        self.add_bezier('right',(40,21),((30,29),(40,29),(36,39)),((35,43),(33,44),(30,44)))
        self.add_line('base',(30,44),(18,44))
        self.add_bezier('left',(18,44),((15,44),(13,43),(12,39)),((8,29),(18,29),(8,21)))
        self.add_contour('jar','rim','right','base','left',closed=True)
