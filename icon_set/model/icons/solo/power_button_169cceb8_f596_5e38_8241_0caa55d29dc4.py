'Power button: smooth reflected open bowl and centered switch with ample separation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '169cceb8-f596-5e38-8241-0caa55d29dc4'
SOURCE_PATH = 'icons-json/interface-essential/power button_169cceb8-f596-5e38-8241-0caa55d29dc4.json'
AUTHOR = 'gpt-6'

class PowerButton(Solo48):
    icon_id = 'power-button'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('power', 'button', 'interface-essential')

    def build(self) -> None:
        self.add_line('switch',(24,4),(24,22))
        self.add_bezier('ring-left',(14,12),((10,15),(8,20),(8,26)),((8,36),(15,44),(24,44)))
        self.add_bezier('ring-right',(24,44),((33,44),(40,36),(40,26)),((40,20),(38,15),(34,12)))
        self.add_contour('ring','ring-left','ring-right')
