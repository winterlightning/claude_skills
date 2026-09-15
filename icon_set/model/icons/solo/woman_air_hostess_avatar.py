"""woman-air-hostess: uniform neck scarf with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 26, shoulder top 30, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: uniform neck scarf. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-13/references/woman-air-hostess.svg'
SOURCE_HEAD_ICON_ID = 'woman-air-hostess'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class WomanAirHostessAvatar(Solo48):
    icon_id = 'woman-air-hostess-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('woman', 'air', 'hostess', 'portrait', 'bust')
    def build(self):
        cx = 24
        self.add_polyline('hat', (14, 16), (18, 4), (30, 4), (34, 16), (14, 16))
        self.add_arc('face', (34, 16), (14, 16), radius_x=10, radius_y=10)
        self.relate('connect', 'hat', 'face')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('hair-' + side, (cx + sign * 10, 16), ((cx + sign * 16, 18), (cx + sign * 16, 22), (cx + sign * 16, 26)))
            self.relate('connect', 'hair-' + side, 'hat')
            self.relate('connect', 'hair-' + side, 'face')

        # Broad curved shoulders follow human_ref/user.svg; clothing carries identity.
        # Body plan: fitted uniform with an asymmetric neck scarf.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(12,top),radius_x=4,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (12, top), (24, top))
        self.add_line('body-top-right', (24, top), (36, top))
        self.add_arc('body-right-shoulder',(36,top),(40,42),radius_x=4,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('body-tie', (12, top), (24,44), (36, top))
        self.relate('connect', 'body-tie', 'body-top')
        self.relate('connect', 'body-tie', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
