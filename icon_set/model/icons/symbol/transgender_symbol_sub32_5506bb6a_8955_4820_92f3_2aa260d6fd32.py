"""Independent 32px profile of transgender-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5506bb6a-8955-4820-92f3-2aa260d6fd32'
SOURCE_PATH = 'pictographic-primitives/users/gender transgender_5506bb6a-8955-4820-92f3-2aa260d6fd32.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5506bb6a-8955-4820-92f3-2aa260d6fd32', 'pictographic-primitives/users/gender transgender_5506bb6a-8955-4820-92f3-2aa260d6fd32.svg'),)
PROFILE_SOURCE_KEYS = ('solo/transgender-symbol',)
SOLO_SOURCE_ICON_IDS = ('transgender-symbol',)
REFERENCE_EXPORT_SHA256 = '216190f5f7c5e561b34bbf5cc13af381d3693ff10f5b0faf536f7578e8b6ffac'

class Drawing(Sub32):
    icon_id = 'transgender-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'users'
    categories = ('users', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Transgender symbol: circle, arrow to the top right, cross below, and the top-left stroke with its crossbar.
        self.add_arc('c-1', (11, 15), (21, 15), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('c-2', (21, 15), (11, 15), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('circle', 'c-1', 'c-2', closed=True)
        self.add_line('male', (20, 12), (30, 2))
        self.add_polyline('male-head', (24, 2), (30, 2), (30, 8))
        self.add_line('trans', (12, 12), (2, 2))
        self.add_line('trans-bar', (3, 7), (7, 3))
        self.add_line('female', (16, 20), (16, 30))
        self.add_line('female-bar', (12, 28), (20, 28))
        for a, b in (('circle', 'male'), ('male', 'male-head'), ('circle', 'trans'), ('trans', 'trans-bar'), ('circle', 'female'), ('female', 'female-bar')):
            self.relate('connect', a, b)
