"""A right-facing head enclosure with a continuous rounded skull and neck.

VRECT_XL: ink (4,0)-(60,64), centerlines (6,2)-(58,62).
Source preserves forehead, projecting nose, jaw and open neck. The rear neck
and skull share an exact 3:4:5 tangent; the face is deliberately asymmetric.
Shared human reference: references/human_ref/full_body_ref.png. An isolated
head has no detached head/body gap. No useful Lucide side-head match was found.
Hosting (compose.py): plus blocked; heart blocked; check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (human-head-side-profile VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '66eefdff-ac9b-4760-951f-816ff21b1e05'
SOURCE_PATH = 'container_icons/svg/human-head-side-profile-66eefdff-ac9b-4760-951f-816ff21b1e05.svg'
AUTHOR = 'claude-opus-5-5'


class HumanHeadSideProfile(Container64):
    icon_id = 'human-head-side-profile'
    keyshape = Keyshape.VRECT_L
    category = 'primitives-generate'
    categories = ('container', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('human', 'head', 'side', 'profile', 'mind')

    def build(self) -> None:
        self.add_line('rear-neck', (20, 60), (20, 44))
        self.add_arc('nape', (20, 44), (16, 36), radius_x=10, sweep=False)
        self.add_arc('rear-skull', (16, 36), (10, 24), radius_x=15)
        self.add_arc('crown', (10, 24), (44, 24), radius_x=17, radius_y=20)
        self.add_line('forehead-nose', (44, 24), (54, 36))
        self.add_line('nose-base', (54, 36), (48, 36))
        self.add_line('face', (48, 36), (48, 44))
        self.add_arc('chin', (48, 44), (40, 52), radius_x=8)
        self.add_arc('front-neck-turn', (40, 52), (36, 56), radius_x=4, sweep=False)
        self.add_line('front-neck', (36, 56), (36, 60))
        self.add_contour('outline', 'rear-neck', 'nape', 'rear-skull', 'crown', 'forehead-nose', 'nose-base', 'face', 'chin', 'front-neck-turn', 'front-neck')
