"""A right-facing head enclosure with a continuous rounded skull and neck.

VRECT_XL: ink (4,0)-(60,64), centerlines (6,2)-(58,62).
Source preserves forehead, projecting nose, jaw and open neck. The rear neck
and skull share an exact 3:4:5 tangent; the face is deliberately asymmetric.
Shared human reference: references/human_ref/full_body_ref.png. An isolated
head has no detached head/body gap. No useful Lucide side-head match was found.
Hosting (compose.py): plus blocked; heart blocked; check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '66eefdff-ac9b-4760-951f-816ff21b1e05'
SOURCE_PATH = 'container_icons/svg/human-head-side-profile-66eefdff-ac9b-4760-951f-816ff21b1e05.svg'
AUTHOR = 'gpt-6'


class HumanHeadSideProfile(Container64):
    icon_id = 'human-head-side-profile'
    keyshape = Keyshape.VRECT_XL
    category = 'primitives-generate'
    aliases = ()
    keywords = ('human', 'head', 'side', 'profile', 'mind')

    def build(self):
        # Plan: one open outline; skull circle (26,22), r20 and rear-neck
        # circle (8,46), r10 meet at (14,38) with parallel 4:3 tangents.
        skull_radius = 20
        rear_join, left, right = (14, 38), (6, 22), (46, 22)
        self.add_line('rear-neck', (18, 62), (18, 46))
        self.add_arc('nape', (18, 46), rear_join, radius_x=10, sweep=False)
        self.add_arc('rear-skull', rear_join, left, radius_x=skull_radius)
        self.add_arc('crown', left, right, radius_x=skull_radius)
        self.add_line('forehead-nose', right, (58, 38))
        self.add_line('nose-base', (58, 38), (50, 38))
        self.add_line('face', (50, 38), (50, 46))
        self.add_arc('chin', (50, 46), (42, 54), radius_x=8)
        self.add_arc('front-neck-turn', (42, 54), (38, 58), radius_x=4, sweep=False)
        self.add_line('front-neck', (38, 58), (38, 62))
        self.add_contour('outline', 'rear-neck', 'nape', 'rear-skull', 'crown',
                         'forehead-nose', 'nose-base', 'face', 'chin',
                         'front-neck-turn', 'front-neck')
