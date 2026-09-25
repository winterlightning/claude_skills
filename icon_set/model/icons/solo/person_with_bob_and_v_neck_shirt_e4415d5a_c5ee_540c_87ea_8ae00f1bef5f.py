'Lowered the shoulder top from31 to35 and restored a parted fringe. Longer bob sides reach28, leaving clear room above the lower shoulders. Circular jaw radius7 at (24,24) ends31; shoulder top35 gives zero visible gap. VRECT_L retains the upright silhouette. V-neck omitted to keep the shorter torso open.'
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'e4415d5a-c5ee-540c-87ea-8ae00f1bef5f'
SOURCE_PATH = 'pictographic-primitives/avatars/woman_e4415d5a-c5ee-540c-87ea-8ae00f1bef5f.svg'
AUTHOR = 'gpt-6'

class PersonWithBobAndVNeckShirt(Solo48):
    icon_id='person-with-bob-and-v-neck-shirt'
    keyshape=Keyshape.VRECT_L
    category = 'avatars'
    categories = ('primitives', 'avatars')
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('woman','bob','portrait')
    def build(self):
        # Circular face within the bob; broad smooth open-bottom avatar bust.
        self.add_bezier('fringe-left',(17,24),((20,23),(22,20),(24,16)))
        self.add_bezier('fringe-right',(24,16),((26,20),(28,23),(31,24)))
        self.add_arc('jaw',(31,24),(17,24),radius_x=7)
        self.add_contour('head','fringe-left','fringe-right','jaw',closed=True)
        self.add_line('hair-left',(8,28),(8,20))
        self.add_arc('hair-crown-left',(8,20),(24,4),radius_x=16)
        self.add_arc('hair-crown-right',(24,4),(40,20),radius_x=16)
        self.add_line('hair-right',(40,20),(40,28))
        self.add_contour('hair','hair-left','hair-crown-left','hair-crown-right','hair-right')
        top=24+7+HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,43))
        self.add_arc('body-left-shoulder',(8,43),(24,top),radius_x=16,radius_y=8)
        self.add_arc('body-right-shoulder',(24,top),(40,43),radius_x=16,radius_y=8)
        self.add_line('body-right-side',(40,43),(40,44))
        self.add_contour('body','body-left-side','body-left-shoulder','body-right-shoulder','body-right-side')
        self.relate('connect','head','body')
