'Vomiting Face Emoji.\nPlan: Open-bottom circular face with closed eyes and two flowing discharge strokes. Radius20 centered24.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Omit raised eyebrows; use one coherent open mouth and two widely spaced flowing sides.\nKeyshape: CIRCLE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6e31c44-cd76-4e66-bc6d-ad1ab6ef4aa8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face vomit_b6e31c44-cd76-4e66-bc6d-ad1ab6ef4aa8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vomiting-face-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('vomiting', 'face', 'solo')

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

        path('face',(8,36),[((4,24),20,20,True),((24,4),20,20,True),((44,24),20,20,True),((40,36),20,20,True)])
        for x in (16,32):self.add_line(f'eye-{x}',(x-1,18),(x+1,18))
        path('vomit',(18,42),[((18,34),6,8,False),(18,32),((30,32),6,5,True),(30,34),((30,42),6,8,False)])
