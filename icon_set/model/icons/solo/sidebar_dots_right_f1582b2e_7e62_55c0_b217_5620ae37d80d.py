'sidebar-dots-right: independent smooth-curve repair.\n\nConstruction: Rounded vertical frame with equal corner radii; centered controls or a shared sidebar divider retain the original panel meaning.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/rectangle-horizontal.svg and atomic-debug/rectangle-horizontal.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f1582b2e-7e62-55c0-b217-5620ae37d80d'
SOURCE_PATH = 'pictographic-primitives/apps/sidebar dots right_f1582b2e-7e62-55c0-b217-5620ae37d80d.svg'
AUTHOR = 'gpt-6'


class SidebarDotsRight(Solo48):
    icon_id = 'sidebar-dots-right'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('sidebar', 'dots', 'right', 'apps')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'frame',4,8,44,40,4,xs=(32,),ys=(24,))
        line(self,'sidebar',(32,8),(32,40))
        contacts(self)
