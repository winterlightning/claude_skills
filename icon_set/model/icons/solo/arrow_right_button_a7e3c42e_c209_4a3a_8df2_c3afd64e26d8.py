'arrow-right-button: independent smooth-curve repair.\n\nConstruction: Outlined chevron with exact horizontal symmetry; preserve its arrow silhouette.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/chevron-right.svg and atomic-debug/chevron-right.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a7e3c42e-c209-4a3a-8df2-c3afd64e26d8'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow right button_a7e3c42e-c209-4a3a-8df2-c3afd64e26d8.svg'
AUTHOR = 'gpt-6'


class ArrowRightButton(Solo48):
    icon_id = 'arrow-right-button'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'right', 'button', 'symbol')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'chevron',(8,4),(20,4),(40,24),(20,44),(8,44),(28,24),(8,4),closed=True)
        contacts(self)
