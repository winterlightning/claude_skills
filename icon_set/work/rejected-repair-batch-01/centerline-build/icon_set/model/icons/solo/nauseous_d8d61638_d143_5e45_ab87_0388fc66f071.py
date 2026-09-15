'nauseous: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8d61638-d143-5e45-ab87-0388fc66f071'
SOURCE_PATH = 'pictographic-primitives/smileys/nauseous_d8d61638-d143-5e45-ab87-0388fc66f071.svg'
AUTHOR = 'gpt-6'

class Nauseous(Solo48):
    icon_id = 'nauseous'
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
        self.add_arc('eye-left',(15,18),(19,16),radius_x=6,sweep=False)
        self.add_arc('eye-right',(29,16),(33,18),radius_x=6,sweep=False)
        self.add_bezier('mouth',(15,31),((17,27),(19,35),(21,31)),((23,27),(25,35),(27,31)),((29,27),(31,35),(33,31)))
