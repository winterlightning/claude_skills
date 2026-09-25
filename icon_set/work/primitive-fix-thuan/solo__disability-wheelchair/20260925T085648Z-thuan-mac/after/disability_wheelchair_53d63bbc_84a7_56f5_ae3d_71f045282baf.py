"""Fresh reference reconstruction for manual fix request. Preserve complete subject and arrangement."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '53d63bbc-84a7-56f5-ae3d-71f045282baf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__disability-wheelchair/20260925T085648Z-thuan-mac/reference/disability wheelchair_53d63bbc-84a7-56f5-ae3d-71f045282baf.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'disability-wheelchair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    exception = {'reason': 'Preserve recognizable seated posture, restored arm, open circular wheel and foot; accept natural width and wheel-to-seat ink contact. Exact detached head/body gap remains 4 units.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': 'fc822574d623f9cfd7f6f5210703ca9be4e0c09a35286257d3daf915eb0fe182'}
    aliases = ()
    keywords = ()

    def build(self):
        # Shared full_body_ref.png: round head, seated continuous limbs; Lucide accessibility open wheel.
        # Head center (18,8), radius 4; neck (18,20): exactly 8 centerline / 4 ink units.
        self.add_arc('head-a',(14,8),(22,8),radius_x=4)
        self.add_arc('head-b',(22,8),(14,8),radius_x=4)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_line('torso',(18,20),(18,30))
        self.add_polyline('leg',(18,30),(32,30),(37,42),(42,42))
        self.relate('connect','torso','leg')
        self.add_line('arm',(18,22),(28,22))
        self.relate('connect','torso','arm')
        self.add_arc('wheel',(10,26),(26,34),radius_x=10,large_arc=True,sweep=False)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
