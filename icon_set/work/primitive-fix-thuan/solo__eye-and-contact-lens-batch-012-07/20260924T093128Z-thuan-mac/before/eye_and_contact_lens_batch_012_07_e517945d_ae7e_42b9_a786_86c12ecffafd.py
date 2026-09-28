"""Eye and Contact Lens.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Eye upper-right with large contact lens at lower-left.
Reduction: Remove reflection and iris ring to allow a clear eye/lens pair.
Construction reference: eye: almond outline and sparse pupil
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e517945d-ae7e-42b9-a786-86c12ecffafd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/ophthalmic contact lens_e517945d-ae7e-42b9-a786-86c12ecffafd.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/ophthalmic contact lens_e517945d-ae7e-42b9-a786-86c12ecffafd.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/ophthalmic contact lens_e517945d-ae7e-42b9-a786-86c12ecffafd.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'eye-and-contact-lens-batch-012-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('eye', 'contact', 'lens', 'vision', 'iris', 'optical')

    def build(self):
        self.add_bezier('eye-1', (16, 22), ((20, 10), (24, 6), (30, 6)))
        self.add_bezier('eye-2', (30, 6), ((36, 6), (40, 12), (42, 16)))
        self.add_bezier('eye-3', (42, 16), ((38, 24), (34, 28), (26, 32)))
        self.add_contour('eye', 'eye-1', 'eye-2', 'eye-3', closed=False)
        self.add_dot('pupil', (30, 17))
        self.add_arc('lens-1', (16, 22), (26, 32), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('lens-2', (26, 32), (16, 42), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('lens-3', (16, 42), (6, 32), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('lens-4', (6, 32), (16, 22), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('lens', 'lens-1', 'lens-2', 'lens-3', 'lens-4', closed=True)
        self.relate("connect", 'eye', 'lens')
