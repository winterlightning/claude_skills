'rectangle-remove-state: independent smooth-curve repair.\n\nConstruction: Rounded vertical frame with equal corner radii; centered controls or a shared sidebar divider retain the original panel meaning.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5c4ca37f-144e-4809-8a31-ca31fdd14824'
SOURCE_PATH = 'pictographic-primitives/state/rectangle remove_5c4ca37f-144e-4809-8a31-ca31fdd14824.svg'
AUTHOR = 'gpt-6'


class RectangleRemoveState(Solo48):
    icon_id = 'rectangle-remove-state'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rectangle', 'remove', 'state')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'frame',4,8,44,40,4,xs=(32,),ys=(24,))
        line(self,'cross-a',(19,18),(29,30))
        line(self,'cross-b',(19,30),(29,18))
        contacts(self)
