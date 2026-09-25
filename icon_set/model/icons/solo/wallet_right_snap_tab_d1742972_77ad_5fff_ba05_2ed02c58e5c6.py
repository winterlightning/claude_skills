"""Simple Pocket Wallet."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1742972-77ad-5fff-ba05-2ed02c58e5c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/crypto wallet_d1742972-77ad-5fff-ba05-2ed02c58e5c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wallet-right-snap-tab'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    categories = ('primitives', 'finance')
    aliases = ()
    keywords = ('wallet', 'pocket', 'money', 'tab', 'leather', 'accessory', 'closed')

    def build(self):
        # Plan: Rounded wallet owns the right capsule tab; pocket seam meets split left wall. Lucide wallet: tangent round corners and inset clasp. Bounds (4,8)-(44,40).
        self.add_line('top',(10,8),(38,8))
        self.add_arc('tr',(38,8),(44,14),radius_x=6)
        self.add_line('r1',(44,14),(44,20))
        self.add_line('r2',(44,20),(44,30))
        self.add_line('r3',(44,30),(44,34))
        self.add_arc('br',(44,34),(38,40),radius_x=6)
        self.add_line('bottom',(38,40),(10,40))
        self.add_arc('bl',(10,40),(4,34),radius_x=6)
        self.add_line('left1',(4,34),(4,17))
        self.add_line('left2',(4,17),(4,14))
        self.add_arc('tl',(4,14),(10,8),radius_x=6)
        self.add_contour('body','top','tr','r1','r2','r3','br','bottom','bl','left1','left2','tl',closed=True)
        self.add_line('pocket',(4,17),(24,17))
        self.relate('connect','pocket','body')
        self.add_line('tabtop',(44,20),(34,20))
        self.add_arc('tabend',(34,20),(34,30),radius_x=5,sweep=False)
        self.add_line('tabbottom',(34,30),(44,30))
        self.add_contour('tab','tabtop','tabend','tabbottom')
        self.relate('connect','tab','body')
