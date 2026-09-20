'Water Drop and Ripple.\nPlan: Pointed droplet above wide open oval ripple. Opening below drop preserves separation. Bounds8,4..40,44.\nReference: Lucide droplet: pointed crown and rounded lower bulb; source open ripple retained.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '936ab246-e53f-4ea0-ab8c-85dda69a6887'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/tinkle_936ab246-e53f-4ea0-ab8c-85dda69a6887.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'water-drop-ripple'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('water', 'drop', 'ripple')

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

        path('drop',(24,4),[(34,20),((24,30),10,10,True),((14,20),10,10,True),(24,4)],True)
        path('ripple',(14,37),[((8,40),6,3,False),((24,44),16,4,False),((40,40),16,4,False),((34,37),6,3,False)])

SOURCE_REFERENCES = [('936ab246-e53f-4ea0-ab8c-85dda69a6887', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tinkle_936ab246-e53f-4ea0-ab8c-85dda69a6887.svg'), ('34284741-8762-4fe7-b3d9-f3e6e854de48', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tinkle_34284741-8762-4fe7-b3d9-f3e6e854de48.svg')]
