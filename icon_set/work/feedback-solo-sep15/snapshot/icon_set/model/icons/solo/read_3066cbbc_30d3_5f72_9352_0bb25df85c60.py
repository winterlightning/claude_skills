"""Read (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3066cbbc-30d3-5f72-9352-0bb25df85c60'
SOURCE_PATH = 'pictographic-primitives/emails/read_3066cbbc-30d3-5f72-9352-0bb25df85c60.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Read(Solo48):
    icon_id = 'read'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('read', 'emails')

    def build(self):
        # Plan: absorb the microscopic terminal detour into the preceding smooth cubic.
        # Reference: original curve and its exact final attachment.
        self.add_line('e0', (33, 28), (31, 30))
        self.add_bezier('e1', (34, 39), ((31.464, 40.522), (28.345, 41.992), (25.276, 41.992)), ((25.019, 41.992), (24.753, 42), (24.495, 42)), ((24.147, 42), (23.82, 41.984), (23.485, 41.984)), ((15.908, 41.984), (9.035, 36.502), (6.81, 29.375)), ((6.393, 28.05), (6.016, 26.536), (6.016, 25.137)), ((6.016, 24.88), (6, 24.622), (6, 24.356)), ((6, 24), (6.016, 23.656), (6.016, 23.313)), ((6.016, 21.423), (6.475, 19.459), (7.129, 17.692)), ((9.731, 10.696), (16.571, 6), (24.033, 6)), ((24.159, 6), (24.28, 6.008), (24.409, 6.008)), ((33.99, 6.008), (41.992, 14.345), (41.992, 23.836)), ((41.992, 24.159), (42, 24.473), (42, 24.795)), ((42, 27.281), (40.994, 31.478), (38.948, 33.057)), ((38.22, 33.622), (37.238, 33.851), (36.346, 33.712)), ((33.352, 33.262), (33.139, 30.405), (33, 28)))
        self.add_bezier('e2', (31, 30), ((29.773, 31.407), (28.811, 32.296), (27.035, 32.975)), ((25.628, 33.499), (24.082, 33.638), (22.609, 33.458)), ((16.317, 32.681), (12.987, 26.266), (15.041, 20.49)), ((16.865, 15.36), (23.026, 13.085), (27.903, 15.18)), ((28.975, 15.638), (29.997, 16.268), (30.783, 17.144)), ((33.401, 20.048), (33.368, 24.358999999999998), (33, 28)))
        self.add_contour('c0', 'e1', closed=False)
        self.add_contour('c1', 'e2', 'e0', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
