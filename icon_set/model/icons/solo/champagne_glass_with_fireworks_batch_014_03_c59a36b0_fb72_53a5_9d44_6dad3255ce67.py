"""Champagne Glass with Fireworks.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Champagne glass at lower-left beside a six-ray firework burst.
Reduction: One clear burst replaces three small fireworks; omit liquid level.
Construction reference: wine: bowl, centered stem and foot
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c59a36b0-fb72-53a5-9d44-6dad3255ce67'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/gregorian new year party_c59a36b0-fb72-53a5-9d44-6dad3255ce67.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/gregorian new year party_c59a36b0-fb72-53a5-9d44-6dad3255ce67.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/gregorian new year party_c59a36b0-fb72-53a5-9d44-6dad3255ce67.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'champagne-glass-with-fireworks-batch-014-03'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('champagne', 'glass', 'fireworks', 'celebration', 'party', 'newyear')

    def build(self):
        self.add_line('glass-1', (6, 20), (8, 29))
        self.add_bezier('glass-2', (8, 29), ((9, 33), (11, 33), (14, 33)))
        self.add_bezier('glass-3', (14, 33), ((17, 33), (19, 33), (20, 29)))
        self.add_line('glass-4', (20, 29), (22, 20))
        self.add_line('glass-close', (22, 20), (6, 20))
        self.add_contour('glass', 'glass-1', 'glass-2', 'glass-3', 'glass-4', 'glass-close', closed=True)
        self.add_line('stem', (14, 33), (14, 42))
        self.add_line('foot', (8, 42), (20, 42))
        self.relate("connect", 'glass', 'stem')
        self.relate("connect", 'stem', 'foot')
        self.add_line('burst-v', (35, 6), (35, 20))
        self.add_line('burst-a', (28, 8), (42, 18))
        self.add_line('burst-b', (30, 18), (40, 8))
        self.relate("connect", 'burst-v', 'burst-a')
        self.relate("connect", 'burst-v', 'burst-b')
        self.relate("connect", 'burst-a', 'burst-b')
