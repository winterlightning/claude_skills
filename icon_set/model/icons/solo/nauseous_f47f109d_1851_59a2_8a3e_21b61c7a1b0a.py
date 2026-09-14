'nauseous-smileys: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f47f109d-1851-59a2-8a3e-21b61c7a1b0a'
SOURCE_PATH = 'icons-json/smileys/nauseous_f47f109d-1851-59a2-8a3e-21b61c7a1b0a.json'
AUTHOR = 'gpt-6'

class NauseousSmileys(Solo48):
    icon_id = 'nauseous-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('nauseous', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_polyline('eye-left',(16,16),(20,18),(16,20))
        self.add_polyline('eye-right',(32,16),(28,18),(32,20))
        self.add_bezier('mouth',(15,31),((17,27),(19,35),(21,31)),((23,27),(25,35),(27,31)),((29,27),(31,35),(33,31)))
