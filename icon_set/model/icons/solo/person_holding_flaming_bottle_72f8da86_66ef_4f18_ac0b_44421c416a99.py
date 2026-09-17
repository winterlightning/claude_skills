"""Person Throwing Molotov Cocktail.

Symbol plan: Directional bottle at left; circle head radius4 at30,10; torso starts30,22, exact detached ink gap4. Extremes6,6,42,42. Remove finger and bottle-neck seams.
Construction references: Shared human_ref/full_body_ref.png: circular head and coherent limbs; source curling flame.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72f8da86-66ef-4f18-ac0b-44421c416a99'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/protest fire bottle_72f8da86-66ef-4f18-ac0b-44421c416a99.svg'
AUTHOR = 'gpt-6'


class PersonHoldingFlamingBottle(Solo48):
    icon_id = 'person-holding-flaming-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('person', 'holding', 'flaming', 'bottle')

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

        circle('head',30,10,4)
        self.add_line('torso',(30,22),(30,32))
        path('arms',(14,24),[(22,24),(30,22),(42,24)])
        path('legs',(20,42),[(30,32),(38,42)])
        path('bottle',(6,24),[(6,16),(10,16),(14,16),(14,24),(6,24)],True)
        self.add_bezier('flame',(10,16),((4,11),(6,10),(8,6)),((16,10),(16,13),(10,16)))
        for a,b in [('torso','arms'),('torso','legs'),('arms','bottle'),('bottle','flame')]:self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
