'Ancient Egyptian Eye of Horus Symbol.\nPlan: Almond-shaped eye with attached iris divider and a sweeping lower curl. Shared extrema keep the pupil within the eye.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Separate brow and small hook omitted; iris reduced to a vertical divider. Preserve almond eye and descending curl.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39cae645-1b03-49ce-9b24-d31178b647e1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/eye of horus_39cae645-1b03-49ce-9b24-d31178b647e1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eye-of-horus'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('eye', 'of', 'horus')

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

        path('eye',(4,16),[((24,8),25,20,True),((44,16),25,20,True),((24,24),25,20,True),((4,16),25,20,True)],True)
        self.add_line('iris',(24,8),(24,24));self.relate('connect','iris','eye')
        path('flourish',(44,16),[((14,40),30,24,True),((6,32),8,8,True)])
        self.relate('connect','flourish','eye')
