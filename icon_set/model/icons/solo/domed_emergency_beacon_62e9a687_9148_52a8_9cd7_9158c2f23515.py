"""Emergency Siren Light.

Symbol plan: Dome and wide base with three detached rays; mirrored about x=24. Visible (4,4)-(44,44). Remove internal bulb line.
Construction references: Lucide siren: half-circle dome on pedestal and radial rays.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62e9a687-9148-52a8-9cd7-9158c2f23515'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/police rotating light_62e9a687-9148-52a8-9cd7-9158c2f23515.svg'
AUTHOR = 'gpt-6'


class DomedEmergencyBeacon(Solo48):
    icon_id = 'domed-emergency-beacon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('domed', 'emergency', 'beacon')

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

        path('base',(6,42),[(6,34),(12,34),(36,34),(42,34),(42,42),(6,42)],True)
        path('dome',(12,34),[(12,28),((24,16),12,12,True),((36,28),12,12,True),(36,34)])
        self.relate('connect','dome','base')
        self.add_line('ray-top',(24,6),(24,8))
        for side in (-1,1):
         self.add_line(f'ray-{side}',(24+side*18,10),(24+side*14,12))
