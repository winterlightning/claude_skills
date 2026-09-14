"""Hole (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13397b20-19ce-44c1-a306-7a5124c9bd71'
SOURCE_PATH = 'icons-json/_uncategorized_22/hole_13397b20-19ce-44c1-a306-7a5124c9bd71.json'
AUTHOR = 'json_to_solo'

class Hole13397b20(Solo48):
    icon_id = 'hole-13397b20'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('hole', '_uncategorized')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
