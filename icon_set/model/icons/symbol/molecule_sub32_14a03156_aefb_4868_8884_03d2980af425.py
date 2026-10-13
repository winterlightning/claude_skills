"""Independent 32px profile of molecule.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '14a03156-aefb-4868-8884-03d2980af425'
SOURCE_PATH = 'pictographic-primitives/science/molecule_14a03156-aefb-4868-8884-03d2980af425.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14a03156-aefb-4868-8884-03d2980af425', 'pictographic-primitives/science/molecule_14a03156-aefb-4868-8884-03d2980af425.svg'), ('bd75597b-ada9-478f-9eb1-91e31b7ac0c2', 'pictographic-primitives/science/molecule_bd75597b-ada9-478f-9eb1-91e31b7ac0c2.svg'))
PROFILE_SOURCE_KEYS = ('solo/molecule', 'solo/molecule-bd75597b')
SOLO_SOURCE_ICON_IDS = ('molecule', 'molecule-bd75597b')
REFERENCE_EXPORT_SHA256 = 'e49186f3373fa44de7dc9fb13f2112688b227299417d6bab5bd5ebcd7109b5f7'

class Drawing(Sub32):
    icon_id = 'molecule-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'science'
    categories = ('science', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Molecule: three atoms joined by three bonds.
        for k, (x, y) in enumerate(((16, 8), (6, 24), (26, 24))):
            self.add_arc(f'atom-{k}-1', (x - 4, y), (x + 4, y), radius_x=4, radius_y=4, large_arc=False, sweep=True)
            self.add_arc(f'atom-{k}-2', (x + 4, y), (x - 4, y), radius_x=4, radius_y=4, large_arc=False, sweep=True)
            self.add_contour(f'atom-{k}', f'atom-{k}-1', f'atom-{k}-2', closed=True)
        self.add_line('bond-l', (12, 8), (6, 20))
        self.add_line('bond-r', (20, 8), (26, 20))
        self.add_line('bond-b', (10, 24), (22, 24))
        for a, b in (('atom-0', 'bond-l'), ('atom-1', 'bond-l'), ('atom-0', 'bond-r'), ('atom-2', 'bond-r'), ('atom-1', 'bond-b'), ('atom-2', 'bond-b')):
            self.relate('connect', a, b)
