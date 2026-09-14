"""Text underline (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8a7ef4b-af1c-59bd-bb25-170aedf30b04'
SOURCE_PATH = 'icons-json/interface-essential/text underline_b8a7ef4b-af1c-59bd-bb25-170aedf30b04.json'
AUTHOR = 'json_to_solo'

class TextUnderlineInterfaceEssential(Solo48):
    icon_id = 'text-underline-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'underline', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 42), (42, 42))
        self.add_bezier('sym-e1', (24, 36), ((24.263, 36), (24.734, 36.016), (25, 36)))
        self.add_bezier('sym-e2', (25, 36), ((29.001, 35.763), (32.979, 33.42), (35, 30)))
        self.add_bezier('sym-e3', (35, 30), ((35.818, 28.609), (35.722, 26.587), (36, 25)))
        self.add_bezier('sym-e4', (36, 25), ((36.025, 24.861), (36, 25.139), (36, 25)))
        self.add_line('sym-e5', (36, 25), (36, 6))
        self.add_bezier('sym-e6', (24, 36), ((23.737, 36), (23.266, 36.016), (23, 36)))
        self.add_bezier('sym-e7', (23, 36), ((18.999, 35.763), (15.021, 33.42), (13, 30)))
        self.add_bezier('sym-e8', (13, 30), ((12.182, 28.609), (12.278, 26.587), (12, 25)))
        self.add_bezier('sym-e9', (12, 25), ((11.975, 24.861), (12, 25.139), (12, 25)))
        self.add_line('sym-e10', (12, 25), (12, 6))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c2')
