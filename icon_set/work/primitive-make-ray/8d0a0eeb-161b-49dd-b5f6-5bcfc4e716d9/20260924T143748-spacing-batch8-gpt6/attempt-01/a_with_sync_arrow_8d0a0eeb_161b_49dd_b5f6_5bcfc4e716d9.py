from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9'
SOURCE_PATH = 'pictographic-primitives/other/a with sync arrow_8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'a-with-sync-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('a with sync arrow',)

    def build(self):
        # Opposed half-ellipse arrows, rotated by 180 degrees; centered capital A.
        self.add_arc('upper-orbit',(6,20),(42,20),radius_x=18,radius_y=14)
        self.add_polyline('upper-tip',(39,20),(42,20),(42,17))
        self.relate('connect','upper-orbit','upper-tip')
        self.add_arc('lower-orbit',(42,28),(6,28),radius_x=18,radius_y=14)
        self.add_polyline('lower-tip',(9,28),(6,28),(6,31))
        self.relate('connect','lower-orbit','lower-tip')
        self.add_polyline('letter-a',(16,32),(18,28),(24,16),(30,28),(32,32))
        self.add_line('a-bar',(18,28),(30,28))
        self.relate('connect','letter-a','a-bar')
