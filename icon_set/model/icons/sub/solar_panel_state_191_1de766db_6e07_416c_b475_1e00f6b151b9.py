"""Solar Panel: A wide trapezoidal panel is divided into four sections by a horizontal crossbar and central vertical line. The vertical line continues downward as a single supporting post.

Construction: The source trapezoidal panel has four cells and a central support continuing below.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1de766db-6e07-416c-b475-1e00f6b151b9'
SOURCE_PATH = 'pictographic-primitives/state/panel_1de766db-6e07-416c-b475-1e00f6b151b9.svg'
AUTHOR = 'gpt-6'


class SolarPanelState191(Sub32):
    icon_id = 'solar-panel-state-191'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('solar', 'panel', 'wide', 'trapezoidal', 'divided', 'four', 'sections', 'horizontal')

    def build(self):
        self.add_polyline('panel',(8,4),(24,4),(30,20),(2,20),closed=True)
        self.add_line('horizontal',(5,12),(27,12))
        self.add_line('vertical',(16,4),(16,28))
        self.relate('connect','panel','horizontal')
        self.relate('connect','panel','vertical')
        self.relate('connect','horizontal','vertical')
