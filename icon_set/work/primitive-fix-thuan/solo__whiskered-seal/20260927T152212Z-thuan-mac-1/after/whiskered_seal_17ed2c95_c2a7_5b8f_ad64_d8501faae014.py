"""Add a centered oval nose inside the seal silhouette. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '17ed2c95-c2a7-5b8f-ad64-d8501faae014'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__whiskered-seal/20260927T152212Z-thuan-mac-1/reference/seal_17ed2c95-c2a7-5b8f-ad64-d8501faae014.svg'
AUTHOR = 'gpt-6'

class WhiskeredSeal(Solo48):
    icon_id = 'whiskered-seal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('seal', 'whiskers', 'marine', 'flippers', 'animal', 'ocean', 'sea', 'front')

    def build(self) -> None:
        """Symbol plan: Add a centered oval nose inside the seal silhouette. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_bezier('body-1',(24,6),((30,6),(34,10),(34,16)))
        self.add_line('body-2',(34,16),(35,24))
        self.add_bezier('body-3',(35,24),((36,32),(39,39),(42,42)))
        self.add_bezier('body-4',(42,42),((40,42),(37,42),(34,42)))
        self.add_bezier('body-5',(34,42),((31,42),(30,37),(28,35)))
        self.add_bezier('body-6',(28,35),((26,39),(22,39),(20,35)))
        self.add_bezier('body-7',(20,35),((18,37),(17,42),(14,42)))
        self.add_bezier('body-8',(14,42),((11,42),(8,42),(6,42)))
        self.add_bezier('body-9',(6,42),((9,39),(12,32),(13,24)))
        self.add_line('body-10',(13,24),(14,16))
        self.add_bezier('body-11',(14,16),((14,10),(18,6),(24,6)))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', closed=True)
        self.add_line('whisker-left-top-1', (14,16),(6,14))
        self.add_contour('whisker-left-top', 'whisker-left-top-1', closed=False)
        self.add_line('whisker-left-low-1', (13,24),(6,26))
        self.add_contour('whisker-left-low', 'whisker-left-low-1', closed=False)
        self.add_line('whisker-right-top-1', (34,16),(42,14))
        self.add_contour('whisker-right-top', 'whisker-right-top-1', closed=False)
        self.add_line('whisker-right-low-1', (35,24),(42,26))
        self.add_contour('whisker-right-low', 'whisker-right-low-1', closed=False)
        self.relate('connect', 'body', 'whisker-left-top')
        self.relate('connect', 'body', 'whisker-right-top')
        self.relate('connect', 'body', 'whisker-left-low')
        self.relate('connect', 'body', 'whisker-right-low')
        self.add_dot('nose',(24,23))
