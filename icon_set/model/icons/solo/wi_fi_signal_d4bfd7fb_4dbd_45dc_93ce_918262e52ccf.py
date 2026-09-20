'Wifi Signal Strength.\nPlan: Three nested Wi-Fi crests and centered signal dot; mirrored smooth curves. Bounds4,8..44,40.\nConstruction reference: Lucide wifi original and atomic-debug: three mirrored nested crests and centered signal dot.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4bfd7fb-4dbd-45dc-93ce-918262e52ccf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wifi fair_d4bfd7fb-4dbd-45dc-93ce-918262e52ccf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wi-fi-signal'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('wi', 'fi', 'signal')

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

        for n,l,y,top in [('outer',4,16,5.333333333333333),('middle',11,25,20),('inner',18,33,31)]:
         self.add_bezier(n,(l,y),((l+5,top),(48-l-5,top),(48-l,y)))
        self.add_dot('signal',(24,40))
