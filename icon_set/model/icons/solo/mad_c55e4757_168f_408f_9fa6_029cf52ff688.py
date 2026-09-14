'mad: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c55e4757-168f-408f-9fa6-029cf52ff688'
SOURCE_PATH = 'icons-json/smileys/mad_c55e4757-168f-408f-9fa6-029cf52ff688.json'
AUTHOR = 'gpt-6'

class Mad(Solo48):
    icon_id = 'mad'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('mad', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_line('eye-left',(15,17),(20,19))
        self.add_line('eye-right',(28,19),(33,17))
        self.add_arc('mouth',(17,32),(31,32),radius_x=7,radius_y=4)
