"""Apache netbeans logo 1 (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '48e8c7c2-c7e1-4fe0-8486-404b3adf87b1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__apache-netbeans-logo-1/20260926T064521Z-thuan-mac/reference/apache netbeans logo 1_48e8c7c2-c7e1-4fe0-8486-404b3adf87b1.svg'
AUTHOR = "claude-opus-5-5"

class ApacheNetbeansLogo1(Solo48):
    icon_id = 'apache-netbeans-logo-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('apache', 'netbeans', 'logo', '_uncategorized_03')

    def build(self):
        # Revision per review: the cube is wider - it fills the SQUARE keyshape (36 x 36, was
        # 32 x 40 in VRECT_L). Outer hexagon: top (24, 6), upper corners (6, 15)/(42, 15), lower
        # corners (6, 33)/(42, 33), bottom (24, 42); the inner Y meets at (24, 24), its upper
        # edges parallel to the opposite top edges (slope 1:2).
        self.add_polyline('outline', (24, 6), (42, 15), (42, 33), (24, 42), (6, 33), (6, 15), closed=True)
        self.add_polyline('edge-left', (6, 15), (24, 24))
        self.add_polyline('edge-right', (24, 24), (42, 15))
        self.add_line('edge-front', (24, 24), (24, 42))
        for part in ('edge-left', 'edge-right', 'edge-front'):
            self.relate('connect', 'outline', part)
        self.relate('connect', 'edge-left', 'edge-right')
        self.relate('connect', 'edge-left', 'edge-front')
        self.relate('connect', 'edge-right', 'edge-front')
