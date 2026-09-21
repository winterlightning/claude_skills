'Curved Straw Broom Sweeping Dust\nPlan: Sweeping curved broom with detached dust puff; coherent taper and handle seam.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: One round dust puff replaces two lobes; retain curved sweep and open bristle ends.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23b1dce1-01a3-4d0e-9224-6b91d6c92bd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/broom sweep 1_23b1dce1-01a3-4d0e-9224-6b91d6c92bd5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-straw-broom-sweeping-dust'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('curved', 'straw', 'broom', 'sweeping', 'dust')

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

        self.add_bezier('broom',(6,36),((21,28),(29,17),(34,8)),((35,6),(38,6),(39,6)),((42,6),(42,9),(42,12)),((39,25),(28,40),(20,42)))
        circle('dust',11,15,5)
