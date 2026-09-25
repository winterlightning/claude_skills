"""police-woman-2: uniform front panels and reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) allows vertical headwear budget.
Face centered x24 with equal circular radii; head bottom 30, shoulders 34,
zero painted gap. Shared human_ref/user.svg supplies curved shoulders;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine hat emblems and facial microdetails omitted for clarity at 48.
Body cue: uniform front panels. Hair and feather asymmetry follow the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-08/references/police-woman-2.svg'
SOURCE_HEAD_ICON_ID = 'police-woman-2'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class PoliceWoman2Avatar(Solo48):
    icon_id = 'police-woman-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('police', 'woman', '2', 'portrait', 'bust')
    def build(self):
        cx = 24
        self.add_polyline('cap', (8, 12), (cx, 4), (40, 12), (34, 20), (14, 20), (8, 12))
        self.add_line('band', (8, 12), (40, 12))
        self.relate('connect', 'cap', 'band')
        self.add_arc('face', (34, 20), (14, 20), radius_x=10, radius_y=10)
        self.relate('connect', 'cap', 'face')
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_bezier('hair-' + side, (cx + sign * 10, 20), ((cx + sign * 16, 20), (cx + sign * 16, 24), (cx + sign * 16, 28)))
            self.relate('connect', 'hair-' + side, 'cap')
            self.relate('connect', 'hair-' + side, 'face')

        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (18, top), (24, top))
        self.add_line('body-top-right', (24, top), (30, top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_line('body-apron-left', (18,top), (18,44))
        self.add_line('body-apron-right', (30,top), (30,44))
        self.relate('connect', 'body-apron-left', 'body-top')
        self.relate('connect', 'body-apron-right', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
