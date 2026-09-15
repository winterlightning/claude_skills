"""A flame burns beside a tall pine. HRECT extremes (4,8)-(44,40); deliberate scene asymmetry.
Reduction: Reduced two overlapping trees to one and omitted detached smoke curls and inner flame.
Lucide: flame, tree-pine
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb5d6e43-8c14-47cd-a965-fb2a738c8e11'
SOURCE_PATH = 'pictographic-primitives/nature/trees camp fire_cb5d6e43-8c14-47cd-a965-fb2a738c8e11.svg'
AUTHOR = 'gpt-6'

class ForestFire(Solo48):
    icon_id = 'forest-fire'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-03"
    aliases = ()
    keywords = ('forest fire', 'wildfire', 'trees', 'flame', 'smoke', 'campfire', 'pine', 'danger')

    def build(self) -> None:
        self.add_polyline('pine',(28,32),(36,8),(44,32),(36,32),closed=True)
        self.add_line('trunk',(36,32),(36,40))
        for p in ('pine-3','pine-4'):self.relate('connect','trunk',p)
        self.add_arc('flame-outer',(12,12),(20,32),radius_x=8,radius_y=20)
        self.add_arc('flame-bottom',(20,32),(4,32),radius_x=8)
        self.add_line('flame-left',(4,32),(4,24))
        self.add_arc('flame-notch',(4,24),(12,24),radius_x=4,sweep=False)
        self.add_line('flame-tip',(12,24),(12,12))
        self.add_contour('flame','flame-outer','flame-bottom','flame-left','flame-notch','flame-tip',closed=True)
