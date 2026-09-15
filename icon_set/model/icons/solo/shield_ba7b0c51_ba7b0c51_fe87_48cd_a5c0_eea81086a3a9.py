"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ba7b0c51-fe87-48cd-a5c0-eea81086a3a9'
SOURCE_PATH = 'pictographic-primitives/protection/shield_ba7b0c51-fe87-48cd-a5c0-eea81086a3a9.svg'
AUTHOR = 'gpt-6'

class ShieldBa7b0c51(Solo48):
    icon_id = 'shield-ba7b0c51'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (24, 4), (28, 7))
        self.add_bezier('e1', (24, 44), ((14.173, 37.773), (8.008, 26), (8.008, 13.645)), ((8.008, 13.27), (8, 12.894), (8, 12.518)), ((8, 12.512), (8, 12.506), (8, 12.5)), ((8, 12.209), (8.008, 11.909), (8.008, 11.609)), ((8.025, 11.436), (8, 10.691), (8.059, 10.573)), ((8.101, 10.518), (11.571, 9.882), (11.992, 9.764)), ((15.141, 8.891), (18.147, 7.418), (21.002, 5.782)), ((21.651, 5.409), (22.299, 5.036), (22.939, 4.645)), ((23.166, 4.5), (23.335, 4.264), (23.571, 4.145)), ((24.042, 4), (23.52, 4.282), (24, 4)))
        self.add_bezier('e2', (28, 7), ((29.979, 8.282), (33.777, 9.2), (36.051, 9.773)), ((36.472, 9.873), (39.933, 10.545), (39.983, 10.6)), ((39.983, 10.664), (39.983, 10.727), (39.983, 10.782)), ((39.983, 11.104), (40, 11.417), (40, 11.731)), ((40, 11.736), (40, 11.74), (40, 11.745)), ((40, 12.155), (39.983, 12.573), (39.983, 12.991)), ((39.983, 25.882), (34.173, 37.291), (24, 44)))
        self.add_contour('c0', 'e1', 'e0', 'e2', closed=True)
