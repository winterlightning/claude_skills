'Standing owl: retain pointed head tufts, a rounded upright side and a compact beak below clear eye dots.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09901c1f-7237-596c-94c4-12d2991e2fed'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird owl body_09901c1f-7237-596c-94c4-12d2991e2fed.svg'
AUTHOR = 'gpt-6'


class StandingOwl(Solo48):
    icon_id = 'standing-owl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('owl', 'standing', 'wise', 'bird', 'night', 'feathers', 'nocturnal', 'perch')

    def build(self) -> None:
        self.add_polyline('tufts',(6,6),(17,10),(25,8),(34,10),(42,6),(38,20))
        self.add_bezier('side',(38,20),((43,25),(41,34),(33,38)),((29,40),(27,42),(24,42)))
        self.add_line('base',(24,42),(6,42))
        self.add_bezier('back',(6,42),((6,31),(9,24),(11,20)))
        self.add_line('left-tuft',(11,20),(6,6))
        for a,b in (('tufts','side'),('side','base'),('base','back'),('back','left-tuft'),('left-tuft','tufts')):self.relate('connect',a,b)
        self.add_dot('eye-left',(20,20));self.add_dot('eye-right',(29,20))
        self.add_polyline('beak',(23,28),(26,31),(28,28))
