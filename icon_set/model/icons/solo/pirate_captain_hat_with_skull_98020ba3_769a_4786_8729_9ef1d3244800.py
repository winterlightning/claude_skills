"""Pirate Captain Hat with Skull.

Symbol plan: Mirror crown about24; continuous upturned brim and skull silhouette. Extremes4,8,44,40. Drop eye dots and bone strokes below spacing budget.
Construction references: Lucide skull: rounded cranium and stepped lower jaw, reduced to silhouette.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98020ba3-769a-4786-8729-9ef1d3244800'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy captain hat_98020ba3-769a-4786-8729-9ef1d3244800.svg'
AUTHOR = 'gpt-6'


class PirateCaptainHatWithSkull(Solo48):
    icon_id = 'pirate-captain-hat-with-skull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('pirate', 'captain', 'hat', 'with', 'skull')

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

        self.add_arc('dome',(8,24),(40,24),radius_x=16)
        path('left',(8,24),[(4,30),(4,34),((10,40),6,6,False),(38,40),((44,34),6,6,False),(44,30),(40,24)])
        self.relate('connect','dome','left')
        path('skull',(18,24),[((30,24),6,6,True),(28,26),(28,30),(20,30),(20,26),(18,24)],True)
