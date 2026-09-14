'evil: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6891103d-f204-4c2b-b7c5-5bb18a962c37'
SOURCE_PATH = 'icons-json/smileys/evil_6891103d-f204-4c2b-b7c5-5bb18a962c37.json'
AUTHOR = 'gpt-6'

class Evil(Solo48):
    icon_id = 'evil'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('evil', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_line('eye-left',(15,17),(20,19))
        self.add_line('eye-right',(28,19),(33,17))
        self.add_polyline('mouth',(16,31),(20,27),(24,32),(28,27),(32,31))
