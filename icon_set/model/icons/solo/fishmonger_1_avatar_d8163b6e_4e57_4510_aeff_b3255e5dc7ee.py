"""fishmonger-1: open waterproof apron straps.
Distinct-avatar plan: preserve reference identity; use open waterproof apron straps.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 26; shoulder top 30; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'd8163b6e-4e57-4510-aeff-b3255e5dc7ee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fishmonger-1-avatar/20260927T032256Z-thuan-mac-1/reference/fishmonger_d8163b6e-4e57-4510-aeff-b3255e5dc7ee.svg'
SOURCE_HEAD_ICON_ID = 'fishmonger-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26

class Fishmonger1Avatar(Solo48):
    icon_id = 'fishmonger-1-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('fishmonger', '1', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_arc('cap-left',(12,16),(24,4),radius_x=12)
        self.add_arc('cap-right',(24,4),(36,16),radius_x=12)
        self.add_contour('cap','cap-left','cap-right')
        self.add_polyline('brim',(8,16),(12,16),(14,16),(34,16),(36,16),(40,16))
        self.relate('connect','cap','brim')
        self.add_arc('face',(34,16),(14,16),radius_x=10,radius_y=10)
        self.relate('connect','face','brim')

        # User reference shoulders frame the fish held across the lower bust.
        # The fish carries the trade; its tail meets the body at one shared node.
        self.add_arc('fish-upper-left',(10,40),(20,36),radius_x=10,radius_y=4)
        self.add_arc('fish-upper-right',(20,36),(30,40),radius_x=10,radius_y=4)
        self.add_arc('fish-lower-right',(30,40),(20,44),radius_x=10,radius_y=4)
        self.add_arc('fish-lower-left',(20,44),(10,40),radius_x=10,radius_y=4)
        self.add_contour('fish-body','fish-upper-left','fish-upper-right','fish-lower-right','fish-lower-left',closed=True)
        self.add_polyline('tail',(30,40),(40,34),(40,44),(30,40),closed=True)
        self.relate('connect','fish-body','tail')
