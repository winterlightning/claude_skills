"""Shoemaker bust with apron and foreground shoe. SQUARE centerlines6,6,42,42; head bottom18 and shoulder apex26. Shared apron and shoe nodes represent actual joined strokes; asymmetry follows source."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4a1b8b06-db68-40b2-adfe-7ecac75aaa72'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/shoemaker_4a1b8b06-db68-40b2-adfe-7ecac75aaa72.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shoemaker'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('head-a',(14,12),(26,12),radius_x=6)
        self.add_arc('head-b',(26,12),(14,12),radius_x=6)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_bezier('shoulder-left',(6,38),((6,31),(9,28),(14,27)),((16,26),(18,26),(20,26)))
        self.add_line('side',(6,42),(6,38))
        self.add_bezier('shoulder-right',(20,26),((27,26),(30,28),(32,30)))
        self.add_contour('body','side','shoulder-left','shoulder-right')
        self.add_polyline('apron',(14,27),(14,34),(12,42),(6,42))
        self.relate('connect','body','apron')
        self.add_bezier('shoe-top',(24,32),((28,36),(30,35),(32,30)),((36,34),(42,33),(42,42)))
        self.add_polyline('sole',(42,42),(24,42),(24,34),(24,32))
        self.add_contour('shoe','shoe-top','sole-1','sole-2','sole-3',closed=True)
        self.relate('connect','body','shoe')
        self.add_line('bib',(14,34),(24,34))
        self.relate('connect','bib','apron')
        self.relate('connect','bib','shoe')
