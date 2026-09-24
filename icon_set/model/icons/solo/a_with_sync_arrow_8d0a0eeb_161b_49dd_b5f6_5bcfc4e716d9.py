from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9'
SOURCE_PATH = 'icon_set/work/todo-references/a with sync arrow_8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9.svg'
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
        self.add_polyline('upper-tip',(34,16),(42,20),(42,12))
        self.relate('connect','upper-orbit','upper-tip')
        self.add_arc('lower-orbit',(42,28),(6,28),radius_x=18,radius_y=14)
        self.add_polyline('lower-tip',(14,32),(6,28),(6,36))
        self.relate('connect','lower-orbit','lower-tip')
        self.add_polyline('letter-a',(16,32),(20,24),(24,16),(28,24),(32,32))
        self.add_line('a-bar',(20,24),(28,24))
        self.relate('connect','letter-a','a-bar')
