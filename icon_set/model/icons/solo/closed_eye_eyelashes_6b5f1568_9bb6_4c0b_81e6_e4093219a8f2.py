'Closed Eye with Eyelashes.\nPlan: Broad circular lower eyelid and three radiating lashes. Six source lashes reduced to three for separation. Bounds4,10..44,38.\nReference: Lucide eye-closed: coherent curved lid and radial lash attachments; human facial-part vocabulary.\nKeyshape: HRECT_M, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b5f1568-9bb6-4c0b-81e6-e4093219a8f2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/eyelashes_6b5f1568-9bb6-4c0b-81e6-e4093219a8f2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-eye-eyelashes'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('closed', 'eye', 'eyelashes')

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

        path('lid',(4,10),[((12,26),20,20,False),((24,30),20,20,False),((36,26),20,20,False),((44,10),20,20,False)])
        for j,(a,b) in enumerate((((12,26),(6,34)),((24,30),(24,38)),((36,26),(42,34)))):self.add_line(f'lash-{j}',a,b);self.relate('connect',f'lash-{j}','lid')
