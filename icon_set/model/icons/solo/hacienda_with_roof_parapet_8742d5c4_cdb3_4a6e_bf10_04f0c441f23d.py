'Traditional Hacienda Manor House.\nPlan: Hacienda facade with pitched roof, notched parapet and arched door.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Small eave ticks omitted; parapet, roof, doorway and broad facade retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8742d5c4-cdb3-4a6e-bf10-04f0c441f23d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/hacienda_8742d5c4-cdb3-4a6e-bf10-04f0c441f23d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hacienda-with-roof-parapet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hacienda', 'with', 'roof', 'parapet')

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

        path('roof',(8,24),[(12,16),(36,16),(40,24),(38,24),(10,24),(8,24)],True)
        self.add_polyline('parapet',(12,16),(12,4),(20,4),(20,8),(28,8),(28,4),(36,4),(36,16));self.relate('connect','parapet','roof')
        self.add_polyline('walls',(10,24),(10,44),(19,44),(29,44),(38,44),(38,24));self.relate('connect','walls','roof')
        path('door',(19,44),[(19,38),((29,38),5,5,True),(29,44)]);self.relate('connect','door','walls')
