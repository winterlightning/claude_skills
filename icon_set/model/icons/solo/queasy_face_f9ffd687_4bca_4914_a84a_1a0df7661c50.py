'Vomiting Face Emoji.\nPlan: Round face interrupted at lower right by a broad expelled cloud, with two closed eyes. Small mouth line omitted. Bounds6..42.\nReference: No useful local Lucide queasy match; circular face and source protruding cloud retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9ffd687-4bca-4914-a84a-1a0df7661c50'
SOURCE_PATH = 'pictographic-primitives/smileys/sick_f9ffd687-4bca-4914-a84a-1a0df7661c50.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'queasy-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('queasy', 'face')

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

        path('face',(42,24),[((24,6),18,18,False),((6,24),18,18,False),((24,42),18,18,False)])
        path('cloud',(24,42),[(22,34),((28,30),6,4,True),(34,34),(38,34),((42,38),4,4,True),((36,42),6,4,True),(24,42)],True);self.relate('connect','face','cloud')
        path('eye-left',(16,19),[((20,19),2,2,False)]);path('eye-right',(28,19),[((32,19),2,2,False)])
