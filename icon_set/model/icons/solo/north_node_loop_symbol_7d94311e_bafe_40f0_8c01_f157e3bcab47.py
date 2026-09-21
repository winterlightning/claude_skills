'North Node Loop Symbol\nPlan: North-node emblem: domed center narrows into two circular lower loops, mirrored about x24.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d94311e-bafe-40f0-8c01-f157e3bcab47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astrology head node_7d94311e-bafe-40f0-8c01-f157e3bcab47.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'north-node-loop-symbol'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('north', 'node', 'loop', 'symbol')

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

        self.add_bezier('arch',(18,36),((18,25),(12,19),(12,14)),((12,6),(18,6),(24,6)),((30,6),(36,6),(36,14)),((36,19),(30,25),(30,36)))
        circle('left-loop',12,36,6);circle('right-loop',36,36,6)
        self.relate('connect','arch','left-loop');self.relate('connect','arch','right-loop')
