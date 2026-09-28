'Mythological Harpy Creature.\nPlan: Round human head above broad spread bird wings and two angular legs. Hair, feathers and claw tips omitted. Head radius4 at30,10; torso starts30,22, exact4 ink gap. Bounds6..42.\nReference: human_ref/full_body_ref.png: circular detached head aligned with upper torso, exact4-unit ink gap. Source spread wings retained; no useful local Lucide harpy match.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b87b798c-92b9-4644-b23b-705c2c8cf361'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_22/harpy_b87b798c-92b9-4644-b23b-705c2c8cf361.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winged-harpy-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('winged', 'harpy', 'profile')

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

        circle('head',30,10,4)
        self.add_line('torso',(30,22),(30,26));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('harpy',(6,18),(30,26),(42,18),(42,32),(30,38),(20,36),(6,30),closed=True);self.relate('connect','torso','harpy')
        self.add_line('leg-left',(20,36),(16,42));self.add_line('leg-right',(30,38),(36,42));self.relate('connect','leg-left','harpy');self.relate('connect','leg-right','harpy')
