"""red-indian-man: rounded tunic neck and reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) allows vertical headwear budget.
Face centered x24 with equal circular radii; head bottom 28, shoulders 32,
zero painted gap. Shared human_ref/user.svg supplies curved shoulders;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine hat emblems and facial microdetails omitted for clarity at 48.
Body cue: rounded tunic neck. Hair and feather asymmetry follow the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'f115a501-49ed-4291-9f64-42b1086ca5d2'
SOURCE_PATH = 'pictographic-primitives/avatars/red indian man_f115a501-49ed-4291-9f64-42b1086ca5d2.svg'
SOURCE_HEAD_ICON_ID = 'red-indian-man'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 28
class RedIndianManAvatar(Solo48):
    icon_id = 'red-indian-man-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('red', 'indian', 'man', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(16,20),(32,20),radius_x=8)
        self.add_arc('face',(32,20),(16,20),radius_x=8)
        self.add_contour('head','crown','face',closed=True)
        self.add_line('headband',(16,20),(32,20))
        self.relate('connect','head','headband')
        self.add_bezier('feather-left',(32,20),((28,8),(36,4),(40,4)))
        self.add_bezier('feather-right',(40,4),((40,12),(40,16),(32,20)))
        self.add_contour('feather','feather-left','feather-right',closed=True)
        self.relate('connect','feather','head')
        self.relate('connect','feather','headband')
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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
