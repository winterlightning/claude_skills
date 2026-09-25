"""Lohri Kite and Bonfire.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Kite upper-right, flame lower-left and short fuel line.
Reduction: Omit kite spars and small inner flame.
Construction reference: flame: pointed crest and curved lower bowl
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0de72e2d-97f0-4d32-ba42-4be760f786bb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/lohri kite_0de72e2d-97f0-4d32-ba42-4be760f786bb.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/lohri kite_0de72e2d-97f0-4d32-ba42-4be760f786bb.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/lohri kite_0de72e2d-97f0-4d32-ba42-4be760f786bb.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'kite-above-bonfire-batch-014-06'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('kite', 'bonfire', 'flame', 'lohri', 'festival', 'tail')

    def build(self):
        self.add_polyline('kite', (32, 6), (42, 16), (32, 28), (22, 16), closed=True)
        self.add_bezier('tail-1', (32, 28), ((30, 34), (38, 34), (38, 42)))
        self.add_contour('tail', 'tail-1', closed=False)
        self.relate("connect", 'kite', 'tail')
        self.add_bezier('flame-1', (14, 20), ((14, 28), (6, 28), (6, 34)))
        self.add_bezier('flame-2', (6, 34), ((6, 42), (22, 42), (22, 34)))
        self.add_bezier('flame-3', (22, 34), ((22, 28), (18, 24), (14, 20)))
        self.add_contour('flame', 'flame-1', 'flame-2', 'flame-3', closed=True)
