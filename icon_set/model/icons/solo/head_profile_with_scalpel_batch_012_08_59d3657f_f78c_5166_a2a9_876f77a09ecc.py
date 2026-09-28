"""Facial Surgery with Scalpel.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Left-facing head profile beside diagonal scalpel.
Reduction: Use one coherent facial contour and single cutting tip; omit tiny lip steps. Human_ref/user.svg informs circular cranium.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59d3657f-f78c-5166-a2a9-876f77a09ecc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/surgery facial surgery_59d3657f-f78c-5166-a2a9-876f77a09ecc.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/surgery facial surgery_59d3657f-f78c-5166-a2a9-876f77a09ecc.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/surgery facial surgery_59d3657f-f78c-5166-a2a9-876f77a09ecc.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'head-profile-with-scalpel-batch-012-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('head', 'scalpel', 'surgery', 'profile', 'face', 'tool')

    def build(self):
        self.add_line('profile-1', (19, 42), (18, 34))
        self.add_line('profile-2', (18, 34), (10, 34))
        self.add_line('profile-3', (10, 34), (10, 26))
        self.add_line('profile-4', (10, 26), (6, 24))
        self.add_line('profile-5', (6, 24), (10, 17))
        self.add_bezier('profile-6', (10, 17), ((10, 10), (13, 6), (20, 6)))
        self.add_bezier('profile-7', (20, 6), ((29, 6), (30, 13), (28, 20)))
        self.add_line('profile-8', (28, 20), (26, 27))
        self.add_line('profile-9', (26, 27), (28, 42))
        self.add_contour('profile', 'profile-1', 'profile-2', 'profile-3', 'profile-4', 'profile-5', 'profile-6', 'profile-7', 'profile-8', 'profile-9', closed=False)
        self.add_polyline('scalpel', (42, 14), (38, 26), (36, 35), (42, 30), closed=False)
