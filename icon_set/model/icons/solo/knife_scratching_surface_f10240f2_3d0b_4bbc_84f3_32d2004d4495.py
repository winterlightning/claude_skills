"""A knife tip touches a surface with two short scratch bursts; small handle seam retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f10240f2-3d0b-4bbc-84f3-32d2004d4495'
SOURCE_PATH = 'pictographic-primitives/tools/scratch resistance_f10240f2-3d0b-4bbc-84f3-32d2004d4495.svg'
AUTHOR = 'gpt-6'

class KnifeScratchingSurface(Solo48):
    icon_id = 'knife-scratching-surface'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('scratch', 'resistance', 'knife', 'surface', 'durability', 'hardness', 'test', 'blade')

    def build(self) -> None:
        self.add_polyline('knife',(16,42),(26,16),(30,6),(40,10),(36,20),(32,28),(24,38),(16,42))
        self.add_line('handle-seam',(26,16),(36,20))
        self.relate('connect','handle-seam','knife')
        self.add_polyline('surface',(6,42),(16,42),(42,42))
        self.relate('connect','knife','surface')
        self.add_line('scratch-left',(6,28),(10,32))
        self.add_line('scratch-right',(40,32),(42,30))
