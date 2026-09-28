'Hand Grenade with Safety Pin.\nPlan: Oval grenade body with two cross grooves, a central meridian and a rear safety ring. Cap and body share a neck.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Dense grid reduced to one meridian and one cross-groove; safety ring added as a rear arc.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7a56ae2-766c-4e0e-9092-08ce21ae1d13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grenade_d7a56ae2-766c-4e0e-9092-08ce21ae1d13.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'segmented-hand-grenade-with-ring'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('segmented', 'hand', 'grenade', 'with', 'ring')

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

        path('body',(14,16),[(24,16),((34,30),10,14,True),((24,44),10,14,True),(14,44),((8,30),6,14,True),((14,16),6,14,True)],True)
        self.add_polyline('cap',(14,16),(14,4),(26,4),(26,16));self.relate('connect','cap','body')
        self.add_line('meridian',(24,16),(24,44));self.relate('connect','meridian','body')
        self.add_polyline('groove',(8,30),(24,30),(34,30));self.relate('connect','groove','body');self.relate('connect','groove','meridian')
        path('ring',(26,6),[((40,16),14,10,True),((34,22),6,6,True)])
        self.relate('connect','ring','cap')
