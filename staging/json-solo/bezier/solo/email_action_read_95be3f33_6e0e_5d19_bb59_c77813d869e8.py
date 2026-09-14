"""Email action read (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95be3f33-6e0e-5d19-bb59-c77813d869e8'
SOURCE_PATH = 'icons-json/emails/email action read_95be3f33-6e0e-5d19-bb59-c77813d869e8.json'
AUTHOR = 'json_to_solo'

class EmailActionReadEmails(Solo48):
    icon_id = 'email-action-read-emails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('email', 'action', 'read', 'emails')

    def build(self):
        self.add_bezier('sym-e0', (44, 14), ((44, 13.74), (44, 13.27), (44, 13)))
        self.add_bezier('sym-e1', (44, 13), ((44, 10.41), (41.464, 8), (39, 8)))
        self.add_line('sym-e2', (39, 8), (24, 8))
        self.add_line('sym-e3', (24, 8), (9, 8))
        self.add_bezier('sym-e4', (9, 8), ((6.536, 8), (4, 10.41), (4, 13)))
        self.add_bezier('sym-e5', (4, 13), ((4, 13.27), (4, 13.74), (4, 14)))
        self.add_line('sym-e6', (4, 14), (4, 33))
        self.add_bezier('sym-e7', (4, 33), ((4, 33.22), (4, 33.78), (4, 34)))
        self.add_bezier('sym-e8', (4, 34), ((4, 34.59), (4, 34.4), (4, 35)))
        self.add_bezier('sym-e9', (4, 35), ((4, 37.23), (5.955, 40), (8, 40)))
        self.add_bezier('sym-e10', (8, 40), ((8.164, 40), (8.836, 40), (9, 40)))
        self.add_line('sym-e11', (9, 40), (24, 40))
        self.add_line('sym-e12', (24, 40), (39, 40))
        self.add_bezier('sym-e13', (39, 40), ((39.164, 40), (39.836, 40), (40, 40)))
        self.add_bezier('sym-e14', (40, 40), ((42.045, 40), (44, 37.23), (44, 35)))
        self.add_bezier('sym-e15', (44, 35), ((44, 34.4), (44, 34.59), (44, 34)))
        self.add_bezier('sym-e16', (44, 34), ((44, 33.78), (44, 33.22), (44, 33)))
        self.add_line('sym-e17', (44, 33), (44, 14))
        self.add_line('sym-e18', (44, 14), (29, 26))
        self.add_bezier('sym-e19', (29, 26), ((27.405, 27.24), (25.453, 28), (24, 28)))
        self.add_bezier('sym-e20', (24, 28), ((22.547, 28), (20.595, 27.24), (19, 26)))
        self.add_line('sym-e21', (19, 26), (4, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
