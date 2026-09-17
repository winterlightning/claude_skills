from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f26224c-ad5e-551c-9f1b-15837db228cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/09-teddy-bear-plush-toy--5f26224c-ad5e-551c-9f1b-15837db228cb.md'
DESIGN_PLAN = 'Mirrored round ears above a broad head; rounded side arms and forward feet.'
DESIGN_NOTES = ['Blank face and belly preserve the plush toy’s uncluttered appearance; feet merge into the lower silhouette.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'teddy-bear-plush-toy-batch-017-09'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('teddy', 'bear', 'plush', 'toy', 'animal', 'seated', 'childhood', 'soft')

    def build(self):
        # Mirrored round ears above a broad head; rounded side arms and forward feet.
        self.add_line('head-top', (18, 10), (30, 10))
        self.add_arc('ear-r', (30, 10), (38, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('face-r', (38, 10), (38, 18))
        self.add_arc('cheek-r', (38, 18), (32, 24), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('arm-r', (32, 24), (42, 30), radius_x=10, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('arm-bottom-r', (42, 30), (34, 36), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('foot-r', (34, 36), (34, 42), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('base', (34, 42), (14, 42))
        self.add_arc('foot-l', (14, 42), (14, 36), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('arm-bottom-l', (14, 36), (6, 30), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('arm-l', (6, 30), (16, 24), radius_x=10, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cheek-l', (16, 24), (10, 18), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('face-l', (10, 18), (10, 10))
        self.add_arc('ear-l', (10, 10), (18, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('bear', 'head-top', 'ear-r', 'face-r', 'cheek-r', 'arm-r', 'arm-bottom-r', 'foot-r', 'base', 'foot-l', 'arm-bottom-l', 'arm-l', 'cheek-l', 'face-l', 'ear-l', closed=True)
