"""man-chef-1: apron with reference hair/headwear.
Plan: SOLO48 VRECT_L, ink (6,2)-(42,46); circular face x24,
head bottom 26, shoulders 30, zero painted gap. Shared human_ref/user.svg
supplies curved shoulders; Lucide user-round original and atomic-debug guide
cardinal arcs. Fine trim omitted at 48. Body cue: apron.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'ca89dca0-33b3-5008-a98d-0d8d4c49fa5a'
SOURCE_PATH = 'pictographic-primitives/avatars/man chef_ca89dca0-33b3-5008-a98d-0d8d4c49fa5a.svg'
SOURCE_HEAD_ICON_ID = 'man-chef-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class ManChef1Avatar(Solo48):
    icon_id = 'man-chef-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'chef', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('puff-left',(14,16),(14,8),radius_x=4)
        self.add_line('hat-left',(14,8),(20,8))
        self.add_arc('puff-top',(20,8),(28,8),radius_x=4)
        self.add_line('hat-right',(28,8),(34,8))
        self.add_arc('puff-right',(34,8),(34,16),radius_x=4)
        self.add_line('hat-base',(34,16),(14,16))
        self.add_contour('hat','puff-left','hat-left','puff-top','hat-right','puff-right','hat-base',closed=True)
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','face','hat')
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
