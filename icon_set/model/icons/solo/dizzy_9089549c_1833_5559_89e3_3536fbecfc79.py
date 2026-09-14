'dizzy: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9089549c-1833-5559-89e3-3536fbecfc79'
SOURCE_PATH = 'icons-json/smileys/dizzy_9089549c-1833-5559-89e3-3536fbecfc79.json'
AUTHOR = 'gpt-6'

class Dizzy(Solo48):
    icon_id = 'dizzy'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('dizzy', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        for name,x in (('left',18),('right',30)):
            self.add_polyline(name+'-a',(x-2,16),(x,18),(x+2,20))
            self.add_polyline(name+'-b',(x+2,16),(x,18),(x-2,20))
            self.relate('connect',name+'-a',name+'-b')
        self.add_bezier('mouth',(15,31),((17,27),(19,35),(21,31)),((23,27),(25,35),(27,31)),((29,27),(31,35),(33,31)))
