"""Batch-02/burj al arab uae (landmarks), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fef6ca45-0bb0-5b62-bc09-38dce2e48b1d'
SOURCE_PATH = 'icons-json/landmarks/batch-02/burj al arab uae_fef6ca45-0bb0-5b62-bc09-38dce2e48b1d.json'
AUTHOR = 'json_to_solo'

class Batch02BurjAlArabUae(Solo48):
    icon_id = 'batch-02-burj-al-arab-uae'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('batch', 'burj', 'al', 'arab', 'uae', 'landmarks')

    def build(self):
        self.add_line('e0', (40, 44), (8, 44))
        self.add_line('e1', (13, 44), (13, 4))
        self.add_line('e2', (8, 20), (13, 20))
        self.add_bezier('e3', (34, 44), ((34.135, 41.473), (34.129, 38.873), (33.76, 36.345)), ((32.64, 28.555), (28.652, 21.336), (22.068, 15.191)), ((19.422, 12.718), (16.077, 11.164), (13, 9)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
