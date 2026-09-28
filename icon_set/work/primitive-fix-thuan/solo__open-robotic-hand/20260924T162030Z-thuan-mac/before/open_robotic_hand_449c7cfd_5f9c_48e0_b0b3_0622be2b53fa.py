'Open Robotic Hand.\nPlan: Articulated open robotic hand with left cuff, thumb and raised two-part finger. Bounds4,10..44,38.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Preserve two visible digit forms; omit fine seams.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '449c7cfd-5f9c-48e0-b0b3-0622be2b53fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/robot hand_449c7cfd-5f9c-48e0-b0b3-0622be2b53fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-robotic-hand'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('open', 'robotic', 'hand')

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

        self.add_polyline('cuff',(4,14),(12,14),(12,34),(4,34))
        self.add_bezier('palm',(12,14),((18,10),(24,10),(26,10)))
        path('thumb',(26,10),[((26,18),4,4,True)])
        self.add_bezier('lower',(12,34),((20,34),(24,38),(28,38)),((34,38),(38,30),(44,26)))
        path('finger',(44,26),[(44,18),(40,18),(28,30),(26,18)])
        for a,z in [('cuff','palm'),('palm','thumb'),('cuff','lower'),('lower','finger'),('finger','thumb')]:self.relate('connect',a,z)
