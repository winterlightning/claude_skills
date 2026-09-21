"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0eaa90e-ee21-4ae5-bede-0c17096fa38f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baby newborn_e0eaa90e-ee21-4ae5-bede-0c17096fa38f.svg'
AUTHOR = 'gpt-6'


class IndependentSolo(Solo48):
    icon_id = 'hooded-swaddle-with-crossed-blanket-folds-v3'
    variant_of = 'hooded-swaddle-with-crossed-blanket-folds'
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('hooded', 'swaddle', 'with', 'crossed', 'blanket', 'folds')

    def build(self):
        # Plan: hood capsule, circular face opening, and two intersecting blanket seams.
        # VRECT_L extremes (8,4)-(40,44); shared human circular-head vocabulary.
        self.add_arc('hood', (8,20),(40,20),radius_x=16)
        self.add_line('right-upper',(40,20),(40,28))
        self.add_line('right-lower',(40,28),(40,36))
        self.add_arc('foot-right',(40,36),(32,44),radius_x=8)
        self.add_line('foot',(32,44),(16,44))
        self.add_arc('foot-left',(16,44),(8,36),radius_x=8)
        self.add_line('left-lower',(8,36),(8,32))
        self.add_line('left-upper',(8,32),(8,20))
        self.add_contour('blanket','hood','right-upper','right-lower','foot-right','foot','foot-left','left-lower','left-upper',closed=True)
        self.add_arc('face-top',(18,19),(30,19),radius_x=6)
        self.add_arc('face-bottom',(30,19),(18,19),radius_x=6)
        self.add_contour('face','face-top','face-bottom',closed=True)
        self.add_polyline('fold-main',(8,32),(24,34),(40,36))
        self.add_line('fold-upper',(40,28),(24,34))
        self.relate('connect','fold-main','blanket')
        self.relate('connect','fold-upper','blanket')
        self.relate('connect','fold-upper','fold-main')
