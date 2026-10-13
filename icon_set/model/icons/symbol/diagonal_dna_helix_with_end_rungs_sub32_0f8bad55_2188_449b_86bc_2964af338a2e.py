"""Independent 32px profile of diagonal-dna-helix-with-end-rungs.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0f8bad55-2188-449b-86bc-2964af338a2e'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_0f8bad55-2188-449b-86bc-2964af338a2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0f8bad55-2188-449b-86bc-2964af338a2e', 'pictographic-primitives/artificial-intelligence/dna_0f8bad55-2188-449b-86bc-2964af338a2e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/diagonal-dna-helix-with-end-rungs',)
SOLO_SOURCE_ICON_IDS = ('diagonal-dna-helix-with-end-rungs',)
REFERENCE_EXPORT_SHA256 = 'f6268bd9b2ed31030db06aec05daf019e46d4744683b61f74a2f78b68935fab6'

class Drawing(Sub32):
    icon_id = 'diagonal-dna-helix-with-end-rungs-sub32'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Double helix: two strands crossing twice, rungs at both ends and in the middle.
        self.add_bezier('strand-a-1', (8, 2), ((8, 8), (24, 10), (24, 16)))
        self.add_bezier('strand-a-2', (24, 16), ((24, 22), (8, 24), (8, 30)))
        self.add_contour('strand-a', 'strand-a-1', 'strand-a-2')
        self.add_bezier('strand-b-1', (24, 2), ((24, 8), (8, 10), (8, 16)))
        self.add_bezier('strand-b-2', (8, 16), ((8, 22), (24, 24), (24, 30)))
        self.add_contour('strand-b', 'strand-b-1', 'strand-b-2')
        self.add_line('rung-top', (8, 2), (24, 2))
        self.add_line('rung-mid', (8, 16), (24, 16))
        self.add_line('rung-bottom', (8, 30), (24, 30))
        for rung in ('rung-top', 'rung-mid', 'rung-bottom'):
            self.relate('connect', 'strand-a', rung)
            self.relate('connect', 'strand-b', rung)
        self.relate('connect', 'strand-a', 'strand-b')
