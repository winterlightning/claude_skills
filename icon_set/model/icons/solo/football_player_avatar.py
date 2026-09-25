"""football-player: sports jersey V collar beneath the reference hair/headwear.

Plan: SOLO48 VRECT_L ink bounds (6,2)-(42,46); centered circular face x24,
head bottom 24, shoulder top 28, zero visible head/body gap.
Primary reference preserves identifying silhouette; tiny trim/facial marks are
omitted for clear openings. Human reference user.svg supplies rounded shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg inform arcs.
Clothing cue: sports jersey V collar. Hair asymmetry follows the reference, face remains centered.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'f678de75-b4a9-4ef4-b0b6-aa17cdb9100d'
SOURCE_PATH = 'pictographic-primitives/avatars/football player_f678de75-b4a9-4ef4-b0b6-aa17cdb9100d.svg'
SOURCE_HEAD_ICON_ID = 'football-player'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24

class FootballPlayerAvatar(Solo48):
    icon_id = 'football-player-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('football', 'player', 'portrait', 'bust')

    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('crown', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('jaw', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'crown', 'jaw', closed=True)
        self.add_bezier('fringe', (14, 14), ((20, 16), (24, 12), (27, 9)), ((29, 12), (32, 14), (34, 14)))
        self.relate('connect', 'head', 'fringe')

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_polyline('body-collar',(16,top),(24,40),(32,top))
        self.relate('connect','body-collar','body-top')
        self.relate('connect','body-collar','body-top-right')
        self.add_line('body-jacket-opening',(24,40),(24,44))
        self.relate('connect','body-jacket-opening','body-collar')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
