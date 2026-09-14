"""Indiferent (smileys), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95ca1914-115c-57dd-8e01-31c3f2e4bf74'
SOURCE_PATH = 'icons-json/smileys/indiferent_95ca1914-115c-57dd-8e01-31c3f2e4bf74.json'
AUTHOR = 'json_to_solo'

class IndiferentSmileys(Solo48):
    icon_id = 'indiferent-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('indiferent', 'smileys')

    def build(self):
        self.add_line('sym-e0', (16, 32), (32, 32))
        self.add_bezier('sym-e1', (24, 4), ((24.136, 4), (23.864, 4), (24, 4)))
        self.add_bezier('sym-e2', (24, 4), ((24.063, 4), (23.946, 4), (24, 4)))
        self.add_bezier('sym-e3', (24, 4), ((31.834, 5.598), (39.776, 11.707), (43, 19)))
        self.add_bezier('sym-e4', (43, 19), ((43.362, 20.321), (43, 21.625), (43, 23)))
        self.add_bezier('sym-e5', (43, 23), ((43, 23.317), (43.997, 23.683), (44, 24)))
        self.add_bezier('sym-e6', (44, 24), ((43.996, 24.38), (43, 24.62), (43, 25)))
        self.add_bezier('sym-e7', (43, 25), ((41.334, 33.976), (32.839, 41.941), (24, 44)))
        self.add_bezier('sym-e8', (24, 44), ((23.789, 43.999), (24.212, 43.999), (24, 44)))
        self.add_bezier('sym-e9', (24, 44), ((23.788, 43.999), (24.211, 43.999), (24, 44)))
        self.add_bezier('sym-e10', (24, 44), ((15.161, 41.941), (6.666, 33.976), (5, 25)))
        self.add_bezier('sym-e11', (5, 25), ((5, 24.62), (4.004, 24.38), (4, 24)))
        self.add_bezier('sym-e12', (4, 24), ((4.003, 23.683), (5, 23.317), (5, 23)))
        self.add_bezier('sym-e13', (5, 23), ((5, 21.625), (4.638, 20.321), (5, 19)))
        self.add_bezier('sym-e14', (5, 19), ((8.224, 11.707), (16.166, 5.598), (24, 4)))
        self.add_bezier('sym-e15', (24, 4), ((24.054, 4), (23.937, 4), (24, 4)))
        self.add_bezier('sym-e16', (24, 4), ((24.136, 4), (23.864, 4), (24, 4)))
        self.add_line('sym-e17', (28, 19), (36, 19))
        self.add_line('sym-e18', (20, 19), (12, 19))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
        self.add_contour('sym-c2', 'sym-e17')
        self.add_contour('sym-c3', 'sym-e18')
