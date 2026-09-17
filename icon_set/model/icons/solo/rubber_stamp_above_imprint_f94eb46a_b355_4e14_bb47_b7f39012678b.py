"""Rubber Stamp Marking Paper.

Symbol plan: Centered rounded knob, narrow handle, wide stamp base above single imprint. Extremes8,4,40,44. Omit perspective paper perimeter and small dash so imprint remains clear.
Construction references: Lucide stamp: round knob narrowing into stem and broad base; keep detached impression.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f94eb46a-b355-4e14-bb47-b7f39012678b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/seal forfeit_f94eb46a-b355-4e14-bb47-b7f39012678b.svg'
AUTHOR = 'gpt-6'


class RubberStampAboveImprint(Solo48):
    icon_id = 'rubber-stamp-above-imprint'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('rubber', 'stamp', 'above', 'imprint')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        self.add_arc('knob-top',(18,10),(30,10),radius_x=6)
        self.add_bezier('handle-right',(30,10),((30,15),(28,14),(28,20)))
        path('base',(28,20),[(36,20),((40,24),4,4,True),(40,28),(8,28),(8,24),((12,20),4,4,True),(20,20)])
        self.add_bezier('handle-left',(20,20),((20,14),(18,15),(18,10)))
        self.add_contour('handle','handle-left','knob-top','handle-right')
        self.relate('connect','handle','base')
        path('imprint',(18,40),[((30,40),6,4,True),((18,40),6,4,True)],True)
