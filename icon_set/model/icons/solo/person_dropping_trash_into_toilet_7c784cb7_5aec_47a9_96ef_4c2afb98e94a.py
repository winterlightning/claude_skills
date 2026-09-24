"""Person reaching over a toilet with trash above it; SQUARE extremes (6,6)-(42,42). Human reference full_body_ref.png governs detached head and stick limbs."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '7c784cb7-5aec-47a9-96ef-4c2afb98e94a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/do not throw trash toilet_7c784cb7-5aec-47a9-96ef-4c2afb98e94a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-dropping-trash-into-toilet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('head-a',(32,10),(40,10),radius_x=4)
        self.add_arc('head-b',(40,10),(32,10),radius_x=4)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_arc('trash-a',(8,10),(16,10),radius_x=4)
        self.add_arc('trash-b',(16,10),(8,10),radius_x=4)
        self.add_contour('trash','trash-a','trash-b',closed=True)
        # Human full_body_ref: head radius 4; bottom y14 to torso start y22 = 8 centerline / 4 ink.
        self.add_line('torso',(36,22),(36,32))
        self.add_polyline('legs',(30,42),(36,32),(42,42))
        self.add_polyline('arm',(36,22),(28,23),(24,23))
        self.relate('connect','torso','legs')
        self.relate('connect','torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('tank',(6,42),(6,22),(14,22),(14,32),(24,32))
        self.add_arc('bowl',(24,32),(16,40),radius_x=8)
        self.add_line('pedestal',(16,40),(16,42))
        self.relate('connect','tank','bowl')
        self.relate('connect','bowl','pedestal')
