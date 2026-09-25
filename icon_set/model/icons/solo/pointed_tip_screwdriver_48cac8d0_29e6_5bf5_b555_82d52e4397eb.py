"""A diagonal screwdriver with chamfered grip and a broad triangular point; the tiny grip dot is omitted and the thin shaft uses one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48cac8d0-29e6-5bf5-b555-82d52e4397eb'
SOURCE_PATH = 'pictographic-primitives/tools/tools screwdriver_48cac8d0-29e6-5bf5-b555-82d52e4397eb.svg'
AUTHOR = 'gpt-6'

class PointedTipScrewdriver(Solo48):
    icon_id = 'pointed-tip-screwdriver'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('screwdriver', 'awl', 'pick', 'point', 'hardware', 'repair', 'shaft', 'tool')

    def build(self) -> None:


        self.add_polyline('handle',(6,30),(14,22),(22,22),(26,26),(26,34),(18,42),(6,42),closed=True)
        self.add_line('shaft',(24,24),(33,15))
        self.relate('connect','shaft','handle')
        self.add_polyline('tip',(24,6),(42,6),(42,24),closed=True)
        self.relate('connect','shaft','tip')
