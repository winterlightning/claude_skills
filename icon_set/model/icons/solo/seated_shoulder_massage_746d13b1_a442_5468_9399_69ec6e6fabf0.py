"""Seated Shoulder Massage.

Plan: Two stick figures; heads r4 at (10,10),(30,18), torso starts 8 below head outlines. Shared human full_body_ref.png governs proportions. Therapist arm meets recipient shoulder. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '746d13b1-a442-5468-9399-69ec6e6fabf0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/thai massage_746d13b1-a442-5468-9399-69ec6e6fabf0.svg'
AUTHOR = 'gpt-6'


class SeatedShoulderMassage(Solo48):
    icon_id = 'seated-shoulder-massage'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('seated', 'shoulder', 'massage')

    def build(self):
        for name,x,y in [('therapist',10,10),('recipient',30,18)]:
            self.add_arc(name+'-head-top',(x-4,y),(x+4,y),radius_x=4)
            self.add_arc(name+'-head-bottom',(x+4,y),(x-4,y),radius_x=4)
            self.add_contour(name+'-head',name+'-head-top',name+'-head-bottom',closed=True)
        self.add_line('therapist-torso',(10,22),(10,42))
        self.add_polyline('therapist-arm',(10,22),(20,30),(30,30))
        self.add_line('recipient-torso',(30,30),(30,38))
        self.add_arc('recipient-hip',(30,38),(34,42),radius_x=4,sweep=False)
        self.add_line('recipient-lap',(34,42),(42,42))
        self.add_contour('recipient-body','recipient-torso','recipient-hip','recipient-lap')
        self.relate('connect','therapist-torso','therapist-arm')
        self.relate('connect','therapist-arm','recipient-body')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
        self.mark_human_figure('recipient',head='recipient-head',torso='recipient-torso',torso_junction='start')
