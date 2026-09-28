"""tribal-woman: rounded garment neckline with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 24, shoulder top 28, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails are omitted for native 48px clarity.
Body cue: rounded garment neckline. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '2ff9b75d-79c3-4a92-b902-1cff6bb77357'
SOURCE_PATH = 'pictographic-primitives/avatars/tribal woman_2ff9b75d-79c3-4a92-b902-1cff6bb77357.svg'
SOURCE_HEAD_ICON_ID = 'tribal-woman'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class TribalWomanAvatar(Solo48):
    icon_id = 'tribal-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('tribal', 'woman', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(16,16),(16,4),(32,4),(32,16),(16,16))
        self.add_arc('face',(32,16),(16,16),radius_x=8)
        self.relate('connect','face','cap')
        for side,sign in [('left',-1),('right',1)]:
            cx=24+sign*12
            self.add_arc('earring-top-'+side,(cx-4,16),(cx+4,16),radius_x=4)
            self.add_arc('earring-bottom-'+side,(cx+4,16),(cx-4,16),radius_x=4)
            self.add_contour('earring-'+side,'earring-top-'+side,'earring-bottom-'+side,closed=True)
            self.relate('connect','earring-'+side,'cap')
            self.relate('connect','earring-'+side,'face')
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
        self.add_arc('body-neckline',(18,top),(30,top),radius_x=6,radius_y=6,sweep=False)
        self.relate('connect','body-neckline','body-top')
        self.relate('connect','body-neckline','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
