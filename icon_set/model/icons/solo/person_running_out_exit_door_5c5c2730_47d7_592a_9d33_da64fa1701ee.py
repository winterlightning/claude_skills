"""A running figure leaves an open doorway toward the left.

Construction: person-standing: circular head and coherent limb strokes, reposed for running.
Reduction: Outlined body reduced to stick limbs; doorway retained as the scene context. Deliberately asymmetric motion.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c5c2730-47d7-592a-9d33-da64fa1701ee'
SOURCE_PATH = 'pictographic-primitives/travel/evacuation center_5c5c2730-47d7-592a-9d33-da64fa1701ee.svg'
AUTHOR = 'gpt-6'


class PersonRunningOutExitDoor(Solo48):
    icon_id = 'person-running-out-exit-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    aliases = ()
    keywords = ('exit', 'evacuation', 'emergency', 'running', 'person', 'door', 'escape', 'safety')

    def build(self) -> None:
        # SQUARE extremes (6,6)-(42,42); head, torso and limbs form one runner.
        self.add_polyline('door',(30,6),(42,6),(42,42),(34,42))
        self.add_arc('head-right',(20,9),(20,15),radius_x=3)
        self.add_arc('head-left',(20,15),(20,9),radius_x=3)
        self.add_contour('head','head-right','head-left',closed=True)
        self.add_polyline('arms',(6,27),(12,21),(20,24),(27,29),(33,29))
        self.add_line('torso',(20,24),(16,32))
        self.add_polyline('front-leg',(16,32),(11,40),(6,40))
        self.add_line('back-leg',(16,32),(25,42))
        for a,b in [('arms','torso'),('torso','front-leg'),('torso','back-leg'),('front-leg','back-leg')]:
         self.relate('connect',a,b)
