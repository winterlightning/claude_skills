'Woman Wearing Islamic Niqab.\nPlan: Niqab with rounded hood, broad eye opening, long tapered veil and curved shoulders. Bounds8,4..40,44.\nConstruction reference: human_ref/user.svg curved shoulders and centered head vocabulary; source face-obscuring clothing contours retained.\nReduction: Simplify outer shawl folds while retaining veil and shoulder distinction.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd8bb0b8-d3a2-456b-a36a-3fff3804821d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/islamic women niqab 1_bd8bb0b8-d3a2-456b-a36a-3fff3804821d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-wearing-niqab'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('woman', 'wearing', 'niqab')

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

        path('crown',(12,16),[((36,16),12,12,True)])
        self.add_line('eye-upper',(12,16),(36,16));self.relate('connect','eye-upper','crown')
        path('veil-left',(12,16),[(12,26),(13,35),(14,44)])
        path('veil-right',(36,16),[(36,26),(35,35),(34,44)])
        path('eye-lower',(12,26),[((36,26),12,4,False)])
        for n in ('veil-left','veil-right'):
         self.relate('connect',n,'crown');self.relate('connect',n,'eye-upper');self.relate('connect',n,'eye-lower')
        self.add_bezier('shoulder-left',(13,35),((8,35),(8,40),(8,44)))
        self.add_bezier('shoulder-right',(35,35),((40,35),(40,40),(40,44)))
        self.relate('connect','shoulder-left','veil-left');self.relate('connect','shoulder-right','veil-right')
