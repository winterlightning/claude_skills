"""Man with a bow tie, circular face and broad open-bottom avatar shoulders.
Symbol plan: mirror the shoulder ellipse and tie about x=24; the circular
head touches the shoulder ink. VRECT_L extremes: (8,4)-(40,44).
References: human_ref/user.svg and Lucide user-round circular bust construction.
The user permits an exception for the compact bow-tie area.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '991b8ae3-461f-513b-aacf-3e86a2bc7b73'
SOURCE_PATH = 'pictographic-primitives/avatars/man_991b8ae3-461f-513b-aacf-3e86a2bc7b73.svg'
SOURCE_CATEGORY = 'avatars'
AUTHOR = 'gpt-6'


class BatchSolo(Solo48):
    icon_id = 'man-wearing-bow-tie'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'wearing', 'bow', 'tie')

    exception = {'reason': 'User approved an exception for the bow-tie area: compact triangular openings and bow-to-shoulder clearance. Circular head, touching head/body ink, curved open-bottom shoulders, 48x48 canvas and stroke 4 remain standard.', 'approved_by': 'user', 'svg_sha256': '8cf5a6db3285534de62822a9a372ea1267023453824eafd759ed50e923c8a763'}

    def build(self):
        cx, cy, radius = 24, 13, 9
        self.add_arc('crown', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('jaw', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'crown', 'jaw', closed=True)
        top = cy + radius + HEAD_BODY_CENTERLINE_GAP
        self.add_line('left-side', (8,44), (8,38))
        self.add_arc('left-shoulder', (8,38), (cx,top), radius_x=16, radius_y=38-top)
        self.add_arc('right-shoulder', (cx,top), (40,38), radius_x=16, radius_y=38-top)
        self.add_line('right-side', (40,38), (40,44))
        self.add_contour('body', 'left-side', 'left-shoulder', 'right-shoulder', 'right-side')
        self.relate('connect', 'head', 'body')
        self.add_polyline('bow-left', (16,34), (cx,38), (16,42), closed=True)
        self.add_polyline('bow-right', (32,34), (32,42), (cx,38), closed=True)
        self.relate('connect', 'bow-left', 'bow-right')
