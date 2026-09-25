"""Reply Speech Bubble Frame.

Plan: Centerline extremes (6,6)-(42,42); SQUARE keyshape supports the complete standalone source silhouette.
Construction: Lucide message-circle-reply: an integrated reply cue. Source owns the rounded rectangular bubble, interrupted top border and bottom-left tail.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '366551e0-8571-45b2-a1da-38d28f6b5b98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/message bubble arrow 1_366551e0-8571-45b2-a1da-38d28f6b5b98.svg'
AUTHOR = "gpt-6"

class Batch04Icon11(Solo48):
    icon_id = 'reply-speech-bubble-frame-366551e0'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('reply-speech-bubble-frame',)
    keywords = ('reply', 'speech', 'bubble', 'frame')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for i, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{i}"
                if kind == "L": self.add_line(member, here, end)
                elif kind == "A": self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == "C": self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, radius):
            path(name,(cx,cy-radius),[("A",(cx+radius,cy),radius,radius,True),("A",(cx,cy+radius),radius,radius,True),("A",(cx-radius,cy),radius,radius,True),("A",(cx,cy-radius),radius,radius,True)],True)
        path("bubble",(22,10),[("L",(38,10)),("A",(42,14),4,4,True),("L",(42,30)),("A",(38,34),4,4,True),("L",(24,34)),("L",(14,42)),("L",(14,34)),("L",(10,34)),("A",(6,30),4,4,True),("L",(6,14)),("A",(10,10),4,4,True),("L",(12,10))])
        self.add_polyline("arrow",(26,6),(22,10),(26,14));self.relate("connect","bubble","arrow")
