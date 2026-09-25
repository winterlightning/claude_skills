'Person with Radiant Aura.\nPlan: Centered radius6 head at24,24 with touching shoulder ink at34, five separate rays and broad open shoulders. Bounds6..42.\nReference: human_ref/user.svg: circular head and smooth broad shoulders. Avatar ink gap0, centerline gap4; Lucide user proportions.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba37ec3b-c43a-4e7b-ba9c-137577c3b1a5'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-09/roleplay game aura_ba37ec3b-c43a-4e7b-ba9c-137577c3b1a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-with-radiant-aura'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    aliases = ()
    keywords = ('person', 'with', 'radiant', 'aura')

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

        self.add_arc('head-top',(18,24),(30,24),radius_x=6,sweep=True);self.add_arc('jaw',(30,24),(18,24),radius_x=6,sweep=True);self.add_contour('head','head-top','jaw',closed=True)
        self.add_arc('body-left',(10,42),(20,34),radius_x=10,radius_y=8,sweep=True);self.add_line('body-top',(20,34),(28,34));self.add_arc('body-right',(28,34),(38,42),radius_x=10,radius_y=8,sweep=True);self.add_contour('body','body-left','body-top','body-right');self.relate('connect','head','body')
        for j,(a,b) in enumerate((((24,6),(24,9)),((6,12),(10,14)),((42,12),(38,14)),((6,24),(9,24)),((42,24),(39,24)))):self.add_line(f'ray-{j}',a,b)
