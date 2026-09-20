'Unity Logo Isometric Cube.\nPlan: Isometric cube with diamond top and two side faces. Hidden edge stubs omitted. Bounds6..42.\nReference: Lucide box: coherent six-sided outline and shared Y-shaped face junction.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f49f0dc-8111-4c9b-acae-0731c78ef67a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/tools unity_3f49f0dc-8111-4c9b-acae-0731c78ef67a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'isometric-cube'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('isometric', 'cube')

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

        self.add_polyline('outline',(24,6),(42,16),(42,32),(24,42),(6,32),(6,16),closed=True)
        self.add_polyline('top-face',(6,16),(24,26),(42,16));self.add_line('front-edge',(24,26),(24,42));self.relate('connect','outline','top-face');self.relate('connect','outline','front-edge');self.relate('connect','top-face','front-edge')

SOURCE_REFERENCES = [('3f49f0dc-8111-4c9b-acae-0731c78ef67a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tools unity_3f49f0dc-8111-4c9b-acae-0731c78ef67a.svg')]
