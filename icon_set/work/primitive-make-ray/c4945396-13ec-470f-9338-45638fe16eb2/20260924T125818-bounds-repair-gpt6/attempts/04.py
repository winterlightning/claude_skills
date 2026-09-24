"""MediaLive: play triangle, three equal media hexagons, three outward scan marks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c4945396-13ec-470f-9338-45638fe16eb2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon web service elemental medialive_c4945396-13ec-470f-9338-45638fe16eb2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amazon-web-service-elemental-medialive'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.HRECT_L.bounds_for(Profile.SOLO48)
    def build(self):
        # Repeated media-node hexagons around a central play symbol.
        for name,cx,cy in [('top',24,14),('left',10,34),('right',38,34)]:
            self.add_polyline(name,(cx,cy-6),(cx+6,cy-3),(cx+6,cy+3),(cx,cy+6),(cx-6,cy+3),(cx-6,cy-3),closed=True)
        self.add_polyline('play',(19,21),(33,28),(19,35),closed=True)
