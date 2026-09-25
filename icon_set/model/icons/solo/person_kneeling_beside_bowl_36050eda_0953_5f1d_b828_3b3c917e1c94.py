"""Person Vomiting into Bowl.
Plan: A forward-bent kneeling figure reaches to a bowl on the left. Head center (14,12), r=4; neck (26,12), exact horizontal 8 centerline / 4 ink gap. Extrema (4,8)-(44,40).
Reference: human_ref/full_body_ref.png: bent/kneeling torso, circular head and round-ended limbs.
Reduction: Outlined thick limbs reduced to coherent stick-figure strokes; no vomiting stream added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36050eda-0953-5f1d-b828-3b3c917e1c94'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/party throw up_36050eda-0953-5f1d-b828-3b3c917e1c94.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'person-kneeling-beside-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('person', 'vomiting', 'into', 'bowl')

    def build(self):

        self.add_arc('head-a',(10,12),(18,12),radius_x=4)
        self.add_arc('head-b',(18,12),(10,12),radius_x=4)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_line('torso',(26,12),(32,12))
        self.add_arc('back-round',(32,12),(36,16),radius_x=4)
        self.add_line('hip',(36,16),(36,28))
        self.add_polyline('leg',(36,28),(30,40),(44,40))
        for a,b in (('torso','back-round'),('back-round','hip'),('hip','leg')):self.relate('connect',a,b)
        self.add_polyline('arm',(26,12),(26,30),(16,30))
        self.relate('connect','arm','torso')
        self.add_line('rim',(4,30),(16,30))
        self.add_arc('bowl',(16,30),(4,30),radius_x=6,radius_y=10)
        self.relate('connect','bowl','rim')
        self.relate('connect','arm','rim')
        self.relate('connect','arm','bowl')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
