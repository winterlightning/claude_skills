"""Trouble (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7062d366-ddbc-51df-b6fd-09ce8c2ccd5d'
SOURCE_PATH = 'icons-json/smileys/trouble_7062d366-ddbc-51df-b6fd-09ce8c2ccd5d.json'
AUTHOR = 'json_to_solo'

class TroubleSmileys(Solo48):
    icon_id = 'trouble-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('trouble', 'smileys')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (31, 16), ((30.627, 16.2), (30.3, 15.682), (30, 16)))
        self.add_bezier('sym-e3', (30, 16), ((29.532, 16.492), (29, 17.264), (29, 18)))
        self.add_bezier('sym-e4', (29, 18), ((29, 18.637), (29.696, 19.519), (30, 20)))
        self.add_bezier('sym-e5', (30, 20), ((30.318, 20.509), (30.518, 20.691), (31, 21)))
        self.add_bezier('sym-e6', (24, 27), ((27.841, 27), (31.676, 29.155), (34, 33)))
        self.add_bezier('sym-e7', (17, 16), ((17.373, 16.2), (17.7, 15.682), (18, 16)))
        self.add_bezier('sym-e8', (18, 16), ((18.468, 16.492), (19, 17.264), (19, 18)))
        self.add_bezier('sym-e9', (19, 18), ((19, 18.637), (18.304, 19.519), (18, 20)))
        self.add_bezier('sym-e10', (18, 20), ((17.682, 20.509), (17.482, 20.691), (17, 21)))
        self.add_bezier('sym-e11', (24, 27), ((20.159, 27), (16.324, 29.155), (14, 33)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11')
        self.relate('connect', 'sym-c2', 'sym-c4')
