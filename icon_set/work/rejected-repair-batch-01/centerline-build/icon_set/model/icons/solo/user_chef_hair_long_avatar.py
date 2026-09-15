"""user-chef-hair-long: long apron with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 22, shoulder top 26, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: long apron. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-10/references/user-chef-hair-long.svg'
SOURCE_HEAD_ICON_ID = 'user-chef-hair-long'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 22
class UserChefHairLongAvatar(Solo48):
    icon_id = 'user-chef-hair-long-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('user', 'chef', 'hair', 'long', 'portrait', 'bust')
    def build(self):
        cx = 24
        for side, sign in [('left', -1), ('right', 1)]:
            pt = lambda x, y: (cx + sign * x, y)
            self.add_arc('hair-' + side, (cx, 4), pt(16, 14), radius_x=16, radius_y=10, sweep=sign > 0)
            self.add_line('tip-' + side, pt(16, 14), pt(16, 18))
            self.add_contour('outer-' + side, 'hair-' + side, 'tip-' + side)
            self.add_arc('fringe-' + side, (cx, 4), pt(8, 14), radius_x=8, radius_y=10, sweep=sign < 0)
            self.relate('connect', 'outer-' + side, 'fringe-' + side)
        self.relate('connect', 'outer-left', 'outer-right')
        self.relate('connect', 'fringe-left', 'fringe-right')
        self.add_arc('face', (32, 14), (16, 14), radius_x=8, radius_y=8)
        for side in ['left', 'right']:
            self.relate('connect', 'face', 'fringe-' + side)

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(18,top),(24,top))
        self.add_line('body-top-right',(24,top),(30,top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_polyline('body-bib',(18,top),(18,44),(30,44),(30,top))
        self.relate('connect','body-bib','body-top')
        self.relate('connect','body-bib','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
