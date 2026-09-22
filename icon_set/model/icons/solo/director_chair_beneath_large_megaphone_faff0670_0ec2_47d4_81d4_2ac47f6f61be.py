"""A megaphone sits above and right of a folding director chair. Physical equipment group, no reusable modifier. Square 6..42 supports the upright chair and a steeply flared horn. Source supplies the two equipment objects; Lucide megaphone supplies flared body and attached grip. Separate the objects laterally to preserve the grip and generous chair opening. Omit the far chair post. Crossed legs share a real hinge at14,36; paired supports derive from this point."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'faff0670-0ec2-47d4-81d4-2ac47f6f61be'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/director_faff0670-0ec2-47d4-81d4-2ac47f6f61be.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'director-chair-beneath-large-megaphone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Director Chair Beneath Large Megaphone']
    keywords = ['director', 'chair', 'megaphone', 'film', 'folding', 'seat', 'equipment']
    def build(self):
        self.add_polyline('horn',(30,10),(42,6),(42,22),(30,18),closed=True)
        self.add_line('grip',(30,18),(30,26))
        self.relate('connect','horn','grip')
        self.add_line('seat',(6,24),(22,24))
        self.add_line('chair-back',(6,14),(6,24))
        self.relate('connect','chair-back','seat')
        for x in (6,22):
            self.add_line('upper-leg-'+str(x),(x,24),(14,36))
            self.add_line('lower-leg-'+str(x),(14,36),(x,42))
            self.relate('connect','seat','upper-leg-'+str(x))
        self.relate('connect','chair-back','upper-leg-6')
        self.relate('connect','upper-leg-6','upper-leg-22','lower-leg-6','lower-leg-22')
