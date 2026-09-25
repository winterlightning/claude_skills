"""Circuit brain with mirrored lobes and descending terminal traces. SQUARE extremes 6,6,42,42. Third trace omitted for legible spacing."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '994c360d-a3ef-411d-83b6-1227713cc09e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/brain circuit_994c360d-a3ef-411d-83b6-1227713cc09e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'brain-circuit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Brain crown has mirrored lobes; two terminal/trace instances use shared spacing.
        self.add_bezier('brain',(9,34),((6,34),(6,31),(6,28)),((6,25),(7,24),(7,22)),((5,17),(8,12),(14,12)),((14,8),(18,6),(20,6)),((22,6),(24,8),(24,8)),((24,8),(26,6),(28,6)),((30,6),(34,8),(34,12)),((40,12),(43,17),(41,22)),((41,24),(42,25),(42,28)),((42,31),(42,34),(39,34)))
        self.add_arc('terminal-left-a',(16,23),(20,23),radius_x=2)
        self.add_arc('terminal-left-b',(20,23),(16,23),radius_x=2)
        self.add_contour('terminal-left','terminal-left-a','terminal-left-b',closed=True)
        self.add_line('trace-left',(18,25),(18,42))
        self.relate('connect','trace-left','terminal-left')
        self.add_arc('terminal-right-a',(28,23),(32,23),radius_x=2)
        self.add_arc('terminal-right-b',(32,23),(28,23),radius_x=2)
        self.add_contour('terminal-right','terminal-right-a','terminal-right-b',closed=True)
        self.add_line('trace-right',(30,25),(30,42))
        self.relate('connect','trace-right','terminal-right')
