"""Presentation microphone (office), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc33bff7-8291-5e3a-956d-f632ad5d2bee'
SOURCE_PATH = 'icons-json/office/presentation microphone_dc33bff7-8291-5e3a-956d-f632ad5d2bee.json'
AUTHOR = 'json_to_solo'

class PresentationMicrophoneOffice(Solo48):
    icon_id = 'presentation-microphone-office'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'microphone', 'office')

    def build(self):
        self.add_line('e0', (24, 35), (24, 44))
        self.add_line('e1', (17, 44), (31, 44))
        self.add_line('e2', (34, 21), (34, 11))
        self.add_line('e3', (14, 11), (14, 22))
        self.add_bezier('e4', (40, 22), ((40, 22.127), (39.988, 22.436), (39.988, 22.555)), ((39.988, 28.918), (32.628, 34.818), (24, 34.909)), ((15.335, 35), (8.012, 28.945), (8.012, 22.636)), ((8.012, 22.482), (8, 22.155), (8, 22)))
        self.add_bezier('e5', (14, 22), ((14, 27.655), (22.412, 32.209), (29.231, 28.8)), ((32.825, 27.009), (34, 24.027), (34, 21)))
        self.add_bezier('e6', (34, 11), ((34, 7.355), (29.428, 4.009), (24.394, 4.009)), ((24.297, 4), (24.2, 4), (24.115, 4)), ((24.113, 4), (24.112, 4), (24.111, 4)), ((23.914, 4), (23.717, 4.009), (23.532, 4.009)), ((18.351, 4.009), (14, 7.309), (14, 11)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e5', 'e2', 'e6', 'e3', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
