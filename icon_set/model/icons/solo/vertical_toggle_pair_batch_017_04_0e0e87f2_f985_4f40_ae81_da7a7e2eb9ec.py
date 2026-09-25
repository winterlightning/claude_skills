from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/settings toggle vertical_0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/settings toggle vertical_0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/04-vertical-settings-toggle-switches--0e0e87f2-f985-4f40-ae81-da7a7e2eb9ec.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Knob reduced to a dot to fit the narrow control.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'vertical-toggle-pair-batch-017-04'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    keywords = ('toggle', 'vertical', 'settings', 'controls', 'switches', 'pair')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('left', (10, 6), (18, 6), (22, 10), (22, 38), (18, 42), (10, 42), (6, 38), (6, 10), closed=True)
        self.add_polyline('right', (34, 6), (38, 6), (42, 10), (42, 30), (42, 38), (38, 42), (34, 42), (30, 38), (30, 30), (30, 10), closed=True)
        self.add_line('divider', (30, 30), (42, 30))
        self.add_dot('knob',(14,31))
        self.relate("connect", 'right', 'divider')
