'Gust of Wind.\nPlan: Three right-curling streams, upper curl rising, two lower curls falling. Staggered endpoints preserve generous gaps. Bounds6..42.\nReference: Lucide wind: horizontal streams ending in coherent round curls.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '181288f1-2380-4aa5-8475-19ae1d611524'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/gale_181288f1-2380-4aa5-8475-19ae1d611524.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-curled-wind-streams'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'curled', 'wind', 'streams')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('upper',(6,14),[(20,14),((20,6),4,4,False)])
        path('middle',(6,24),[(34,24),((34,40),8,8,True)])
        path('lower',(6,34),[(20,34),((20,42),4,4,True)])

SOURCE_REFERENCES = [('80a48910-43ec-4dfd-a250-0befc61930d5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/air_80a48910-43ec-4dfd-a250-0befc61930d5.svg')]
