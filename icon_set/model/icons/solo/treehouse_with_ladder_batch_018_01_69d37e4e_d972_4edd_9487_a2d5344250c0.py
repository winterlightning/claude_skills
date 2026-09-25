from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69d37e4e-d972-4edd-9487-a2d5344250c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/01-treehouse-with-ladder--69d37e4e-d972-4edd-9487-a2d5344250c0.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = []
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'treehouse-with-ladder-batch-018-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    categories = ("primitives", "kids")
    keywords = ('treehouse', 'tree', 'ladder', 'house', 'play', 'outdoors', 'childhood', 'shelter')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('house', (28, 26), (28, 16), (35, 8), (42, 16), (42, 26), (28, 26), closed=False)
        self.add_polyline('ladder-left', (28, 26), (28, 34), (28, 42), closed=False)
        self.add_polyline('ladder-right', (40, 26), (40, 34), (40, 42), closed=False)
        self.add_line('rung-26', (28, 26), (40, 26))
        self.add_line('rung-34', (28, 34), (40, 34))
        self.add_line('rung-42', (28, 42), (40, 42))
        self.add_polyline('tree', (12, 20), (12, 30), (12, 42), closed=False)
        self.add_polyline('branch', (6, 24), (12, 30), (18, 26), closed=False)
        self.add_arc('crown', (6, 12), (18, 12), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.relate("connect", 'house', 'ladder-left')
        self.relate("connect", 'house', 'rung-26')
        self.relate("connect", 'ladder-left', 'rung-26')
        self.relate("connect", 'ladder-left', 'rung-34')
        self.relate("connect", 'ladder-left', 'rung-42')
        self.relate("connect", 'ladder-right', 'rung-26')
        self.relate("connect", 'ladder-right', 'rung-34')
        self.relate("connect", 'ladder-right', 'rung-42')
        self.relate("connect", 'tree', 'branch')
