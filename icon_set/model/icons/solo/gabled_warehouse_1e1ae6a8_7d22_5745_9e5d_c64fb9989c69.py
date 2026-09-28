from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e1ae6a8-7d22-5745-9e5d-c64fb9989c69'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse_1e1ae6a8-7d22-5745-9e5d-c64fb9989c69.svg'
AUTHOR = 'gpt-6-astra'


class GabledWarehouse(Solo48):
    icon_id = 'gabled-warehouse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    categories = ("primitives", "shipping")
    aliases = ()
    keywords = ('warehouse', 'building', 'storage', 'depot', 'doorway', 'shipping')

    def build(self) -> None:
        # Square centerlines (6,6)-(42,42); mirror around x=24.
        axis = 24
        left, right = 6, 2*axis-6
        door_left, door_right = 16, 2*axis-16
        self.add_polyline("building", (left,42), (left,18), (axis,6), (right,18), (right,42), (door_right,42), (door_right,24), (door_left,24), (door_left,42), (left,42))
