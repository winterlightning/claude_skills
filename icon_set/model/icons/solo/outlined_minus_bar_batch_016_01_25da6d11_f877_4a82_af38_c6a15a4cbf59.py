from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25da6d11-f877-4a82-af38-c6a15a4cbf59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/subtract bold_25da6d11-f877-4a82-af38-c6a15a4cbf59.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/references/subtract bold_25da6d11-f877-4a82-af38-c6a15a4cbf59.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-016/01-minus-symbol--25da6d11-f877-4a82-af38-c6a15a4cbf59.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Outlined bar uses radial envelope to retain a horizontal minus silhouette.']
CONSTRUCTION_REFERENCE = 'No useful outlined minus match.'

class BatchIcon(Solo48):
    icon_id = 'outlined-minus-bar-batch-016-01'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    keywords = ('minus', 'subtract', 'bar', 'horizontal', 'operator', 'symbol')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_line('bar-0', (8, 16), (40, 16))
        self.add_arc('bar-1', (40, 16), (43, 19), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('bar-2', (43, 19), (43, 29))
        self.add_arc('bar-3', (43, 29), (40, 32), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('bar-4', (40, 32), (8, 32))
        self.add_arc('bar-5', (8, 32), (5, 29), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('bar-6', (5, 29), (5, 19))
        self.add_arc('bar-7', (5, 19), (8, 16), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('bar', 'bar-0', 'bar-1', 'bar-2', 'bar-3', 'bar-4', 'bar-5', 'bar-6', 'bar-7', closed=True)
