'Open Palm Helping Hand.\nPlan: Open upturned hand with cupped fingertips and distinct thumb. Bounds4,10..44,38.\nConstruction reference: Lucide hand rounded contour vocabulary; source palm-up gesture.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21f148ad-8725-429c-aa23-cad9257d7f13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/give hand 1_21f148ad-8725-429c-aa23-cad9257d7f13.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-helping-hand'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('open', 'helping', 'hand')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
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

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_bezier('upper',(44,14),((34,14),(32,10),(26,10)),((20,10),(20,18),(14,18)))
        self.add_bezier('fingers',(14,18),((10,14),(4,10),(4,18)),((4,22),(14,32),(20,36)),((24,38),(26,38),(28,38)),((34,38),(38,34),(44,32)))
        self.relate('connect','upper','fingers')
        self.add_line('thumb',(14,18),(28,18));self.relate('connect','thumb','upper');self.relate('connect','thumb','fingers')
