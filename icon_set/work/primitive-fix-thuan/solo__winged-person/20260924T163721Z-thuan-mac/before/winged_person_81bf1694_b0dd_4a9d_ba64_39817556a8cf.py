'Person with Wings.\nPlan: Round-headed figure with paired low wings joining the shoulders and hip. Head radius5 at24,11; upper torso24,24 establishes exact4 ink gap and vertical alignment. Wings x6..42, legs end42; feather layers omitted.\nReference: human_ref/full_body_ref.png: circular head aligned over upper torso with exact4 ink gap; source wings reduced to one lobe each.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81bf1694-b0dd-4a9d-ba64-39817556a8cf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/wingman_81bf1694-b0dd-4a9d-ba64-39817556a8cf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winged-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('winged', 'person')

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

        circle('head',24,11,5)
        self.add_line('torso',(24,24),(24,34))
        self.add_polyline('legs',(18,42),(24,34),(30,42));self.relate('connect','legs','torso')
        path('wings',(24,24),[(14,24),((6,32),8,8,False),((14,36),8,4,False),(24,34)])
        path('wings-right',(24,24),[(34,24),((42,32),8,8,True),((34,36),8,4,True),(24,34)])
        for name in ('wings','wings-right'):self.relate('connect',name,'torso');self.relate('connect',name,'legs')
        self.relate('connect','wings','wings-right')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
