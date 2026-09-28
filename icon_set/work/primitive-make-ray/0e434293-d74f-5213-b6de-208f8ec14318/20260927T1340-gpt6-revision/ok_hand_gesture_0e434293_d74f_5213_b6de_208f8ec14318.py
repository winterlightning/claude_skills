'A hand makes a closed loop with the thumb and index finger at lower-left. Two fingers project upward and the remaining finger curves beside them above the rounded palm.\n\nConstruction: Circular thumb-index loop beneath two extended fingers and a rounded palm. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0e434293-d74f-5213-b6de-208f8ec14318'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ok-hand-gesture/20260927T133654Z-thuan-mac-1/reference/ok hand_0e434293-d74f-5213-b6de-208f8ec14318.svg'
AUTHOR = 'gpt-6'

class OkHandGesture(Solo48):
    icon_id = 'ok-hand-gesture'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('ok', 'hand', 'gesture', 'fingers', 'approval', 'sign')

    def build(self):
        # One hand silhouette surrounds a small thumb-index aperture. Keeping
        # the aperture inside the hand removes the detached circular badge.
        self.add_bezier('thumb-upper',(8,28),((10,21),(13,19),(16,21)))
        self.add_line('index-left',(16,21),(16,8))
        self.add_arc('index-tip',(16,8),(24,8),radius_x=4,radius_y=4)
        self.add_line('index-right',(24,8),(28,20))
        self.add_line('middle-left',(28,20),(32,8))
        self.add_arc('middle-tip',(32,8),(40,8),radius_x=4,radius_y=4)
        self.add_line('middle-right',(40,8),(40,31))
        self.add_bezier('palm',(40,31),((40,39),(34,44),(28,44)))
        self.add_line('palm-bottom',(28,44),(20,44))
        self.add_bezier('thumb-lower',(20,44),((12,44),(8,36),(8,28)))
        self.add_contour('hand','thumb-upper','index-left','index-tip',
                         'index-right','middle-left','middle-tip','middle-right',
                         'palm','palm-bottom','thumb-lower',closed=True)
        self.add_arc('aperture-right',(20,29),(20,33),radius_x=2)
        self.add_arc('aperture-left',(20,33),(20,29),radius_x=2)
        self.add_contour('thumb-index-aperture','aperture-right','aperture-left',closed=True)
