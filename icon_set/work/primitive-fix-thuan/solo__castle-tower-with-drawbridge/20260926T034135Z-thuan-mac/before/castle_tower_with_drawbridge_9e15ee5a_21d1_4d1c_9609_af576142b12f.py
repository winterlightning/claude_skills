"""A castle tower lowers a drawbridge over water. Lucide castle informs the battlement and tower. Keep intentional right-heavy asymmetry; simplify chain to one line, window to slit and water to one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e15ee5a-21d1-4d1c-9609-af576142b12f'
SOURCE_PATH = 'pictographic-primitives/protection/castle gate_9e15ee5a-21d1-4d1c-9609-af576142b12f.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'castle-tower-with-drawbridge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('castle', 'tower', 'drawbridge', 'gate', 'fortress', 'moat', 'medieval', 'defence')

    def build(self):
        # SQUARE centerline extremes: (6,6)-(42,42).

        # Deliberately asymmetric: right tower and a lowered left drawbridge.
        self.add_polyline('tower',(26,42),(26,6),(34,6),(34,14),(42,14),(42,6),(42,42))
        self.add_polyline('bridge',(6,30),(26,42))
        self.relate('connect','bridge','tower')
        self.add_line('chain',(6,30),(26,14))
        self.relate('connect','chain','bridge')
        self.relate('connect','chain','tower')
        self.add_line('window',(34,24),(34,29))
        self.add_line('water',(6,42),(9,42))
