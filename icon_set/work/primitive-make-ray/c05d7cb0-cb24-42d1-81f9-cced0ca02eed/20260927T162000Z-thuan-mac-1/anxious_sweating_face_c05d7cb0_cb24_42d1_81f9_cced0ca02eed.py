'Anxious Face with Sweat Drop.\nPlan: Worried eyes, downturned mouth and a round sweat bead with a short upper tip.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Brows and eyes combined. Droplet body made round with a short tip for a readable small sweat bead.\nKeyshape: CIRCLE; use exact SOLO48 centerline extremes from the contract.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c05d7cb0-cb24-42d1-81f9-cced0ca02eed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__anxious-sweating-face/20260927T160114Z-thuan-mac-1/reference/face anxious sweat_c05d7cb0-cb24-42d1-81f9-cced0ca02eed.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'anxious-sweating-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('anxious', 'sweating', 'face')

    def build(self):
        # The brows and open eyes distinguish worry; the teardrop sits on one cheek.
        self.add_arc('face-a',(4,24),(44,24),radius_x=20)
        self.add_arc('face-b',(44,24),(4,24),radius_x=20)
        self.add_contour('face','face-a','face-b',closed=True)
        self.add_bezier('brow-left',(12,15),((15,15),(17,13),(18,11)))
        self.add_bezier('brow-right',(30,11),((31,13),(33,15),(36,15)))
        for name,x in [('left-eye',17),('right-eye',31)]:
            self.add_arc(name+'-a',(x-2,23),(x+2,23),radius_x=2)
            self.add_arc(name+'-b',(x+2,23),(x-2,23),radius_x=2)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        self.add_arc('frown',(16,36),(28,36),radius_x=8,radius_y=4,sweep=False)
        self.add_bezier('sweat',(35,29),((37,32),(38,33),(35,35)),((32,35),(32,32),(35,29)))
        self.add_contour('drop','sweat',closed=True)
