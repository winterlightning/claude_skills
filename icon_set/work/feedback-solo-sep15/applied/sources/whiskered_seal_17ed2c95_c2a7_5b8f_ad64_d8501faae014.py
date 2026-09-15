"""Add a centered oval nose inside the seal silhouette. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '17ed2c95-c2a7-5b8f-ad64-d8501faae014'
SOURCE_PATH = 'pictographic-primitives/animals/seal_17ed2c95-c2a7-5b8f-ad64-d8501faae014.svg'
AUTHOR = 'gpt-6'

class WhiskeredSeal(Solo48):
    icon_id = 'whiskered-seal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('seal', 'whiskers', 'marine', 'flippers', 'animal', 'ocean', 'sea', 'front')

    def build(self) -> None:
        """Symbol plan: Add a centered oval nose inside the seal silhouette. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_bezier('body-1', (24, 6), *(((30.40593167, 6), (36.17366573, 9.85418684), (38, 16)),))
        self.add_line('body-2', (38, 16), (39, 24))
        self.add_arc('body-3', (39, 24), (42, 42), radius_x=46, radius_y=46, sweep=False)
        self.add_bezier('body-4', (42, 42), *(((39.72891624, 42), (37.27108376, 42), (35, 42)),))
        self.add_line('body-5', (35, 42), (32, 42))
        self.add_bezier('body-6', (32, 42), *(((26.89899073, 42), (21.10100927, 42), (16, 42)),))
        self.add_line('body-7', (16, 42), (13, 42))
        self.add_bezier('body-8', (13, 42), *(((10.72891624, 42), (8.27108376, 42), (6, 42)),))
        self.add_arc('body-9', (6, 42), (9, 24), radius_x=46, radius_y=46, sweep=False)
        self.add_line('body-10', (9, 24), (10, 16))
        self.add_bezier('body-11', (10, 16), *(((11.82633427, 9.85418684), (17.59406833, 6), (24, 6)),))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', closed=True)
        self.add_line('whisker-left-top-1', (10, 16), (6, 13))
        self.add_contour('whisker-left-top', 'whisker-left-top-1', closed=False)
        self.add_line('whisker-left-low-1', (9, 24), (6, 27))
        self.add_contour('whisker-left-low', 'whisker-left-low-1', closed=False)
        self.add_line('whisker-right-top-1', (38, 16), (42, 13))
        self.add_contour('whisker-right-top', 'whisker-right-top-1', closed=False)
        self.add_line('whisker-right-low-1', (39, 24), (42, 27))
        self.add_contour('whisker-right-low', 'whisker-right-low-1', closed=False)
        self.relate('connect', 'body', 'whisker-left-top')
        self.relate('connect', 'body', 'whisker-right-top')
        self.relate('connect', 'body', 'whisker-left-low')
        self.relate('connect', 'body', 'whisker-right-low')
        self.add_arc('nose-top', (18, 22), (30, 22), radius_x=6, radius_y=4)
        self.add_arc('nose-bottom', (30, 22), (18, 22), radius_x=6, radius_y=4)
        self.add_contour('nose', 'nose-top', 'nose-bottom', closed=True)
