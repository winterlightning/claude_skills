"""Make the seated back upright with a horizontal reaching arm, a clear chair seat and leg, bent knee, and a separate upright hooked cane.
Construction plan: Head (14,9), r5; neck (14,22), exact 4 ink gap. Torso, thigh and lower leg form one seated stroke. Cane remains a separate prop. VRECT_L extremes (8,4)-(40,44).
Human construction: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing original and atomic-debug: articulated limbs and shared torso nodes.
Source comparison: The rejected figure leans awkwardly, its arm visually merges into the cane hook, and the detached seat is hard to identify as a chair.
Omissions: fine source outline doubling; preserve the complete action and its identifying prop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1ea697d7-e80d-4a42-b015-acd8cd95ff6c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-person-with-cane/20260929T084652Z-thuan-mac/reference/disability sit cane_1ea697d7-e80d-4a42-b015-acd8cd95ff6c.svg'
AUTHOR = 'gpt-6'
class AuthoredIcon(Solo48):
    icon_id = 'seated-person-with-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/activity'
    aliases = ()
    keywords = ('seated', 'person', 'with', 'cane')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def build(self):

        self.circle('head',14,9,5)
        self.add_line('torso',(14,22),(14,27))
        self.add_arc('hip',(14,27),(18,31),radius_x=4,sweep=False)
        self.add_line('thigh',(18,31),(24,31))
        self.add_arc('knee',(24,31),(28,35),radius_x=4)
        self.add_line('shin',(28,35),(28,44))
        self.add_contour('body','torso','hip','thigh','knee','shin')
        self.add_line('arm',(14,22),(24,22))
        self.add_polyline('chair',(8,44),(8,39),(20,39))
        self.add_arc('cane-hook',(32,25),(40,25),radius_x=4)
        self.add_line('cane-shaft',(40,25),(40,44))
        self.add_contour('cane','cane-hook','cane-shaft')
        self.relate('connect','body','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

