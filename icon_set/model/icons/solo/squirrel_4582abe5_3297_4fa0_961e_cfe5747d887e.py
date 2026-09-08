"""Seated right-facing squirrel with a large curled tail. Bounds (2,2)-(46,46). Lucide squirrel: connected round haunch and high tail; omit eye and ground extension for spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4582abe5-3297-4fa0-961e-cfe5747d887e'
SOURCE_PATH = 'pictographic-primitives/animals/squirrel_4582abe5-3297-4fa0-961e-cfe5747d887e.svg'
AUTHOR = 'gpt-6'


class Squirrel(Solo48):
    icon_id = 'squirrel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('squirrel', 'tail', 'bushy', 'rodent', 'nut', 'tree', 'animal', 'wildlife')

    def build(self) -> None:
        self.add_arc('tail-top',(2,14),(14,2),radius_x=12,sweep=True)
        self.add_arc('tail-turn',(14,2),(26,14),radius_x=12,sweep=True)
        self.add_arc('tail-return',(26,14),(20,28),radius_x=20,sweep=True)
        self.add_arc('tail-body',(20,28),(24,46),radius_x=20,sweep=False)
        self.add_line('base',(24,46),(36,46))
        self.add_arc('haunch',(36,46),(46,36),radius_x=10,sweep=False)
        self.add_arc('haunch-top',(46,36),(36,26),radius_x=10,sweep=False)
        self.add_arc('haunch-inner',(36,26),(28,30),radius_x=10,sweep=False)
        self.add_contour('tail-to-haunch','tail-top','tail-turn','tail-return','tail-body','base','haunch','haunch-top','haunch-inner')
        self.add_arc('tail-left',(2,14),(8,24),radius_x=12,sweep=False)
        self.add_arc('back',(8,24),(2,34),radius_x=12,sweep=False)
        self.add_arc('rump',(2,34),(14,46),radius_x=12,sweep=False)
        self.add_line('rear-base',(14,46),(24,46))
        self.add_contour('back-outline','tail-left','back','rump','rear-base')
        self.relate('connect','tail-to-haunch','back-outline')
        self.add_polyline('neck',(20,28),(30,18),(30,8))
        self.add_arc('ear',(30,8),(38,8),radius_x=4,radius_y=6,sweep=True)
        self.add_line('head-top',(38,8),(46,10))
        self.add_arc('muzzle',(46,10),(40,20),radius_x=6,radius_y=10,sweep=True)
        self.add_line('chest',(40,20),(36,26))
        self.add_contour('head','ear','head-top','muzzle','chest')
        self.relate('connect','neck','head')
        self.relate('connect','head','tail-to-haunch')
        self.relate('connect','neck','tail-to-haunch')
