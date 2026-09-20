'Tattooing Heart on Shoulder.\nPlan: Curved shoulder carrying a heart tattoo touched by a diagonal tool with two crossbars.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Inner arm crease omitted; shoulder outline, heart and two tool crossbars retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09849323-30e8-4e89-80f9-b5adff38e1bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tattoo arm tattoo_09849323-30e8-4e89-80f9-b5adff38e1bd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shoulder-heart-tattooing'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('shoulder', 'heart', 'tattooing')

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

        path('shoulder',(8,12),[((16,20),8,8,True),(16,26)])
        path('heart',(20,30),[((16,26),4,4,False),((12,30),4,4,False),((16,38),8,10,False),(20,42),(24,38),((28,30),8,10,False),((24,26),4,4,False),((20,30),4,4,False)],True)
        self.relate('connect','heart','shoulder')
        self.add_line('arm',(20,42),(20,44));self.relate('connect','arm','heart')
        self.add_polyline('needle',(34,7),(28,17),(24,26));self.relate('connect','needle','heart')
        self.add_polyline('bar-top',(28,4),(34,7),(40,10));self.add_polyline('bar-bottom',(24,15),(28,17),(32,19))
        self.relate('connect','needle','bar-top');self.relate('connect','needle','bar-bottom')
