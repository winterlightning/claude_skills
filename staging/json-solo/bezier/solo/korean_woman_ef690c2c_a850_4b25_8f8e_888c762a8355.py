"""Korean woman (avatars), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef690c2c-a850-4b25-8f8e-888c762a8355'
SOURCE_PATH = 'icons-json/avatars/korean woman_ef690c2c-a850-4b25-8f8e-888c762a8355.json'
AUTHOR = 'json_to_solo'

class KoreanWomanAvatars(Solo48):
    icon_id = 'korean-woman-avatars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('korean', 'woman', 'avatars')

    def build(self):
        self.add_line('e0', (20, 12), (20, 8))
        self.add_bezier('e1', (36, 28), ((37.145, 27.975), (38.064, 28.109), (39.182, 28.371)), ((41.736, 28.96), (43.991, 31.141), (43.991, 33.684)), ((43.991, 33.734), (44, 33.776), (44, 33.825)), ((44, 33.826), (44, 33.827), (44, 33.827)), ((44, 33.971), (43.991, 34.105), (43.991, 34.248)), ((43.991, 37.229), (40.864, 39.992), (37.673, 39.992)), ((37.545, 39.992), (37.418, 40), (37.291, 40)), ((37.29, 40), (37.289, 40), (37.288, 40)), ((37.234, 40), (37.172, 40), (37.109, 39.992)), ((35.445, 39.992), (33.655, 39.091), (32.609, 37.92)), ((32.064, 37.305), (31.391, 36.674), (31, 36)))
        self.add_bezier('e2', (36, 28), ((35.318, 30.998), (33.118, 33.709), (31, 36)))
        self.add_bezier('e3', (36, 28), ((36.355, 26.038), (36.118, 23.979), (36, 22)))
        self.add_bezier('e4', (20, 12), ((20.664, 13.465), (21.609, 15.175), (22.609, 16.48)), ((25.909, 20.766), (30.645, 21.621), (36, 22)))
        self.add_bezier('e5', (20, 12), ((19.064, 13.617), (18.609, 15.503), (17.345, 16.926)), ((13.8, 20.909), (9.345, 21.747), (4, 22)))
        self.add_bezier('e6', (36, 22), ((35.945, 20.644), (35.664, 19.646), (35.3, 18.324)), ((34.191, 14.282), (30.718, 11.006), (26.691, 9.305)), ((25.118, 8.632), (23.182, 8), (21.418, 8)), ((21.073, 8), (20.355, 8), (20, 8)))
        self.add_bezier('e7', (20, 8), ((19.545, 8), (19.464, 8.017), (19.018, 8.017)), ((12.436, 8.017), (5.955, 13.659), (4.473, 19.402)), ((4.345, 19.899), (4.009, 20.8), (4.009, 21.28)), ((4.009, 21.314), (4, 21.347), (4, 21.381)), ((4, 21.693), (4, 21.688), (4, 22)))
        self.add_bezier('e8', (31, 36), ((27.945, 38.291), (24.673, 39.992), (20.609, 39.992)), ((20.473, 39.992), (20.345, 40), (20.209, 40)), ((19.991, 40), (19.764, 39.992), (19.545, 39.992)), ((10.927, 39.992), (4.018, 32.564), (4.018, 24.842)), ((4.009, 24.741), (4.009, 24.648), (4, 24.556)), ((4, 23.806), (4, 22.749), (4, 22)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e0')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
