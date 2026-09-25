from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b2a855e-6ab2-51bc-8612-b388126ed3ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/networks/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/cross region data delivery_3b2a855e-6ab2-51bc-8612-b388126ed3ff.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/12-global-network-nodes--3b2a855e-6ab2-51bc-8612-b388126ed3ff.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Three connected nodes retained; outer boundary links omitted to reduce clutter.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'global-network-nodes-batch-018-12'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "networks"
    categories = ("primitives", "networks")
    keywords = ('network', 'globe', 'nodes', 'links', 'data', 'connections', 'graph', 'global')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('boundary-0', (4, 24), (24, 4), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('boundary-1', (24, 4), (44, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('boundary-2', (44, 24), (24, 44), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('boundary-3', (24, 44), (4, 24), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_contour('boundary', 'boundary-0', 'boundary-1', 'boundary-2', 'boundary-3', closed=True)
        self.add_arc('left-0', (13, 24), (15, 22), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('left-1', (15, 22), (17, 24), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('left-2', (17, 24), (15, 26), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('left-3', (15, 26), (13, 24), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('left', 'left-0', 'left-1', 'left-2', 'left-3', closed=True)
        self.add_arc('top-0', (26, 17), (28, 15), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('top-1', (28, 15), (30, 17), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('top-2', (30, 17), (28, 19), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('top-3', (28, 19), (26, 17), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('top', 'top-0', 'top-1', 'top-2', 'top-3', closed=True)
        self.add_arc('bottom-0', (26, 31), (28, 29), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('bottom-1', (28, 29), (30, 31), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('bottom-2', (30, 31), (28, 33), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('bottom-3', (28, 33), (26, 31), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('bottom', 'bottom-0', 'bottom-1', 'bottom-2', 'bottom-3', closed=True)
        self.add_line('upper-link', (17, 24), (26, 17))
        self.add_line('lower-link', (17, 24), (26, 31))
        self.add_line('vertical-link', (28, 19), (28, 29))
        self.relate("connect", 'left', 'upper-link')
        self.relate("connect", 'left', 'lower-link')
        self.relate("connect", 'top', 'upper-link')
        self.relate("connect", 'top', 'vertical-link')
        self.relate("connect", 'bottom', 'lower-link')
        self.relate("connect", 'bottom', 'vertical-link')
        self.relate("connect", 'upper-link', 'lower-link')
