'Broad Curved Sweeping Broom\nPlan: Broad curved broom tapers to a round handle; two tip sweep at base and separate dust.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: One clean dust puff; broad curved two-tip broom silhouette retained.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a0e03d9-b69e-480d-a8e2-6dac337ad0f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/broom sweep 2_9a0e03d9-b69e-480d-a8e2-6dac337ad0f9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-curved-sweeping-broom'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('broad', 'curved', 'sweeping', 'broom')

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

        self.add_bezier('broom',(6,32),((17,29),(28,17),(33,8)),((34,6),(36,6),(38,6)),((42,6),(42,8),(42,10)),((42,11),(41,12),(40,13)),((34,28),(28,42),(20,42)),((16,42),(16,38),(18,36)),((12,40),(8,37),(6,32)))
        self.add_contour('outline','broom',closed=True)
        circle('dust',10,13,4)
