"""Ear with sound wave. SQUARE (6,6)-(42,42); one wave omitted to preserve the outer helix and inner fold. Lucide ear informs crown-to-lobe flow."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '4317946e-a563-47b7-9c3d-e830b878ecc6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/ear listen_4317946e-a563-47b7-9c3d-e830b878ecc6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ear-with-sound-waves-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Crown extrema are axial endpoints; lower lobe and fold use coherent curves.
        self.add_arc('crown',(6,19),(32,19),radius_x=13)
        self.add_bezier('back',(32,19),((32,27),(24,29),(24,34)))
        self.add_arc('lobe',(24,34),(8,34),radius_x=8)
        self.add_contour('ear','crown','back','lobe')
        self.add_arc('fold-top',(23,20),(15,20),radius_x=4,sweep=False)
        self.add_arc('fold-bottom',(15,20),(15,28),radius_x=4,sweep=True)
        self.add_contour('fold','fold-top','fold-bottom')
        self.add_arc('wave',(40,14),(40,34),radius_x=2,radius_y=10,sweep=True)
