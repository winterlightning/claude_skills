'three-dots-horizontal: independent smooth-curve repair.\n\nConstruction: Three equally spaced dots in a rounded field; shared centers and equal radii.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/ellipsis.svg and atomic-debug/ellipsis.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '50252b7f-b14c-4f4f-85f4-62a07a034258'
SOURCE_PATH = 'pictographic-primitives/state/three dots horizontal_50252b7f-b14c-4f4f-85f4-62a07a034258.svg'
AUTHOR = 'gpt-6'


class ThreeDotsHorizontalVariant2(Solo48):
    icon_id = 'three-dots-horizontal-v2'
    variant_of = 'three-dots-horizontal'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('three', 'dots', 'horizontal', 'state')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'field',4,8,44,40,5)
        for i,x in enumerate((13,24,35)): self.add_dot(f'dot-{i}',(x,24))
        contacts(self)
