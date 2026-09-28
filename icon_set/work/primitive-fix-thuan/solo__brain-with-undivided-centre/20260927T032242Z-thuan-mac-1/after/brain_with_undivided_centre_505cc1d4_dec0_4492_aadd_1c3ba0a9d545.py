"""Brain with Undivided Centre.

Plan: HRECT centerlines (4,8)-(44,40); mirrored rounded hemispheres share top and bottom notch nodes. Sparse inward folds preserve clear internal channels.
Construction references: Lucide brain: paired lobe contours, shared central fissure and inward curved folds.
Reduction: Reduced the small perimeter wrinkles to broad lobes; preserved the named center treatment and two folds where specified.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '505cc1d4-dec0-4492-aadd-1c3ba0a9d545'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__brain-with-undivided-centre/20260927T032242Z-thuan-mac-1/reference/brain 1_505cc1d4-dec0-4492-aadd-1c3ba0a9d545.svg'
SOURCE_ICON_IDS = ('505cc1d4-dec0-4492-aadd-1c3ba0a9d545',)
SOURCE_PATHS = ('pictographic-primitives/artificial-intelligence/brain 1_505cc1d4-dec0-4492-aadd-1c3ba0a9d545.svg',)
AUTHOR = 'gpt-6'


class BrainWithUndividedCentre(Solo48):
    icon_id = 'brain-with-undivided-centre'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('brain', 'with', 'undivided', 'centre')

    def build(self) -> None:
        # Mirrored scalloped silhouette; the shallow notches at top and bottom
        # retain the undivided centre of the source without a central seam.
        p=[(24,12),(30,8),(36,10),(40,16),(44,22),(40,28),(40,34),(34,38),(28,40),(24,36)]
        controls=[((25,8),(27,8)),((33,8),(35,9)),((41,10),(40,13)),((44,17),(44,19)),((44,25),(41,27)),((42,32),(40,34)),((40,38),(37,38)),((31,40),(30,40)),((26,40),(25,37))]
        for side in (1,-1):
            here=p[0]
            ids=[]
            for j,(end,(c1,c2)) in enumerate(zip(p[1:],controls)):
                flip=lambda q:(24+side*(q[0]-24),q[1])
                n=f'hemisphere-{side}-{j}'
                self.add_bezier(n,flip(here),(flip(c1),flip(c2),flip(end)))
                ids.append(n);here=end
            self.add_contour(f'hemisphere-{side}',*ids)
        self.relate('connect','hemisphere-1','hemisphere--1')
