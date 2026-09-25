"""Traditional Bow and Arrow.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Curved upright bow with taut string and right-pointing arrow.
Reduction: Focus on named bow and arrow; omit unresolved adjacent ritual forms.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5f26275-d65e-486b-af08-f77f5cc364f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/vijayadashami_a5f26275-d65e-486b-af08-f77f5cc364f2.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/vijayadashami_a5f26275-d65e-486b-af08-f77f5cc364f2.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/vijayadashami_a5f26275-d65e-486b-af08-f77f5cc364f2.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'bow-and-arrow-with-unresolved-adjacent-forms-batch-014-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('bow', 'arrow', 'archery', 'festival', 'string', 'weapon')

    def build(self):
        self.add_bezier('bow-1', (10, 6), ((34, 6), (34, 42), (10, 42)))
        self.add_contour('bow', 'bow-1', closed=False)
        self.add_polyline('string', (10, 6), (20, 24), (10, 42), closed=False)
        self.relate("connect", 'bow', 'string')
        self.add_line('arrow', (6, 24), (42, 24))
        self.add_polyline('arrowhead', (34, 16), (42, 24), (34, 32), closed=False)
        self.relate("connect", 'arrow', 'arrowhead')
        self.relate("connect", 'arrow', 'bow')
        self.relate("connect", 'arrow', 'string')
