"""A rounded bird with swept crest, paired angry brows and a projecting beak; beak is part of the silhouette rather than a crowded interior hole.
References: Lucide face-angry for brow direction; supplied bird crest and beak identity.
Authored directly on SOLO48; original retained for comparison."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6a537336-3a61-589f-bdab-c6977b97e933'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__angry-bird/20260927T160114Z-thuan-mac-1/reference/angry birds_6a537336-3a61-589f-bdab-c6977b97e933.svg'
AUTHOR = 'gpt-6'

class AngryBird(Solo48):
    icon_id = 'angry-bird'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('angry', 'bird')

    def build(self):
        # Frontal angry bird: a crested round body, paired brows, and a pointed beak.
        self.add_bezier('body',(24,4),
            ((27,7),(32,8),(36,13)),((42,20),(44,30),(38,37)),
            ((32,44),(16,44),(10,37)),((4,30),(6,18),(13,12)),
            ((17,8),(21,8),(24,4)))
        self.add_contour('bird','body',closed=True)
        self.add_polyline('left-brow',(13,19),(21,23))
        self.add_polyline('right-brow',(35,19),(27,23))
        self.add_polyline('beak',(20,32),(24,35),(28,32))
