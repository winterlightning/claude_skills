'warp-arch: independent smooth-curve repair.\n\nConstruction: Warped arch frame with three matching smooth bows; equal vertical offsets preserve spacious bands.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'bdc7edeb-0efe-4644-960d-7671381627e9'
SOURCE_PATH = 'pictographic-primitives/design/warp arch_bdc7edeb-0efe-4644-960d-7671381627e9.svg'
AUTHOR = 'gpt-6'


class WarpArch(Solo48):
    icon_id = 'warp-arch'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'arch', 'design')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'outline',(4,18),('C',(16,4.666666667),(32,4.666666667),(44,18)),('L',(44,40)),('C',(32,26.666666667),(16,26.666666667),(4,40)),('L',(4,18)),closed=True)
        path(self,'middle',(4,29),('C',(16,15.666666667),(32,15.666666667),(44,29)))
        contacts(self)
