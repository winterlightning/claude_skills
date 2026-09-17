"""Closed Workflow Request Connection.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Two upright workflow links: circle pair at left, circle and cross at right.
Reduction: Equal node radii; upper-right cross is intrinsic closed endpoint.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '387cccb6-81ba-437c-8e8c-5ee228aa94de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/workflow request closed_387cccb6-81ba-437c-8e8c-5ee228aa94de.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/workflow request closed_387cccb6-81ba-437c-8e8c-5ee228aa94de.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/workflow request closed_387cccb6-81ba-437c-8e8c-5ee228aa94de.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'workflow-connections-with-cross-endpoint-batch-014-15'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('workflow', 'connections', 'nodes', 'cross', 'diagram', 'request')

    def build(self):
        self.add_arc('upper-1', (12, 6), (18, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('upper-2', (18, 12), (12, 18), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('upper-3', (12, 18), (6, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('upper-4', (6, 12), (12, 6), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('upper', 'upper-1', 'upper-2', 'upper-3', 'upper-4', closed=True)
        self.add_arc('lower-1', (12, 30), (18, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('lower-2', (18, 36), (12, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('lower-3', (12, 42), (6, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('lower-4', (6, 36), (12, 30), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('lower', 'lower-1', 'lower-2', 'lower-3', 'lower-4', closed=True)
        self.add_arc('right-1', (36, 30), (42, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('right-2', (42, 36), (36, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('right-3', (36, 42), (30, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('right-4', (30, 36), (36, 30), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('right', 'right-1', 'right-2', 'right-3', 'right-4', closed=True)
        self.add_line('left-link', (12, 18), (12, 30))
        self.relate("connect", 'upper', 'left-link')
        self.relate("connect", 'lower', 'left-link')
        self.add_line('right-link', (36, 24), (36, 30))
        self.relate("connect", 'right', 'right-link')
        self.add_line('cross-a', (30, 6), (42, 18))
        self.add_line('cross-b', (42, 6), (30, 18))
        self.relate("connect", 'cross-a', 'cross-b')
