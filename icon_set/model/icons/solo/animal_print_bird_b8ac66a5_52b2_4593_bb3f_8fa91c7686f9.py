"""Animal print bird (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8ac66a5-52b2-4593-bb3f-8fa91c7686f9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/animal print bird_b8ac66a5-52b2-4593-bb3f-8fa91c7686f9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AnimalPrintBird(Solo48):
    icon_id = 'animal-print-bird'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('animal', 'print', 'bird', '_uncategorized')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_bezier('e0', (12, 7), ((8.801, 9.839), (6.008, 14.55), (6.008, 18.911)), ((6.008, 18.983), (6, 19.064), (6, 19.137)), ((6, 19.295), (6.008, 19.443), (6.008, 19.598)), ((6.008, 23.877), (9.027, 27.723), (13.56, 27.314)), ((15, 27.183), (16.35, 26.602), (17.414, 25.62)), ((21.398, 21.93), (19.811, 14.787), (17.135, 10.819)), ((16.17, 9.395), (14.951, 8.209), (13.699, 7.047)), ((13.249, 6.614), (12.938, 6.303), (12.635, 6)), ((12.332, 6), (12.298, 6.734), (12, 7)))
        self.add_bezier('e1', (35, 22), ((30.975, 25.322), (27.715, 29.981), (28.345, 35.34)), ((28.729, 38.613), (31.069, 41.992), (34.685, 41.992)), ((34.798, 41.992), (34.903, 42), (35.016, 42)), ((35.209, 42), (35.405, 41.992), (35.594, 41.992)), ((39.627, 41.992), (41.992, 37.901), (41.992, 34.285)), ((41.992, 34.212), (42, 34.132), (42, 34.059)), ((42, 33.826), (41.992, 33.589), (41.992, 33.36)), ((41.992, 29.719), (40.036, 25.98), (37.655, 23.329)), ((37.312, 22.945), (35.61, 21.112), (35.291, 21.071)), ((35.07, 21.226), (35.221, 21.845), (35, 22)))
        self.add_contour('c0', 'e0', closed=True)
        self.add_contour('c1', 'e1', closed=True)
