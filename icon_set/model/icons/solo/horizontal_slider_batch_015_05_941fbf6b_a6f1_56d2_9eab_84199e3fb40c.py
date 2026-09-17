"""Horizontal Adjustment Slider.

SOLO48 visible bounds: (2, 8, 46, 40). Centerline extremes: (4, 10, 44, 38).

Symbol plan: Tall capsule slider thumb and separated horizontal track arms.
Reduction: Thumb remains slightly left of center.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '941fbf6b-a6f1-56d2-9eab-84199e3fb40c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/setting slider horizontal_941fbf6b-a6f1-56d2-9eab-84199e3fb40c.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/setting slider horizontal_941fbf6b-a6f1-56d2-9eab-84199e3fb40c.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-015/references/setting slider horizontal_941fbf6b-a6f1-56d2-9eab-84199e3fb40c.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'horizontal-slider-batch-015-05'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-subjects"
    aliases = ()
    keywords = ('slider', 'control', 'setting', 'adjust', 'horizontal', 'knob')

    def build(self):
        self.add_line('thumb-1', (19, 10), (19, 10))
        self.add_arc('thumb-2', (19, 10), (25, 16), radius_x=6, radius_y=6, sweep=True)
        self.add_line('thumb-3', (25, 16), (25, 32))
        self.add_arc('thumb-4', (25, 32), (19, 38), radius_x=6, radius_y=6, sweep=True)
        self.add_line('thumb-5', (19, 38), (19, 38))
        self.add_arc('thumb-6', (19, 38), (13, 32), radius_x=6, radius_y=6, sweep=True)
        self.add_line('thumb-7', (13, 32), (13, 16))
        self.add_arc('thumb-8', (13, 16), (19, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('thumb', 'thumb-1', 'thumb-2', 'thumb-3', 'thumb-4', 'thumb-5', 'thumb-6', 'thumb-7', 'thumb-8', closed=True)
        self.add_line('track-left', (4, 24), (13, 24))
        self.add_line('track-right', (25, 24), (44, 24))
        self.relate("connect", 'thumb', 'track-left')
        self.relate("connect", 'thumb', 'track-right')
