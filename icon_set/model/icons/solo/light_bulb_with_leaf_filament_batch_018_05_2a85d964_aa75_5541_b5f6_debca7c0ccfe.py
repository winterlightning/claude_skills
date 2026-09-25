from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a85d964-aa75-5541-b5f6-debca7c0ccfe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/lights/light bulb eco_2a85d964-aa75-5541-b5f6-debca7c0ccfe.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/light bulb eco_2a85d964-aa75-5541-b5f6-debca7c0ccfe.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/05-eco-friendly-light-bulb--2a85d964-aa75-5541-b5f6-debca7c0ccfe.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Leaf reduced to a broad pointed diamond with a short stem; base threads omitted.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'light-bulb-with-leaf-filament-batch-018-05'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "lights"
    keywords = ('bulb', 'leaf', 'filament', 'light', 'eco', 'plant', 'energy', 'electric')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('top', (8, 20), (40, 20), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_line('base-part-0', (40, 20), (34, 32))
        self.add_line('base-part-1', (34, 32), (32, 36))
        self.add_line('base-part-2', (32, 36), (32, 44))
        self.add_line('base-part-3', (32, 44), (16, 44))
        self.add_line('base-part-4', (16, 44), (16, 36))
        self.add_line('base-part-5', (16, 36), (14, 32))
        self.add_line('base-part-6', (14, 32), (8, 20))
        self.add_contour('bulb', 'top', 'base-part-0', 'base-part-1', 'base-part-2', 'base-part-3', 'base-part-4', 'base-part-5', 'base-part-6', closed=True)
        self.add_polyline('leaf', (24, 16), (30, 22), (24, 28), (18, 22), closed=True)
        self.add_line('stem', (24, 28), (24, 34))
        self.relate("connect", 'leaf', 'stem')
