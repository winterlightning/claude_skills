'devastated: preserve the expression with balanced eyes and a clear mouth; omit redundant tiny eyebrow or blush marks where the three detail rows could not meet MIC4.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcba8556-9d35-5f8d-8f91-745b9f8022a8'
SOURCE_PATH = 'pictographic-primitives/smileys/devastated_bcba8556-9d35-5f8d-8f91-745b9f8022a8.svg'
AUTHOR = 'gpt-6'

class Devastated(Solo48):
    icon_id = 'devastated'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('devastated', 'smileys')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        for name,x in (('left',18),('right',30)):
            self.add_polyline(name+'-a',(x-2,16),(x,18),(x+2,20))
            self.add_polyline(name+'-b',(x+2,16),(x,18),(x-2,20))
            self.relate('connect',name+'-a',name+'-b')
        self.add_arc('mouth',(17,32),(31,32),radius_x=7,radius_y=4)
