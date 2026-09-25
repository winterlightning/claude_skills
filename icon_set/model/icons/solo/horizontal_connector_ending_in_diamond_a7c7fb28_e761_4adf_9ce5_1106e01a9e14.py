"""Diamond Terminal Point Connector.

Symbol plan: Horizontal connector and diamond terminal, centered at y=24. Diamond owns equal half diagonals; line shares its left vertex.
Keyshape HRECT_M; exact visible bounds (2, 8, 46, 40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7c7fb28-e761-4adf-9ce5-1106e01a9e14'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/end point diamond_a7c7fb28-e761-4adf-9ce5-1106e01a9e14.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'horizontal-connector-ending-in-diamond'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('diamond', 'terminal', 'point', 'connector')

    def build(self):
        self.add_polyline('terminal',(16,24),(30,10),(44,24),(30,38),closed=True)
        self.add_line('connector',(4,24),(16,24));self.relate('connect','terminal','connector')
