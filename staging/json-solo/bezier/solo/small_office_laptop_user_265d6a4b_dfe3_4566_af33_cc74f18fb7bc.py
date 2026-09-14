"""Small office laptop user (office), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '265d6a4b-dfe3-4566-af33-cc74f18fb7bc'
SOURCE_PATH = 'icons-json/office/small office laptop user_265d6a4b-dfe3-4566-af33-cc74f18fb7bc.json'
AUTHOR = 'json_to_solo'

class SmallOfficeLaptopUserOffice(Solo48):
    icon_id = 'small-office-laptop-user-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('small', 'office', 'laptop', 'user')

    def build(self):
        self.add_line('e0', (26, 35), (26, 34))
        self.add_line('e1', (38, 37), (38, 42))
        self.add_line('e2', (26, 35), (27, 42))
        self.add_line('e3', (26, 35), (25, 33))
        self.add_line('e4', (23, 32), (13, 32))
        self.add_line('e5', (12, 33), (14, 42))
        self.add_line('e6', (38, 42), (27, 42))
        self.add_line('e7', (38, 42), (41, 42))
        self.add_line('e8', (42, 41), (42, 21))
        self.add_line('e9', (41, 20), (24, 6))
        self.add_line('e10', (23, 6), (7, 20))
        self.add_line('e11', (6, 21), (6, 41))
        self.add_line('e12', (7, 42), (14, 42))
        self.add_line('e13', (27, 42), (14, 42))
        self.add_arc('e14-top', (26, 24), (36, 24), radius_x=5)
        self.add_arc('e14-bottom', (36, 24), (26, 24), radius_x=5)
        self.add_bezier('e15', (26, 34), ((26.565, 33.493), (27.535, 32.877), (28.271, 32.632)), ((29.212, 32.329), (30.308, 32.419), (31.282, 32.476)), ((32.19, 32.534), (33.139, 32.427), (34.039, 32.599)), ((36.117, 32.992), (38, 34.832), (38, 37)))
        self.add_bezier('e16', (25, 33), ((24.419, 32.525), (23.72, 32.172), (23, 32)))
        self.add_bezier('e17', (13, 32), ((12.722, 32.278), (12.278, 32.714), (12, 33)))
        self.add_bezier('e18', (41, 42), ((41.262, 41.836), (41.681, 41.885), (41.861, 41.575)), ((41.935, 41.452), (41.926, 41.115), (42, 41)))
        self.add_bezier('e19', (42, 21), ((41.951, 20.894), (41.902, 20.515), (41.853, 20.408)), ((41.689, 20.179), (41.221, 20.164), (41, 20)))
        self.add_bezier('e20', (24, 6), ((23.73, 6), (23.27, 6), (23, 6)))
        self.add_bezier('e21', (7, 20), ((6.82, 20.147), (6.393, 20.122), (6.213, 20.269)), ((6, 20.515), (6.229, 20.738), (6, 21)))
        self.add_bezier('e22', (6, 41), ((6.074, 41.115), (6.057, 41.493), (6.131, 41.624)), ((6.303, 41.918), (6.763, 41.836), (7, 42)))
        self.add_contour('c0', 'e0', 'e15', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e16', 'e4', 'e17', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7', 'e18', 'e8', 'e19', 'e9', 'e20', 'e10', 'e21', 'e11', 'e22', 'e12')
        self.add_contour('c5', 'e13')
        self.add_contour('e14', 'e14-top', 'e14-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
