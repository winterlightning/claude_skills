"""Scalp Massage Tool with Waves.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Rounded grip, five equally spaced prongs and a scalp wave.
Reduction: Keep one broad wave instead of two for clearance.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a087fb85-b626-4733-80ad-3053b73b9ca9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/head massage tool_a087fb85-b626-4733-80ad-3053b73b9ca9.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/head massage tool_a087fb85-b626-4733-80ad-3053b73b9ca9.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/head massage tool_a087fb85-b626-4733-80ad-3053b73b9ca9.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'scalp-massage-tool-batch-012-11'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('scalp', 'massage', 'tool', 'prongs', 'waves', 'therapy')

    def build(self):
        self.add_line('grip-1', (8, 6), (40, 6))
        self.add_arc('grip-2', (40, 6), (42, 8), radius_x=2, radius_y=2, sweep=True)
        self.add_line('grip-3', (42, 8), (42, 12))
        self.add_arc('grip-4', (42, 12), (40, 14), radius_x=2, radius_y=2, sweep=True)
        self.add_line('grip-5', (40, 14), (8, 14))
        self.add_arc('grip-6', (8, 14), (6, 12), radius_x=2, radius_y=2, sweep=True)
        self.add_line('grip-7', (6, 12), (6, 8))
        self.add_arc('grip-8', (6, 8), (8, 6), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('grip', 'grip-1', 'grip-2', 'grip-3', 'grip-4', 'grip-5', 'grip-6', 'grip-7', 'grip-8', closed=True)
        self.add_line('prong-0', (8, 14), (8, 26))
        self.relate("connect", 'grip', 'prong-0')
        self.add_line('prong-1', (16, 14), (16, 26))
        self.relate("connect", 'grip', 'prong-1')
        self.add_line('prong-2', (24, 14), (24, 26))
        self.relate("connect", 'grip', 'prong-2')
        self.add_line('prong-3', (32, 14), (32, 26))
        self.relate("connect", 'grip', 'prong-3')
        self.add_line('prong-4', (40, 14), (40, 26))
        self.relate("connect", 'grip', 'prong-4')
        self.add_bezier('wave-1', (6, 38), ((9, 34), (12, 34), (15, 38)))
        self.add_bezier('wave-2', (15, 38), ((18, 42), (21, 42), (24, 42)))
        self.add_bezier('wave-3', (24, 42), ((27, 42), (30, 34), (33, 34)))
        self.add_bezier('wave-4', (33, 34), ((36, 34), (39, 38), (42, 38)))
        self.add_contour('wave', 'wave-1', 'wave-2', 'wave-3', 'wave-4', closed=False)
