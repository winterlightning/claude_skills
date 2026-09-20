'Three Bladed Wind Turbine.\nPlan: Three open rotor blades meet the hub above a vertical wind-turbine mast.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Narrow enclosed blades and small hub ring reduced to open rotor strokes meeting at one hub node.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3d28fda-3648-4ab3-a4cc-cf06d1ff7799'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wind turbine_e3d28fda-3648-4ab3-a4cc-cf06d1ff7799.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-bladed-wind-turbine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'bladed', 'wind', 'turbine')

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

        self.add_line('top-blade',(24,22),(24,4))
        self.add_polyline('left-blade',(24,22),(16,26),(8,34))
        self.add_polyline('right-blade',(24,22),(32,30),(40,34))
        self.add_line('mast',(24,22),(24,44))
        for a,b in [('top-blade','left-blade'),('top-blade','right-blade'),('top-blade','mast'),('left-blade','right-blade'),('left-blade','mast'),('right-blade','mast')]:self.relate('connect',a,b)
