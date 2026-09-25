'3D Cube Volume.\nPlan: Perspective cube centered on x=24; its three faces share vertices. Detached curved base reaches y44.\nConstruction reference: Lucide box: shared three-face vertices; source base arc retained.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd17d5c7-a42f-42da-9fc1-6c22d8f4b116'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/life like interface volume_bd17d5c7-a42f-42da-9fc1-6c22d8f4b116.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cube-above-curved-base'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cube', 'above', 'curved', 'base')

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

        self.add_polyline('cube',(8,14),(24,4),(40,14),(40,26),(24,34),(8,26),closed=True)
        self.add_polyline('faces',(8,14),(24,22),(40,14))
        self.add_line('front',(24,22),(24,34))
        for a,b in [('cube','faces'),('cube','front'),('faces','front')]:self.relate('connect',a,b)
        path('base',(8,37),[((24,44),16,7,False),((40,37),16,7,False)])

# Additional original represented by this same concept; no duplicate drawing.
SOURCE_REFERENCES = ({'source_icon_id': 'a3d8b0c8-6ade-42bc-abef-f00b08e319c0', 'source_path': '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/life like interface volume_a3d8b0c8-6ade-42bc-abef-f00b08e319c0.svg'},)
