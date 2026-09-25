"""Athlete holding a javelin overhead, with a wide throwing stance.

VRECT_L reaches (8,4)-(40,44). Human full_body_ref supplies the circular
head and simple limbs; Lucide orbit supplies closed circle construction.
The source supplies the raised throwing arm, spear and opposing arm.
Head centre (24,16), r4; neck (24,28): exactly 4 ink clearance.
The torso owns the shoulder/hip nodes. Outline anatomy is reduced to strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed2e2f29-f220-45d7-a61a-49096d243eef'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/athletics javelin throwing_ed2e2f29-f220-45d7-a61a-49096d243eef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'javelin-thrower-with-raised-arm'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Athlete Throwing Javelin',)
    keywords = ('javelin', 'athlete', 'throwing', 'spear', 'sport', 'person', 'stance')

    def build(self):
        shoulder, hip, hand = (24,28), (24,36), (16,4)
        self.add_arc('head-top',(20,16),(28,16),radius_x=4)
        self.add_arc('head-bottom',(28,16),(20,16),radius_x=4)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_polyline('javelin',(8,4),hand,(40,4))
        self.add_line('raised-forearm-1',hand,(8,20))
        self.add_line('raised-forearm-2',(8,20),(8,24))
        self.add_arc('elbow',(8,24),(12,28),radius_x=4,sweep=False)
        self.add_line('upper-arm',(12,28),shoulder)
        self.add_contour('raised-arm','raised-forearm-1','raised-forearm-2','elbow')
        self.relate('connect','raised-arm','upper-arm')
        self.add_line('forward-arm',shoulder,(40,28))
        self.add_line('torso',shoulder,hip)
        self.add_polyline('legs',(12,44),hip,(36,44))
        self.relate('connect','javelin','raised-arm')
        self.relate('connect','upper-arm','torso','forward-arm')
        self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
