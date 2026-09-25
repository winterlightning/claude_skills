"""SQUARE (6,6)-(42,42) centerlines. Preserve two attached crosses, unequal towers and low linking wall. Omit window marks and roof/base divisions that formed tiny enclosed regions. Deliberate asymmetric heights follow the reference.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7c03c33-4c66-43c3-b9d3-d90822308a96'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/saint patrick cathedral dublin_f7c03c33-4c66-43c3-b9d3-d90822308a96.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'church-with-two-crossed-spires'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('church', 'cathedral', 'spire', 'cross', 'towers', 'gothic', 'religion', 'worship')

    def build(self):
        self.add_polyline('outline',(6,42),(6,32),(10,32),(10,29),(16,22),(22,29),(22,32),(30,32),(30,24),(36,16),(42,24),(42,42),(30,42),(22,42),(10,42),closed=True)
        for p,x,y in (('left',16,12),('right',36,6)):
            self.add_polyline(p+'-cross-stem',(x,y),(x,y+3),(x,y+10))
            self.add_polyline(p+'-cross-bar',(x-4,y+3),(x,y+3),(x+4,y+3))
            self.relate('connect',p+'-cross-stem',p+'-cross-bar')
            self.relate('connect',p+'-cross-stem','outline')
        self.add_polyline('left-tower',(22,32),(22,42))
        self.add_polyline('right-tower',(30,42),(30,32))
        self.relate('connect','left-tower','outline')
        self.relate('connect','right-tower','outline')
