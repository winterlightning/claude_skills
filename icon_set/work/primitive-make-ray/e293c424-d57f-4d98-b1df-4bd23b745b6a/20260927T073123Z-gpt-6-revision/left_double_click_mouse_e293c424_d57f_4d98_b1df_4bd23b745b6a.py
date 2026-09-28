"""Double-click mouse with tangent capsule ends, informed by Lucide mouse.

The right version mirrors the left; the offset reserves room for both click arcs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e293c424-d57f-4d98-b1df-4bd23b745b6a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__left-double-click-mouse/20260927T072903Z-thuan-mac-1/reference/left double click mouse_e293c424-d57f-4d98-b1df-4bd23b745b6a.svg'
AUTHOR = "gpt-6"

class LeftDoubleClickMouse(Solo48):
    icon_id = 'left-double-click-mouse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "computers"
    categories = ("computers", "primitives")
    aliases = ()
    keywords = ('mouse', 'double click', 'left click', 'cursor', 'pointer', 'input', 'peripheral', 'computer')

    def build(self):
        # Full mouse capsule with two click marks to its upper left.
        self.add_arc('mouse-top',(24,23),(42,23),radius_x=9,radius_y=9)
        self.add_line('mouse-right',(42,23),(42,33))
        self.add_arc('mouse-bottom',(42,33),(24,33),radius_x=9,radius_y=9)
        self.add_line('mouse-left',(24,33),(24,23))
        self.add_contour('mouse','mouse-top','mouse-right','mouse-bottom','mouse-left',closed=True)
        self.add_line('button-v',(33,14),(33,23))
        self.add_line('button-h',(33,23),(24,23))
        self.add_contour('button','button-v','button-h')
        self.relate('connect','button','mouse')
        self.add_line('click-one',(6,20),(11,6))
        self.add_line('click-two',(14,23),(18,13))
