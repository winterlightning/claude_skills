'A seated figure crosses both legs in front of the torso and raises both arms in a broad curve overhead. The circular head sits between the open ends of the arms.\nConstruction: Bounds (6,6)-(42,42). Mirror rounded arms; retain crossed legs. Remove doubled body outline and hands.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f67610a5-7a4d-4827-a29e-81df7c544fc5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-overhead-stretch/20260927T091411Z-thuan-mac-1/reference/yoga arms stretch_f67610a5-7a4d-4827-a29e-81df7c544fc5.svg'
AUTHOR = "gpt-6"

class SeatedOverheadStretch(Solo48):
    icon_id = 'seated-overhead-stretch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('seated', 'overhead', 'stretch', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (20, 15), (28, 15), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-bottom', (28, 15), (20, 15), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('arm-l', (6, 6), (6, 10))
        self.add_bezier('shoulder-l', (6, 10), ((6, 20), (12, 28), (20, 28)))
        self.add_line('shoulder-center-l', (20, 28), (24, 28))
        self.add_line('shoulder-center-r', (24, 28), (28, 28))
        self.add_bezier('shoulder-r', (28, 28), ((36, 28), (42, 20), (42, 10)))
        self.add_line('arm-r', (42, 10), (42, 6))
        self.add_contour('arms', 'arm-l', 'shoulder-l', 'shoulder-center-l', 'shoulder-center-r', 'shoulder-r', 'arm-r', closed=False)
        self.add_line('torso', (24, 28), (24, 38))
        self.relate("connect", 'arms', 'torso')
        self.add_polyline('leg-l', (8, 34), (24, 38), (40, 42), closed=False)
        self.add_polyline('leg-r', (40, 34), (24, 38), (8, 42), closed=False)
        self.relate("connect", 'leg-l', 'leg-r')
        self.relate("connect", 'leg-l', 'torso')
        self.relate("connect", 'leg-r', 'torso')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
