'Waterspout Over Wavy Water.\nPlan: Wide funnel rim narrows through a twisted spout over two water strokes. Bounds8,4..40,44.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Open the elliptical rim and reduce two crowded wave rows to one broad undulating waterline; preserve twisting funnel.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0102a56-3946-4598-aaf0-332f7c91d6d0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/waterspout_e0102a56-3946-4598-aaf0-332f7c91d6d0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'waterspout-above-waves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('waterspout', 'above', 'waves')

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

        path('rim',(8,8),[((24,4),16,4,True),((40,8),16,4,True)])
        self.add_bezier('left-bank',(8,8),((8,18),(22,18),(20,26)),((18,30),(22,31),(22,31)))
        self.add_bezier('right-bank',(40,8),((40,20),(30,20),(32,26)),((34,30),(32,32),(32,31)))
        self.relate('connect','rim','left-bank');self.relate('connect','rim','right-bank')
        path('water',(8,42),[((24,42),8,2,True),((40,42),8,2,False)])
