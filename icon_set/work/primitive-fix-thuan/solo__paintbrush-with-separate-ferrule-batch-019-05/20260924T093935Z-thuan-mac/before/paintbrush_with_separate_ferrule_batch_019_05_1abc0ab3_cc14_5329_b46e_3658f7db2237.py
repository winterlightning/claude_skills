from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1abc0ab3-cc14-5329-b46e-3658f7db2237'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/brush_1abc0ab3-cc14-5329-b46e-3658f7db2237.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/references/brush_1abc0ab3-cc14-5329-b46e-3658f7db2237.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-019/05-artistic-paint-brush--1abc0ab3-cc14-5329-b46e-3658f7db2237.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Ferrule widened as one owning shape to preserve its internal opening.']
CONSTRUCTION_REFERENCE = 'paintbrush: bristle, ferrule and diagonal handle hierarchy.'

class BatchIcon(Solo48):
    icon_id = 'paintbrush-with-separate-ferrule-batch-019-05'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('paintbrush', 'brush', 'paint', 'artist', 'bristles', 'ferrule', 'handle', 'art')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('handle', (22, 18), (34, 6), (42, 6), (42, 14), (32, 28), closed=False)
        self.add_polyline('ferrule', (22, 18), (14, 26), (24, 36), (32, 28), closed=True)
        self.add_arc('bristle-side', (14, 26), (6, 34), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_line('tip', (6, 34), (6, 42))
        self.add_arc('bristle-belly', (6, 42), (24, 36), radius_x=18, radius_y=6, sweep=False, large_arc=False)
        self.relate("connect", 'handle', 'ferrule')
        self.relate("connect", 'ferrule', 'bristle-side')
        self.relate("connect", 'ferrule', 'bristle-belly')
        self.relate("connect", 'bristle-side', 'tip')
        self.relate("connect", 'tip', 'bristle-belly')
