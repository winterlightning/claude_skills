"""Pop up alert (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f2d1b12-2c74-4b57-91be-a4a84e1da748'
SOURCE_PATH = 'icons-json/apps/pop up alert_1f2d1b12-2c74-4b57-91be-a4a84e1da748.json'
AUTHOR = 'json_to_solo'

class PopUpAlertApps(Solo48):
    icon_id = 'pop-up-alert-apps'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('pop', 'up', 'alert', 'apps')

    def build(self):
        self.add_line('e0', (24, 4), (24, 9))
        self.add_line('e1', (8, 9), (11, 13))
        self.add_line('e2', (37, 13), (40, 9))
        self.add_line('e3', (33, 44), (15, 44))
        self.add_line('e4', (13, 42), (13, 19))
        self.add_line('e5', (15, 18), (33, 18))
        self.add_line('e6', (35, 19), (35, 42))
        self.add_bezier('e7', (21, 28), ((21.185, 27.273), (20.935, 26.318), (21.44, 25.745)), ((23.183, 23.736), (27.006, 24.436), (27.402, 27.373)), ((27.764, 30.009), (25.364, 30.145), (24.337, 31.673)), ((24.025, 32.127), (24.076, 32.491), (24, 33)))
        self.add_bezier('e8', (24, 38), ((24, 37.7), (24, 37.3), (24, 37)))
        self.add_bezier('e9', (15, 44), ((14.966, 44), (14.661, 43.991), (14.627, 43.991)), ((13.752, 43.991), (13.269, 42.682), (13, 42)))
        self.add_bezier('e10', (13, 19), ((13.522, 17.736), (13.821, 18.536), (15, 18)))
        self.add_bezier('e11', (33, 18), ((34.053, 18.509), (34.545, 17.836), (35, 19)))
        self.add_bezier('e12', (35, 42), ((34.739, 42.591), (34.417, 43.564), (33.802, 43.855)), ((33.634, 43.936), (33.168, 43.918), (33, 44)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', closed=True)
