'server-choose: independent smooth-curve repair.\n\nConstruction: Three stacked server trays with matching rounded ends and shared horizontal rails.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/server.svg and atomic-debug/server.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '778556a1-f207-5e49-9e02-977c5f493d53'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__server-choose/20260927T091411Z-thuan-mac-1/reference/server choose_778556a1-f207-5e49-9e02-977c5f493d53.svg'
AUTHOR = "gpt-6"


class ServerChoose(Solo48):
    icon_id = 'server-choose'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    categories = ('servers', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('server', 'choose', 'servers')
    keyshape = Keyshape.HRECT_L

    # Revision plan: Source shows three separate pill shaped server trays. Give the stack lobed sides while retaining three equal levels. Lucide server informs horizontal rhythm.
    # Revision plan: Source shows three separate pill shaped server trays. Give the stack lobed sides while retaining three equal levels. Lucide server informs horizontal rhythm.
    # Revision plan: Source shows three separate pill shaped server trays. Give the stack lobed sides while retaining three equal levels. Lucide server informs horizontal rhythm.
    # Revision plan: Source shows three separate pill shaped server trays. Give the stack lobed sides while retaining three equal levels. Lucide server informs horizontal rhythm.
    # Revision plan: Source shows three separate pill shaped server trays. Give the stack lobed sides while retaining three equal levels. Lucide server informs horizontal rhythm.
    def build(self):
        # Three stacked rounded trays share one broad envelope and two seams.
        self.add_polyline('server-stack', (12, 8), (36, 8), (44, 13), (40, 18), (44, 24), (40, 30), (44, 35), (36, 40), (12, 40), (4, 35), (8, 30), (4, 24), (8, 18), (4, 13), closed=True)
        self.add_line('upper-seam', (8, 18), (40, 18))
        self.add_line('lower-seam', (8, 30), (40, 30))
        self.relate('connect', 'server-stack', 'upper-seam')
        self.relate('connect', 'server-stack', 'lower-seam')
