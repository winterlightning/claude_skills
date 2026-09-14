'Star shield: balanced curved shield flanks with a smaller centered five-point star. Lucide shield guides the continuous lower sides.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e9c2606-3dd8-5da8-9c75-2314a86e8c6e'
SOURCE_PATH = 'icons-json/protection/badge star 2_8e9c2606-3dd8-5da8-9c75-2314a86e8c6e.json'
AUTHOR = 'gpt-6'

class BadgeStar2(Solo48):
    icon_id = 'badge-star-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('badge', 'star', 'protection')

    def build(self) -> None:
        # Square shield with broad shoulders; x=24 owns both mirrored sides.
        self.add_bezier('top-left',(24,6),((18,10),(12,10),(6,10)))
        self.add_line('left',(6,10),(6,27))
        self.add_bezier('lower-left',(6,27),((6,40),(16,41),(24,42)))
        self.add_bezier('lower-right',(24,42),((32,41),(42,40),(42,27)))
        self.add_line('right',(42,27),(42,10))
        self.add_bezier('top-right',(42,10),((36,10),(30,10),(24,6)))
        self.add_contour('shield','top-left','left','lower-left','lower-right','right','top-right',closed=True)
        self.add_polyline('star',(24,16),(27,22),(33,22),(28,26),(30,32),(24,28),(18,32),(20,26),(15,22),(21,22),closed=True)
