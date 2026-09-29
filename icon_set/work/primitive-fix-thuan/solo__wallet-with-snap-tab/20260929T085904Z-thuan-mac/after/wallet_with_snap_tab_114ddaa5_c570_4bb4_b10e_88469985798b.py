from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '114ddaa5-c570-4bb4-b10e-88469985798b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wallet-with-snap-tab/20260929T085904Z-thuan-mac/reference/wallet_114ddaa5-c570-4bb4-b10e-88469985798b.svg'
AUTHOR = "gpt-6"

# Comparison: The cash opening merged into the wallet silhouette and the snap tab had no fastener.
# Revision: Show a separate angled banknote above a rounded wallet and add a clear snap on its closing tab.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'wallet-with-snap-tab'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('wallet',)

    def build(self):
        path(self,'wallet',(40,23),('L',(40,18)),('A',4,4,False,(36,14)),('L',(8,14)),('A',4,4,False,(4,18)),('L',(4,38)),('A',4,4,False,(8,42)),('L',(36,42)),('A',4,4,False,(40,38)),('L',(40,33)))
        poly(self,'banknote',(9,14),(32,6),(35,14))
        path(self,'snap-tab',(44,23),('L',(33,23)),('A',5,5,False,(33,33)),('L',(44,33)),('L',(44,23)),closed=True)
        self.add_dot('snap',(37,28))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Keep the snap fastener inside its tab and the banknote above the wallet; the 1px snap clearance is visible and the taller envelope preserves the source.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '925173e3b9a986d0349497de414215347dbc55c39ef994f442f6d6c3abebd57e'}
