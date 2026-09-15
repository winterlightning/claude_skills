'warp-fisheye: independent smooth-curve repair.\n\nConstruction: Fisheye panel with an evenly rounded border and a concentric circular lens.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'fd7cd327-9177-528e-8a97-5ea387ee5601'
SOURCE_PATH = 'pictographic-primitives/design/warp fisheye_fd7cd327-9177-528e-8a97-5ea387ee5601.svg'
AUTHOR = 'gpt-6'


class WarpFisheyeVariant2(Solo48):
    icon_id = 'warp-fisheye-v2'
    variant_of = 'warp-fisheye'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'fisheye', 'design')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'frame',4,8,44,40,5)
        ellipse(self,'lens',24,24,7)
        contacts(self)
