"""A diagonal security scanner wand emits signals. No useful exact Lucide match; scan-line informs reducing scanning detail to clean strokes. Keep one arc on either side, replacing two pairs; simplify handle thickness. Deliberate diagonal orientation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58f838b1-c66c-4ee9-8046-26e151660ee4'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance camera moving_58f838b1-c66c-4ee9-8046-26e151660ee4.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'security-scanner-wand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('security', 'wand', 'scanner', 'metal detector', 'screening', 'handheld', 'signal', 'checkpoint')

    def build(self):
        # SQUARE centerline extremes (6, 6, 42, 42).

        # Diagonal detector head owns one-line handle; paired signal arcs are intrinsic emission.
        self.add_polyline('head',(16,24),(32,8),(40,16),(24,32),(20,28),closed=True)
        self.add_line('handle',(20,28),(6,42))
        self.relate('connect','handle','head')
        self.add_arc('signal-left',(6,20),(20,6),radius_x=14)
        self.add_arc('signal-right',(42,28),(28,42),radius_x=14)
