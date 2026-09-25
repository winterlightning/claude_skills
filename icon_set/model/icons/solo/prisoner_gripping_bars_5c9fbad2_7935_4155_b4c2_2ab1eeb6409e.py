"""Prisoner Behind Bars.

Symbol plan: Front prisoner with two widely spaced gripped bars, circular head r5 at24,9; shoulders22 exact gap4. Extremes8,4,40,44. Reduce four bars to two to reveal person.
Construction references: Shared human_ref/full_body_ref.png: simple circular head and coherent limbs. Bars intersect at hand endpoints.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c9fbad2-7935-4155-b4c2-2ab1eeb6409e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/prisoner bars_5c9fbad2-7935-4155-b4c2-2ab1eeb6409e.svg'
AUTHOR = 'gpt-6'


class PrisonerGrippingBars(Solo48):
    icon_id = 'prisoner-gripping-bars'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('prisoner', 'gripping', 'bars')

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

        circle('head',24,9,5)
        self.add_line('torso',(24,22),(24,34))
        path('arms',(8,26),[(16,26),(24,22),(32,26),(40,26)])
        path('legs',(16,44),[(24,34),(32,44)])
        for x in (8,40):
         path(f'bar-{x}',(x,4),[(x,26),(x,44)])
         self.relate('connect','arms',f'bar-{x}')
        self.relate('connect','torso','arms');self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
