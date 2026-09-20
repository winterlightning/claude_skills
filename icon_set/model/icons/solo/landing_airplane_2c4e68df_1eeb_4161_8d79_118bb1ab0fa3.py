'Airplane Landing on Runway.\nPlan: Rightward plane silhouette above detached runway; swept wing remains in outline.\nConstruction reference: Lucide plane: preserve a coherent wing/tail silhouette; source side view retained.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c4e68df-1eeb-4161-8d79-118bb1ab0fa3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/landing_2c4e68df-1eeb-4161-8d79-118bb1ab0fa3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'landing-airplane'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('landing', 'airplane')

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

        path('plane',(4,20),[(12,20),(10,8),(18,8),(30,20),(38,20),((44,26),6,6,True),((38,32),6,6,True),(14,32),((4,22),10,10,True),(4,20)],True)
        self.add_line('runway',(4,40),(44,40))
