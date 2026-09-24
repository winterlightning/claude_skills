"""Two hands enclosing a heart. SQUARE ink bounds; central heart separated from the enclosing hands. Shared human reference inspected; no detached figure head."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c4776ceb-e74e-4923-a8f4-ac3c1635d4e5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/donation care hands heart 1_c4776ceb-e74e-4923-a8f4-ac3c1635d4e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'donation-care-hands-heart-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Enclosing hand silhouette with a central heart; repeated heart lobes share radius 4.
        self.add_bezier('hands',(24,8),((21,7),(19,6),(16,6)),((12,6),(6,14),(6,20)),((6,24),(6,30),(6,34)))
        self.add_arc('thumb-turn',(6,34),(16,34),radius_x=5,sweep=False)
        
        self.add_line('fingers-2',(16,34),(26,42))
        self.add_line('fingers-3',(26,42),(32,36))
        self.add_bezier('right-hand',(32,36),((36,42),(41,38),(42,32)),((42,28),(42,24),(42,20)),((42,14),(36,6),(32,6)),((29,6),(27,7),(24,8)))
        self.add_contour('hand-outline','hands','thumb-turn','fingers-2','fingers-3','right-hand',closed=True)
        self.add_arc('heart-left',(24,20),(16,20),radius_x=4,sweep=False)
        self.add_bezier('heart-tip',(16,20),((16,23),(20,25),(24,28)),((28,25),(32,23),(32,20)))
        self.add_arc('heart-right',(32,20),(24,20),radius_x=4,sweep=False)
        self.add_contour('heart','heart-left','heart-tip','heart-right',closed=True)
