from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'adb3af2d-d45b-443f-893f-729c0e49861d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/slinky physics spring toy_adb3af2d-d45b-443f-893f-729c0e49861d.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/slinky physics spring toy_adb3af2d-d45b-443f-893f-729c0e49861d.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/06-curved-physics-spring-toy--adb3af2d-d45b-443f-893f-729c0e49861d.md'
DESIGN_PLAN = 'One coherent outline; shared dimensions own repeated parts.'
DESIGN_NOTES = ['Top seam omitted to avoid subdividing the small curved crown.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'arched-spring-toy-batch-017-06'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('spring', 'slinky', 'toy', 'arch', 'curve', 'physics')

    def build(self):
        # One coherent outline; shared dimensions own repeated parts.
        self.add_arc('outer', (4, 28), (44, 28), radius_x=20, radius_y=20, sweep=True, large_arc=False)
        self.add_arc('inner', (32, 28), (16, 28), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_line('bottom-right-part-0', (44, 28), (44, 40))
        self.add_line('bottom-right-part-1', (44, 40), (32, 40))
        self.add_line('bottom-right-part-2', (32, 40), (32, 28))
        self.add_line('bottom-left-part-0', (16, 28), (16, 40))
        self.add_line('bottom-left-part-1', (16, 40), (4, 40))
        self.add_line('bottom-left-part-2', (4, 40), (4, 28))
        self.add_contour('arch', 'outer', 'bottom-right-part-0', 'bottom-right-part-1', 'bottom-right-part-2', 'inner', 'bottom-left-part-0', 'bottom-left-part-1', 'bottom-left-part-2', closed=True)
        self.add_line('left-seam', (4, 28), (16, 28))
        self.add_line('right-seam', (32, 28), (44, 28))
        self.relate("connect", 'arch', 'left-seam')
        self.relate("connect", 'arch', 'right-seam')
