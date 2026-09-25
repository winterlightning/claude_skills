"""Person Wearing Explosive Vest.

Symbol plan: Front figure, head radius5 centered18,11; chest top24 exact detached gap4. Two chest panels and extended bent right arm; extremes6,6,42,42. Remove ambiguous device inference and tiny waist seam.
Construction references: Shared human_ref/user.svg: circular faceless head and broad shoulders. Literal source vest and bent arm.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '152f8e57-b879-40b3-9e9a-155338f12ac6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/suicide bombing_152f8e57-b879-40b3-9e9a-155338f12ac6.svg'
AUTHOR = 'gpt-6'


class PersonWithChestPanelsAndExtendedArm(Solo48):
    icon_id = 'person-with-chest-panels-and-extended-arm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('person', 'with', 'chest', 'panels', 'and', 'extended', 'arm')

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

        circle('head',18,11,5)
        path('vest',(6,24),[(18,24),(30,24),(30,34),(26,34),(18,34),(10,34),(6,34),(6,24)],True)
        self.add_line('panels',(18,24),(18,34))
        path('lower-body',(10,34),[(12,42),(24,42),(26,34)])
        path('arm',(30,24),[(42,24),(42,34),((38,38),4,4,True)])
        for a,b in [('vest','panels'),('vest','arm'),('vest','lower-body')]:self.relate('connect',a,b)
