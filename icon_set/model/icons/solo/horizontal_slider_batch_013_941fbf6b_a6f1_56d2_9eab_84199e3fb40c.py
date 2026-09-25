"""Tall capsule adjustment knob left of center across a horizontal track. Capsule radius6 controls both ends, tracks remain detached with 8 centerline units clearance.
Lucide sliders-horizontal: interrupted horizontal track, source capsule rather than straight knob.
Keyshape HRECT_M on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '941fbf6b-a6f1-56d2-9eab-84199e3fb40c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/setting slider horizontal_941fbf6b-a6f1-56d2-9eab-84199e3fb40c.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/setting slider horizontal_941fbf6b-a6f1-56d2-9eab-84199e3fb40c.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/setting slider horizontal_941fbf6b-a6f1-56d2-9eab-84199e3fb40c.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'horizontal-slider-batch-013'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    aliases = ()
    keywords = ('horizontal', 'slider')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_arc('top',(14,16),(26,16),radius_x=6)
        self.add_line('right',(26,16),(26,32))
        self.add_arc('bottom',(26,32),(14,32),radius_x=6)
        self.add_line('left',(14,32),(14,16))
        self.add_contour('knob','top','right','bottom','left',closed=True)
        self.add_line('track-left',(4,24),(6,24))
        self.add_line('track-right',(34,24),(44,24))
