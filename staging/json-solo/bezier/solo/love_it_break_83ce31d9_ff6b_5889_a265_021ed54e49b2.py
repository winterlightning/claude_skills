"""Love it break (social), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83ce31d9-ff6b-5889-a265-021ed54e49b2'
SOURCE_PATH = 'icons-json/social/love it break_83ce31d9-ff6b-5889-a265-021ed54e49b2.json'
AUTHOR = 'json_to_solo'

class LoveItBreakSocial(Solo48):
    icon_id = 'love-it-break-social'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('love', 'it', 'break', 'social')

    def build(self):
        self.add_line('e0', (9, 27), (24, 40))
        self.add_line('e1', (24, 40), (38, 28))
        self.add_line('e2', (26, 12), (21, 17))
        self.add_line('e3', (21, 17), (28, 23))
        self.add_line('e4', (28, 23), (22, 28))
        self.add_bezier('e5', (25, 13), ((23.118, 10.549), (21.127, 9.406), (17.991, 8.556)), ((16.991, 8.286), (15.9, 8.017), (14.845, 8.017)), ((14.782, 8.008), (14.709, 8.008), (14.636, 8)), ((14.634, 8), (14.632, 8), (14.629, 8)), ((14.477, 8), (14.316, 8.008), (14.164, 8.008)), ((9.045, 8.008), (4.009, 11.764), (4.009, 16.724)), ((4.009, 16.857), (4, 16.981), (4, 17.114)), ((4, 17.116), (4, 17.118), (4, 17.12)), ((4, 17.314), (4.009, 17.516), (4.009, 17.718)), ((4.009, 20.918), (6.527, 24.844), (9, 27)))
        self.add_bezier('e6', (38, 28), ((40.882, 25.507), (43.991, 21.844), (43.991, 17.979)), ((43.991, 17.855), (44, 17.73), (44, 17.598)), ((44, 17.596), (44, 17.594), (44, 17.592)), ((44, 17.331), (43.982, 17.061), (43.982, 16.8)), ((43.982, 12.825), (40.709, 9.364), (36.673, 8.354)), ((36.009, 8.194), (35.309, 8.008), (34.618, 8.008)), ((34.473, 8.008), (34.327, 8), (34.182, 8)), ((33.964, 8), (33.745, 8.017), (33.527, 8.017)), ((30.4, 8.017), (27.9, 9.895), (26, 12)))
        self.add_bezier('e7', (22, 28), ((21.955, 28.211), (21.918, 28.573), (21.909, 28.817)), ((21.891, 29.288), (23.673, 32.242), (24, 33)))
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e6', 'e2', 'e3', 'e4', 'e7')
