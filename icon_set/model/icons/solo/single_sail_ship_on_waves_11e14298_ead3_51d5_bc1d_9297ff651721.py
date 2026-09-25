"""Sailing Ship on Waves.

Symbol plan: Single curved rectangular sail and raised hull ends, wave-interrupted lower edge. Extremes6,6,42,42. Remove second water row; central mast shares endpoints.
Construction references: Lucide sailboat: rounded hull and mast; source curved sail and water occlusion.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11e14298-ead3-51d5-bc1d-9297ff651721'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy ship_11e14298-ead3-51d5-bc1d-9297ff651721.svg'
AUTHOR = 'gpt-6'


class SingleSailShipOnWaves(Solo48):
    icon_id = 'single-sail-ship-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('single', 'sail', 'ship', 'on', 'waves')

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

        self.add_bezier('sail-left',(12,6),((16,12),(16,16),(12,22)))
        self.add_bezier('sail-right',(36,22),((32,16),(32,12),(36,6)))
        self.add_line('sail-top',(36,6),(12,6))
        path('sail-bottom',(12,22),[(24,22),(36,22)])
        for a,b in [('sail-left','sail-top'),('sail-left','sail-bottom'),('sail-right','sail-top'),('sail-right','sail-bottom')]:self.relate('connect',a,b)
        self.add_line('mast',(24,22),(24,30))
        path('hull',(6,30),[(24,30),(42,30),(38,42)])
        self.add_line('stern',(6,30),(10,42))
        self.add_bezier('wave-left-cap',(6,40),((8,42),(8,42),(10,42)))
        self.add_bezier('wave-left',(10,42),((12,42),(14,40),(16,38)))
        self.relate('connect','wave-left-cap','wave-left')
        self.relate('connect','stern','wave-left-cap')
        self.relate('connect','stern','wave-left')
        self.add_bezier('wave-center',(16,38),((20,42),(28,42),(32,38)))
        self.add_bezier('wave-right',(32,38),((34,40),(36,42),(38,42)))
        self.add_bezier('wave-right-cap',(38,42),((40,42),(40,42),(42,40)))
        self.relate('connect','wave-right','wave-right-cap')
        self.relate('connect','hull','wave-right')
        self.relate('connect','hull','wave-right-cap')
        self.relate('connect','mast','sail-bottom');self.relate('connect','mast','hull');self.relate('connect','hull','stern')
        self.relate('connect','wave-left','wave-center');self.relate('connect','wave-center','wave-right')
