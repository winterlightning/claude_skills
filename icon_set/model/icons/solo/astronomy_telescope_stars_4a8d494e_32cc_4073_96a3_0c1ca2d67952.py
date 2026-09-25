"""Telescope and two stars. SQUARE bounds (4,4)-(44,44). Lucide telescope informs barrel with shared tripod node. Four-ray stars and two visible tripod legs simplify small detail."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '4a8d494e-32cc-4073-96a3-0c1ca2d67952'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/astronomy telescope stars_4a8d494e-32cc-4073-96a3-0c1ca2d67952.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'astronomy-telescope-stars'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Tilted barrel and eyepiece; tripod attaches at a shared lower-barrel endpoint.
        self.add_polyline('barrel',(22,16),(38,10),(42,22),(26,28),(22,16),closed=True)
        self.add_polyline('eyepiece',(22,16),(12,23),(16,32),(26,28))
        self.relate('connect','barrel','eyepiece')
        self.add_polyline('tripod',(14,42),(26,28),(26,42))
        self.relate('connect','barrel','tripod')
        for name,x,y in [('star-left',10,10),('star-right',38,38)]:
            self.add_line(name+'-h',(x-4,y),(x+4,y))
            self.add_line(name+'-v',(x,y-4),(x,y+4))
            self.relate('connect',name+'-h',name+'-v')
