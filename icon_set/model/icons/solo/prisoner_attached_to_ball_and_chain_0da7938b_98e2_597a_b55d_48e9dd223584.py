"""Prisoner with Ball and Chain.

Symbol plan: Frontal stick prisoner and attached ankle ball, head r5 at16,11; torso24 gives exact gap4. Extremes6,6,42,42. Single curved chain replaces individual links.
Construction references: Shared human_ref/full_body_ref.png: circle head, simple limbs. Lucide spline: connecting curve between objects.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0da7938b-98e2-597a-b55d-48e9dd223584'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/prisoner ball_0da7938b-98e2-597a-b55d-48e9dd223584.svg'
AUTHOR = 'gpt-6'


class PrisonerAttachedToBallAndChain(Solo48):
    icon_id = 'prisoner-attached-to-ball-and-chain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('prisoner', 'attached', 'to', 'ball', 'and', 'chain')

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

        circle('head',16,11,5)
        self.add_line('torso',(16,24),(16,32))
        path('arms',(6,32),[(6,26),(16,24),(24,26)])
        path('legs',(10,42),[(16,32),(22,42)])
        circle('ball',36,36,6)
        self.add_bezier('chain',(22,42),((28,42),(26,36),(30,36)))
        for a,b in [('torso','arms'),('torso','legs'),('legs','chain'),('chain','ball')]:self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
