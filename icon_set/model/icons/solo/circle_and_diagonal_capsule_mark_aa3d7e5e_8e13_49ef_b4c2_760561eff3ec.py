'Circle and Diagonal Capsule Mark\nPlan: Diagonal capsule descends right; circular companion at lower left. Capsule constructed by tangent Beziers.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa3d7e5e-8e13-49ef-b4c2-760561eff3ec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/analogue logo_aa3d7e5e-8e13-49ef-b4c2-760561eff3ec.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-and-diagonal-capsule-mark'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('circle', 'and', 'diagonal', 'capsule', 'mark')

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

        self.add_bezier('capsule',(20,6),((24,6),(26,8),(28,11)),((32,17),(36,23),(40,29)),((42,32),(42,34),(42,36)),((42,40),(40,42),(36,42)),((32,42),(30,40),(28,37)),((24,31),(20,25),(16,19)),((14,16),(14,14),(14,12)),((14,8),(16,6),(20,6)))
        self.add_contour('capsule-outline','capsule',closed=True)
        circle('companion',11,37,5)
