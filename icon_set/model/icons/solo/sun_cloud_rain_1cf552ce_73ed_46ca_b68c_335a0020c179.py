'Sun Cloud and Rain Drops.\nPlan: An exposed solar disc joins the rounded cloud above two pointed raindrops.\nConstruction reference: Lucide cloud-sun: integrated sun/cloud silhouette with an explicit shared arc.\nReduction: Sun rays omitted; two enlarged raindrops retain the rainy-weather identity.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cf552ce-73ed-46ca-b68c-335a0020c179'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather rain drops_1cf552ce-73ed-46ca-b68c-335a0020c179.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-cloud-rain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sun', 'cloud', 'rain')

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

        path('outline',(12,18),[((6,12),6,6,True),((12,6),6,6,True),((18,12),6,6,True),((30,12),6,4,True),((42,18),12,6,True),((36,23),6,5,True),(18,23),((12,18),6,5,True)],True)
        path('sun-seam',(18,12),[((12,18),6,6,True)]);self.relate('connect','sun-seam','outline')

        for j,x in enumerate((15,35)):
         path(f'drop-{j}',(x,32),[(x+5,37),((x-5,37),5,5,True),(x,32)],True)
