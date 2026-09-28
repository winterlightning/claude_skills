"""Tooth with Brace Bracket.

Plan: Mirrored molar owns a rectangular bracket and wire at y22. Remove tiny ticks and interrupt wire through bracket to preserve its opening. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd72327b-af72-492c-b3df-5ebc0cb31774'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/dental brace_dd72327b-af72-492c-b3df-5ebc0cb31774.svg'
AUTHOR = 'gpt-6'


class ToothWithBraceBracket(Solo48):
    icon_id = 'tooth-with-brace-bracket'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('tooth', 'with', 'brace', 'bracket')

    def build(self):
        # A mirrored molar: broad crown, two round roots, shallow central cleft.
        self.add_arc('crown-left',(8,12),(16,4),radius_x=8)
        self.add_arc('cusp-left',(16,4),(24,8),radius_x=8,radius_y=4,sweep=False)
        self.add_arc('cusp-right',(24,8),(32,4),radius_x=8,radius_y=4,sweep=False)
        self.add_arc('crown-right',(32,4),(40,12),radius_x=8)
        self.add_line('wall-r1',(40,12),(40,22))
        self.add_line('wall-r2',(40,22),(40,28))
        self.add_arc('root-right-outer',(40,28),(36,40),radius_x=4,radius_y=12)
        self.add_arc('root-right-bottom',(36,40),(28,40),radius_x=4)
        self.add_arc('cleft-right',(28,40),(24,36),radius_x=4,sweep=False)
        self.add_arc('cleft-left',(24,36),(20,40),radius_x=4,sweep=False)
        self.add_arc('root-left-bottom',(20,40),(12,40),radius_x=4)
        self.add_arc('root-left-outer',(12,40),(8,28),radius_x=4,radius_y=12)
        self.add_line('wall-l2',(8,28),(8,22))
        self.add_line('wall-l1',(8,22),(8,12))
        self.add_contour('tooth','crown-left','cusp-left','cusp-right','crown-right','wall-r1','wall-r2','root-right-outer','root-right-bottom','cleft-right','cleft-left','root-left-bottom','root-left-outer','wall-l2','wall-l1',closed=True)

        self.add_polyline('bracket',(19,22),(19,18),(29,18),(29,22),(29,26),(19,26),closed=True)
        self.add_line('wire-left',(8,22),(19,22))
        self.add_line('wire-right',(29,22),(40,22))
        for wire in ['wire-left','wire-right']:
            self.relate('connect',wire,'tooth')
            self.relate('connect',wire,'bracket')
