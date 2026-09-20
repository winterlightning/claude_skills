'Vertical Classic Surfboard.\nPlan: Mirrored surfboard with pointed nose and broad continuous rounded sides, short flat tail. Bounds10,4..38,44.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: VRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73d75cdb-2fbf-4f3f-92ba-79cedfc8d079'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/surfboard_73d75cdb-2fbf-4f3f-92ba-79cedfc8d079.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-surfboard'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('upright', 'surfboard')

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

        self.add_bezier('right',(24,4),((34,12),(38,24),(38,34)),((38,38),(36,42),(34,44)))
        self.add_line('tail',(34,44),(14,44))
        self.add_bezier('left',(14,44),((12,42),(10,38),(10,34)),((10,24),(14,12),(24,4)))
        self.add_contour('board','right','tail','left',closed=True)
        self.add_line('stringer',(24,4),(24,44));self.relate('connect','board','stringer')
