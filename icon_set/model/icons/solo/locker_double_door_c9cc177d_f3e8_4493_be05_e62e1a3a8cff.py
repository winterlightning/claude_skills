"""A two-door locker with paired vertical handles. SQUARE extremes (6,6)-(42,42). No useful exact Lucide match; construct matched rectangular doors and equally spaced handles, retaining every identifying feature."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9cc177d-f3e8-4493-be05-e62e1a3a8cff'
SOURCE_PATH = 'pictographic-primitives/symbol/locker_c9cc177d-f3e8-4493-be05-e62e1a3a8cff.svg'
AUTHOR = 'gpt-6'


class LockerDoubleDoor(Solo48):
    icon_id = 'locker-double-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('locker', 'cabinet', 'wardrobe', 'cupboard', 'storage', 'doors', 'closet', 'furniture')

    def build(self) -> None:
        self.add_polyline('cabinet',(6,6),(24,6),(42,6),(42,42),(24,42),(6,42),(6,6),closed=True)
        self.add_line('divider',(24,6),(24,42))
        self.relate('connect','cabinet','divider')
        self.add_line('handle-left',(15,24),(15,28))
        self.add_line('handle-right',(33,24),(33,28))
