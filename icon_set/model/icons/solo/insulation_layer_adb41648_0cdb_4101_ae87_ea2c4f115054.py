'Thermal Insulation Layer.\nPlan: Three hanging material lobes integrated into the upper slab, above a second slab.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Internal upper horizontal seam omitted so the three material lobes remain clear.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'adb41648-0cdb-4101-ae87-ea2c4f115054'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/insulation_adb41648-0cdb-4101-ae87-ea2c4f115054.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'insulation-layer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('insulation', 'layer')

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

        path('upper',(4,8),[(44,8),(44,20),((36,20),4,3,True),((28,20),4,2,False),((20,20),4,3,True),((12,20),4,2,False),((4,20),4,3,True),(4,8)],True)
        path('lower',(4,32),[(44,32),(44,40),(4,40),(4,32)],True)
