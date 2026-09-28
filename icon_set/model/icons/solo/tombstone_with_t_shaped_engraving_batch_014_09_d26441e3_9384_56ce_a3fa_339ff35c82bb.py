"""Tombstone Grave Marker.

SOLO48 visible bounds: (6, 2, 42, 46). Centerline extremes: (8, 4, 40, 44).

Symbol plan: Round-topped grave marker with a central abstract cross and base.
Reduction: Interpret ambiguous T-shaped engraving as a memorial cross, not text; omit ground ripple.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd26441e3-9384-56ce-a3fa-339ff35c82bb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/halloween graveyard_d26441e3-9384-56ce-a3fa-339ff35c82bb.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/halloween graveyard_d26441e3-9384-56ce-a3fa-339ff35c82bb.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/halloween graveyard_d26441e3-9384-56ce-a3fa-339ff35c82bb.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'tombstone-with-t-shaped-engraving-batch-014-09'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('tombstone', 'grave', 'marker', 'engraving', 'cemetery', 'stone')

    def build(self):
        self.add_line('stone-1', (12, 44), (12, 16))
        self.add_arc('stone-2', (12, 16), (36, 16), radius_x=12, radius_y=12, sweep=True)
        self.add_line('stone-3', (36, 16), (36, 44))
        self.add_line('stone-close', (36, 44), (12, 44))
        self.add_contour('stone', 'stone-1', 'stone-2', 'stone-3', 'stone-close', closed=True)
        self.add_line('base-left', (8, 44), (12, 44))
        self.add_line('base-right', (36, 44), (40, 44))
        self.relate("connect", 'stone', 'base-left')
        self.relate("connect", 'stone', 'base-right')
        self.add_line('cross-stem', (24, 17), (24, 30))
        self.add_line('cross-bar', (21, 21), (27, 21))
        self.relate("connect", 'cross-stem', 'cross-bar')

# Visually reviewed equivalent content reference, explicitly requested for reuse.
SOURCE_REFERENCES = tuple(globals().get("SOURCE_REFERENCES", ())) + (('d639010e-7131-46d6-b3fa-028d7353a5b9', 'icon_set/dist/gallery/combination-originals/d639010e-7131-46d6-b3fa-028d7353a5b9.svg'),)
