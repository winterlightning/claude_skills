"""Common file empty (files), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec6cb18b-47f8-5fc6-be69-95fa07c27623'
SOURCE_PATH = 'icons-json/files/common file empty_ec6cb18b-47f8-5fc6-be69-95fa07c27623.json'
AUTHOR = 'json_to_solo'

class CommonFileEmptyFiles(Solo48):
    icon_id = 'common-file-empty-files'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('common', 'file', 'empty', 'files')

    def build(self):
        self.add_line('e0', (27, 4), (11, 4))
        self.add_line('e1', (8, 8), (8, 41))
        self.add_line('e2', (11, 44), (37, 44))
        self.add_line('e3', (40, 41), (40, 13))
        self.add_bezier('e4', (11, 4), ((9.535, 4), (8.017, 5.164), (8.017, 6.727)), ((8.017, 6.918), (8, 7.109), (8, 7.3)), ((8, 7.409), (8, 7.891), (8, 8)))
        self.add_bezier('e5', (8, 41), ((8.008, 41.1), (8.008, 41.482), (8.017, 41.582)), ((8.017, 43.073), (9.922, 43.618), (11, 44)))
        self.add_bezier('e6', (37, 44), ((37.109, 44), (37.693, 43.991), (37.802, 43.991)), ((39.099, 43.991), (40, 42.309), (40, 41)))
        self.add_bezier('e7', (40, 13), ((39.992, 12.927), (39.992, 12.945), (39.983, 12.882)), ((39.983, 11.664), (39.057, 10.864), (38.333, 10.1)), ((36.901, 8.6), (35.461, 7.127), (34.013, 5.645)), ((33.364, 4.973), (32.606, 4.018), (31.604, 4.018)), ((31.36, 4.018), (31.107, 4), (30.863, 4)), ((29.701, 4), (28.162, 4), (27, 4)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', closed=True)
