from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d0d1025-1418-574d-b291-75e0e612531c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/references/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-018/14-3d-object-rotation-tool--0d0d1025-1418-574d-b291-75e0e612531c.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Three node connections retained; terminal circles use the approved small-circle construction.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'cube-with-three-connected-nodes-batch-018-14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('cube', 'nodes', 'diagram', 'connections', 'network', 'three-dimensional', 'graph', 'object')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_polyline('cube', (14, 20), (24, 14), (34, 20), (34, 32), (24, 38), (14, 32), closed=True)
        self.add_polyline('faces', (14, 20), (24, 26), (34, 20), closed=False)
        self.add_line('face-center', (24, 26), (24, 38))
        self.add_arc('top-node-0', (22, 8), (24, 6), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('top-node-1', (24, 6), (26, 8), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('top-node-2', (26, 8), (24, 10), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('top-node-3', (24, 10), (22, 8), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('top-node', 'top-node-0', 'top-node-1', 'top-node-2', 'top-node-3', closed=True)
        self.add_line('top-link', (24, 10), (24, 14))
        self.add_arc('left-node-0', (6, 40), (8, 38), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('left-node-1', (8, 38), (10, 40), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('left-node-2', (10, 40), (8, 42), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('left-node-3', (8, 42), (6, 40), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('left-node', 'left-node-0', 'left-node-1', 'left-node-2', 'left-node-3', closed=True)
        self.add_line('left-link', (10, 40), (14, 32))
        self.add_arc('right-node-0', (38, 40), (40, 38), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('right-node-1', (40, 38), (42, 40), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('right-node-2', (42, 40), (40, 42), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('right-node-3', (40, 42), (38, 40), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('right-node', 'right-node-0', 'right-node-1', 'right-node-2', 'right-node-3', closed=True)
        self.add_line('right-link', (38, 40), (34, 32))
        self.relate("connect", 'cube', 'faces')
        self.relate("connect", 'cube', 'face-center')
        self.relate("connect", 'cube', 'top-link')
        self.relate("connect", 'cube', 'left-link')
        self.relate("connect", 'cube', 'right-link')
        self.relate("connect", 'faces', 'face-center')
        self.relate("connect", 'top-node', 'top-link')
        self.relate("connect", 'left-node', 'left-link')
        self.relate("connect", 'right-node', 'right-link')
