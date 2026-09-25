from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fabb5032-2d1a-5cd1-9271-52e946129be1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/yoyo_fabb5032-2d1a-5cd1-9271-52e946129be1.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/yoyo_fabb5032-2d1a-5cd1-9271-52e946129be1.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/13-toy-yoyo-with-finger-loop--fabb5032-2d1a-5cd1-9271-52e946129be1.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Loop separated from yoyo; string attaches at exact outline extrema.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'yoyo-with-finger-loop-batch-017-13'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    categories = ("primitives", "kids")
    keywords = ('yoyo', 'toy', 'string', 'loop', 'circle', 'play', 'spinning', 'childhood')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('body-0', (6, 30), (18, 18), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('body-1', (18, 18), (30, 30), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('body-2', (30, 30), (18, 42), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('body-3', (18, 42), (6, 30), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', closed=True)
        self.add_arc('ring-0', (15, 30), (18, 27), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('ring-1', (18, 27), (21, 30), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('ring-2', (21, 30), (18, 33), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('ring-3', (18, 33), (15, 30), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('ring', 'ring-0', 'ring-1', 'ring-2', 'ring-3', closed=True)
        self.add_arc('loop-0', (34, 10), (38, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('loop-1', (38, 6), (42, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('loop-2', (42, 10), (38, 14), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('loop-3', (38, 14), (34, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('loop', 'loop-0', 'loop-1', 'loop-2', 'loop-3', closed=True)
        self.add_polyline('string', (30, 30), (38, 22), (38, 14), closed=False)
        self.relate("connect", 'body', 'string')
        self.relate("connect", 'loop', 'string')
