"""Two-finger right-swipe gesture.
Plan: HRECT_L preserves the horizontal arrow above the hand. Shared eight-unit finger widths, rounded tips, shorter right finger and full arrow reviewed in both themes.
Reduction: Small finger creases omitted; two raised fingers and thumb retained. Finger spread simplified.
Construction references: Lucide hand original and atomic-debug: equal rounded fingertip vocabulary; deliberate unequal finger height preserves clearance below the arrow.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "3808dced-acba-4c34-8f9f-05ba44dfe152"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/gesture two finger flip right_3808dced-acba-4c34-8f9f-05ba44dfe152.svg'
AUTHOR = "gpt-6"

class TwoFingerSwipeRight(Solo48):
    icon_id = 'two-finger-swipe-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("two-finger flip right",)
    keywords = ("hand", "spread fingers", "right arrow")

    def build(self) -> None:
        # Shared finger width eight; the valley and palm also retain eight units.
        self.add_polyline('hand-left',(4,28),(12,32),(12,24))
        self.add_arc('index-tip',(12,24),(20,24),radius_x=4)
        self.add_polyline('finger-valley',(20,24),(20,32),(28,32),(28,26))
        self.add_arc('middle-tip',(28,26),(36,26),radius_x=4)
        self.add_polyline('hand-right',(36,26),(36,30),(44,32),(44,40),(4,40),(4,28))
        for a,b in [('hand-left','index-tip'),('index-tip','finger-valley'),('finger-valley','middle-tip'),('middle-tip','hand-right'),('hand-right','hand-left')]:self.relate('connect',a,b)
        self.add_line('shaft',(4,12),(44,12))
        self.add_polyline('arrowhead',(40,8),(44,12),(40,16))
        self.relate('connect','shaft','arrowhead')
