"""Color palette sample (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca1b998f-0a5f-47b5-a6aa-2effc22a4f39'
SOURCE_PATH = 'icons-json/design/color palette sample_ca1b998f-0a5f-47b5-a6aa-2effc22a4f39.json'
AUTHOR = 'json_to_solo'

class ColorPaletteSampleDesign(Solo48):
    icon_id = 'color-palette-sample-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('color', 'palette', 'sample', 'design')

    def build(self):
        self.add_line('e0', (19, 21), (21, 22))
        self.add_line('e1', (27, 12), (27, 16))
        self.add_line('e2', (19, 34), (22, 33))
        self.add_line('e3', (37, 23), (34, 26))
        self.add_line('e4', (32, 31), (32, 36))
        self.add_bezier('e5', (34, 26), ((32.745, 27.009), (32.724, 28.555), (32.573, 30.073)), ((32.531, 30.464), (32, 30.609), (32, 31)))
        self.add_bezier('e6', (32, 36), ((32, 41.173), (29.331, 43.991), (24.581, 43.991)), ((24.506, 43.991), (24.424, 44), (24.349, 44)), ((24.348, 44), (24.346, 44), (24.345, 44)), ((24.084, 44), (23.823, 43.991), (23.562, 43.991)), ((15.217, 43.991), (8.017, 35.027), (8.017, 26.273)), ((8.017, 26.076), (8, 25.879), (8, 25.682)), ((8, 25.679), (8, 25.676), (8, 25.673)), ((8, 25.264), (8.017, 24.864), (8.017, 24.455)), ((8.017, 14.418), (16.598, 4.009), (26.114, 4.009)), ((26.188, 4.009), (26.263, 4), (26.338, 4)), ((26.339, 4), (26.34, 4), (26.341, 4)), ((26.653, 4), (26.973, 4.009), (27.284, 4.009)), ((33.465, 4.009), (39.992, 9.064), (39.992, 16.2)), ((39.992, 16.334), (40, 16.477), (40, 16.612)), ((40, 16.614), (40, 16.616), (40, 16.618)), ((40, 16.764), (39.983, 16.909), (39.983, 17.055)), ((39.983, 19.145), (38.592, 21.709), (37, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e5', 'e4', 'e6', closed=True)
