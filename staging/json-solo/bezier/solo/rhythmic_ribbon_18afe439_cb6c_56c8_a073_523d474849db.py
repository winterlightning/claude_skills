"""Rhythmic ribbon (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18afe439-cb6c-56c8-a073-523d474849db'
SOURCE_PATH = 'icons-json/sports/rhythmic ribbon_18afe439-cb6c-56c8-a073-523d474849db.json'
AUTHOR = 'json_to_solo'

class RhythmicRibbonSports(Solo48):
    icon_id = 'rhythmic-ribbon-sports'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('rhythmic', 'ribbon', 'sports')

    def build(self):
        self.add_line('e0', (29, 22), (26, 20))
        self.add_line('e1', (23, 29), (8, 44))
        self.add_bezier('e2', (40, 10), ((39.865, 9.845), (39.84, 10.009), (39.688, 9.873)), ((38.787, 9.027), (37.954, 8.082), (36.994, 7.309)), ((34.771, 5.518), (31.865, 4.009), (29.053, 4.009)), ((28.829, 4.009), (28.613, 4), (28.398, 4)), ((28.394, 4), (28.391, 4), (28.387, 4)), ((28.194, 4), (28, 4.009), (27.798, 4.009)), ((25.128, 4.009), (22.105, 5.991), (21.718, 8.991)), ((21.592, 9.973), (21.895, 10.945), (22.577, 11.609)), ((23.571, 12.573), (25.272, 12.6), (26.509, 12.9)), ((28.724, 13.436), (31.217, 14.436), (32.758, 16.309)), ((33.415, 17.109), (33.945, 18.036), (34.232, 19.073)), ((34.661, 20.673), (34.324, 22.982), (32.497, 23.309)), ((31.402, 23.5), (29.943, 22.509), (29, 22)))
        self.add_bezier('e3', (26, 20), ((23.945, 18.891), (19.604, 17.873), (18.139, 20.655)), ((17.785, 21.318), (17.592, 22.173), (17.794, 22.936)), ((18.543, 25.7), (21.004, 27.436), (23, 29)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1')
