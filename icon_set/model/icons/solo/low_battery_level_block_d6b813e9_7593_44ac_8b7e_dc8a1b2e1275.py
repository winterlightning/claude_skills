"""Low Battery Level. Battery with a low upright rectangular charge block and separately outlined right terminal. Source terminal divider preserved with shared endpoint joins. Symmetry about y=24, envelope (4,10)-(44,38). Lucide battery-full contributes the simple case and charge layout; small corner curves omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'd6b813e9-7593-44ac-8b7e-dc8a1b2e1275'
SOURCE_PATH = 'pictographic-primitives/devices/charging battery low_d6b813e9-7593-44ac-8b7e-dc8a1b2e1275.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'low-battery-level-block'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'devices'
    aliases = ('Low Battery Level',)
    keywords = ('low', 'battery', 'level')
    def build(self):
        self.add_polyline('case',(4,10),(36,10),(36,20),(36,28),(36,38),(4,38),closed=True)
        self.add_polyline('terminal',(36,20),(44,20),(44,28),(36,28))
        self.relate('connect','case','terminal')
        self.add_polyline('charge',(12,18),(20,18),(20,30),(12,30),closed=True)
