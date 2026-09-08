"""Two interlocking diagonal chain links. Lucide link informs open capsule ends that describe the overlap without crossed strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c06efbf-f3f5-4fe4-88b2-7fb4d1d00885'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/chain_7c06efbf-f3f5-4fe4-88b2-7fb4d1d00885.svg'
AUTHOR = 'astra-chatgpt'

class InterlockingChainLinks(Solo48):
    icon_id = 'interlocking-chain-links'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('interlocking', 'chain', 'links')

    def build(self) -> None:
        # Centerline extremes (2,2)-(46,46); opposed open capsules.
        self.add_arc("lower-inner", (28,20), (12,20), radius_x=10, sweep=False)
        self.add_line("lower-left", (12,20), (6,28))
        self.add_arc("lower-outer", (6,28), (18,44), radius_x=10, sweep=False)
        self.add_line("lower-tip", (18,44), (22,39))
        self.add_contour("lower-link", "lower-inner", "lower-left", "lower-outer", "lower-tip")
        self.add_arc("upper-inner", (20,28), (36,28), radius_x=10, sweep=False)
        self.add_line("upper-right", (36,28), (42,20))
        self.add_arc("upper-outer", (42,20), (30,4), radius_x=10, sweep=False)
        self.add_line("upper-tip", (30,4), (26,9))
        self.add_contour("upper-link", "upper-inner", "upper-right", "upper-outer", "upper-tip")
