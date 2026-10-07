"""A right-facing head enclosure with a continuous rounded skull and neck.

VRECT_XL: ink (4,0)-(60,64), centerlines (6,2)-(58,62).
Source preserves forehead, projecting nose, jaw and open neck. The rear neck
and skull share an exact 3:4:5 tangent; the face is deliberately asymmetric.
Shared human reference: references/human_ref/full_body_ref.png. An isolated
head has no detached head/body gap. No useful Lucide side-head match was found.
Hosting (compose.py): plus blocked; heart blocked; check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (human-head-side-profile VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-redrawn after review on SQUARE instead of VRECT_L: v1 construction (head circle r20 on 12-16-20 nodes) kept at full width, neck and jaw shortened; the symbol area grows from 18 to a 22.5-unit square.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '66eefdff-ac9b-4760-951f-816ff21b1e05'
SOURCE_PATH = 'container_icons/svg/human-head-side-profile-66eefdff-ac9b-4760-951f-816ff21b1e05.svg'
AUTHOR = 'claude-opus-5-5'


class HumanHeadSideProfile(Container64):
    icon_id = 'human-head-side-profile'
    keyshape = Keyshape.SQUARE
    category = 'primitives-generate'
    categories = ('container', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('human', 'head', 'side', 'profile', 'mind')

    def build(self) -> None:
        # Cranium on r24 about (30,30) touching the keyshape top and left; the back of the head falls straight
        # (vertical tangent at (6,30)) into a smooth nape, so the skull holds a symbol of 24+ with a 4 px gap.
        self.add_line('rear-neck', (16, 58), (16, 52))
        self.add_bezier('nape', (16, 52), ((16, 47), (6, 41), (6, 30)))
        self.add_arc('crown', (6, 30), (54, 30), radius_x=24)
        self.add_line('forehead-nose', (54, 30), (58, 42))
        self.add_line('nose-base', (58, 42), (52, 42))
        self.add_line('face', (52, 42), (52, 45))
        self.add_arc('chin', (52, 45), (44, 52), radius_x=8)
        self.add_arc('front-neck-turn', (44, 52), (40, 56), radius_x=4, sweep=False)
        self.add_line('front-neck', (40, 56), (40, 58))
        self.add_contour('outline', 'rear-neck', 'nape', 'crown', 'forehead-nose', 'nose-base', 'face', 'chin', 'front-neck-turn', 'front-neck')
