"""Sacred Divine Gateway Entrance.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Symmetric central ceremonial arch beneath two angular raised forms.
Reduction: Preserve ambiguous gateway/figure silhouette; omit tiny interior U.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'arched-figure-beneath-paired-raised-forms-batch-014-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('arch', 'figure', 'ceremony', 'raised', 'outline', 'festival')

    def build(self):
        self.add_line('arch-1', (14, 42), (14, 30))
        self.add_arc('arch-2', (14, 30), (34, 30), radius_x=10, radius_y=12, sweep=True)
        self.add_line('arch-3', (34, 30), (34, 42))
        self.add_line('arch-close', (34, 42), (14, 42))
        self.add_contour('arch', 'arch-1', 'arch-2', 'arch-3', 'arch-close', closed=True)
        self.add_polyline('raised-left', (6, 18), (6, 10), (14, 6), (16, 10), closed=False)
        self.add_polyline('raised-right', (42, 18), (42, 10), (34, 6), (32, 10), closed=False)
