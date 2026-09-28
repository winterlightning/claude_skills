'Car Power Window Switch.\nSymbol plan: Vertical switch body fits VRECT_L(8,4)-(40,44), seam y24. Two opposing chevrons occupy their own bands with8-unit wall clearances.\nConstruction reference: Lucide bot: sparse controls inside one structural body.\nOriginal reference: SOURCE_PATH below.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e8aae3d0-0e34-46f8-b97a-5d2beab999fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__power-window-rocker-switch/20260927T170540Z-thuan-mac-1/reference/power window lockout_e8aae3d0-0e34-46f8-b97a-5d2beab999fb.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'power-window-rocker-switch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('power', 'window', 'rocker', 'switch')

    def build(self):
        # Sloped rocker face, rounded top right, and separate up/down marks.
        self.add_line('slope',(8,24),(16,4))
        self.add_line('top',(16,4),(36,4))
        self.add_arc('corner',(36,4),(40,8),radius_x=4)
        self.add_line('right',(40,8),(40,44))
        self.add_line('bottom',(40,44),(8,44))
        self.add_line('left',(8,44),(8,24))
        self.add_contour('panel','slope','top','corner','right','bottom','left',closed=True)
        self.add_line('seam',(8,24),(40,24))
        self.relate('connect','panel','seam')
        self.add_polyline('up',(22,15),(27,13),(31,15))
        self.add_polyline('down',(22,33),(27,35),(31,33))
