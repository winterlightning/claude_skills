'Bull Head with Upturned Horns\nPlan: Mirrored bull horns and broad tapered muzzle; side ears and nostrils reduced.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Omit tiny eyes, nostril pair and tongue; preserve upturned horns, ears and long muzzle.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a466215a-b95a-46d4-9521-ed15878b3eed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beast_a466215a-b95a-46d4-9521-ed15878b3eed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bull-head-with-upturned-horns'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('bull', 'head', 'with', 'upturned', 'horns')

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
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        self.add_bezier('head',(14,16),((18,12),(30,12),(34,16)),((38,18),(39,20),(42,20)),((42,24),(38,26),(34,26)),((34,34),(31,42),(24,42)),((17,42),(14,34),(14,26)),((10,26),(6,24),(6,20)),((9,20),(10,18),(14,16)))
        self.add_contour('head-outline','head',closed=True)
        for side in [-1,1]:
         x=lambda a:24+side*a
         self.add_bezier(f'horn-{side}',(x(10),16),((x(16),14),(x(17),10),(x(16),6)))
         self.relate('connect',f'horn-{side}','head-outline')
        self.add_line('muzzle',(23,28),(25,28))
