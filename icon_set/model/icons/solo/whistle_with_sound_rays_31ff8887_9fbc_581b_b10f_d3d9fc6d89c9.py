"""Referee Whistle with Sound Waves.

Symbol plan: Round chamber with small circular hole and right mouthpiece, three detached sound rays. Extremes6,6,42,42. Asymmetric sound direction retained.
Construction references: No useful direct Lucide match; coherent geometric contours.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31ff8887-9fbc-581b-b10f-d3d9fc6d89c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/whistle blowing_31ff8887-9fbc-581b-b10f-d3d9fc6d89c9.svg'
AUTHOR = 'gpt-6'


class WhistleWithSoundRays(Solo48):
    icon_id = 'whistle-with-sound-rays'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('whistle', 'with', 'sound', 'rays')

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

        path('shell',(26,18),[(42,18),(42,26),(34,30),((22,42),12,12,True),((10,30),12,12,True),((22,18),12,12,True),(26,18)],True)
        circle('hole',22,30,3)
        self.add_line('ray-top',(22,6),(22,9))
        self.add_line('ray-diagonal',(8,8),(10,10))
        self.add_dot('ray-left',(6,17))
