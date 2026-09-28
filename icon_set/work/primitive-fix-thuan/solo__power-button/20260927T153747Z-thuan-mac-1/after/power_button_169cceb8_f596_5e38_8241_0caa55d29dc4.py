'Power button: smooth reflected open bowl and centered switch with ample separation.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '169cceb8-f596-5e38-8241-0caa55d29dc4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__power-button/20260927T153747Z-thuan-mac-1/reference/power button_169cceb8-f596-5e38-8241-0caa55d29dc4.svg'
AUTHOR = 'gpt-6'

class PowerButton(Solo48):
    icon_id = 'power-button'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('power', 'button', 'interface-essential')

    def build(self) -> None:
        # The switch and open circular ring share the reference's vertical axis.
        self.add_line('switch', (24, 6), (24, 22))
        self.add_bezier('ring-left', (14, 12), ((9, 16), (6, 21), (6, 26)), ((6, 35), (14, 42), (24, 42)))
        self.add_bezier('ring-right', (24, 42), ((34, 42), (42, 35), (42, 26)), ((42, 21), (39, 16), (34, 12)))
        self.add_contour('ring', 'ring-left', 'ring-right')
