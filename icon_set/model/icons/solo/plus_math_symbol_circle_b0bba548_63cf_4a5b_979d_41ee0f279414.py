'plus-math-symbol-circle: independent smooth-curve repair.\n\nConstruction: Concentric circular frame; equal cross arms end ten units inside its centerline.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle-plus.svg and atomic-debug/circle-plus.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b0bba548-63cf-4a5b-979d-41ee0f279414'
SOURCE_PATH = 'pictographic-primitives/interface-essential/plus math symbol circle_b0bba548-63cf-4a5b-979d-41ee0f279414.svg'
AUTHOR = 'gpt-6'


class PlusMathSymbolCircle(Solo48):
    icon_id = 'plus-math-symbol-circle'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('plus', 'math', 'symbol', 'circle', 'interface-essential')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'ring',24,24,20)
        line(self,'cross-h',(14,24),(34,24))
        line(self,'cross-v',(24,14),(24,34))
        contacts(self)
