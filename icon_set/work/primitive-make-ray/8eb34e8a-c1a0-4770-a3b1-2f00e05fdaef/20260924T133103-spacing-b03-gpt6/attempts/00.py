"""Passover plate, five-point star and foreground matzo. SQUARE centerline6,6,42,42. Plate radius15 centered21,21; hidden behind tile. Star and tile share the star lower-right endpoint26,25. One tile row replaces the dense series."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pesach passover 2_8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pesach-passover-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('plate',(12,33),(33,12),radius_x=15,large_arc=True)
        self.add_polyline('star',(21,15),(24,18),(27,19),(25,22),(26,25),(21,24),(17,26),(18,22),(15,19),(18,18),closed=True)
        self.add_polyline('tile',(26,25),(42,25),(42,33),(42,42),(26,42),(26,33),closed=True)
        self.add_line('row',(26,33),(42,33))
        self.relate('connect','row','tile')
        self.relate('connect','star','tile')
