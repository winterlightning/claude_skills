'Blood cell: round membrane replaces the faceted trace; two curved indent marks retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '324706d7-2d66-4a91-bead-c314dc987a3f'
SOURCE_PATH = 'pictographic-primitives/health/red blood cell strem_324706d7-2d66-4a91-bead-c314dc987a3f.svg'
AUTHOR = 'gpt-6'

class RedBloodCellStrem(Solo48):
    icon_id = 'red-blood-cell-strem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('red', 'blood', 'cell', 'strem', 'health')

    def build(self) -> None:
        self.add_arc('outline-top', (6,24), (42,24), radius_x=18, radius_y=18)
        self.add_arc('outline-bottom', (42,24), (6,24), radius_x=18, radius_y=18)
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)

        self.add_arc('upper-indent',(17,19),(20,16),radius_x=3)
        self.add_arc('lower-indent',(28,31),(33,26),radius_x=6,sweep=False)
