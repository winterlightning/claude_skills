'Football Passing Through Goalposts\nPlan: Goal at right, detached ball at upper left, two trajectory dashes rising from lower left. Shared post junction.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Two trajectory dashes; ball kept separate from goal.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47149a22-d0ce-4e36-93a9-5d52a967e3c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/american football score_47149a22-d0ce-4e36-93a9-5d52a967e3c3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'football-passing-through-goalposts'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('football', 'passing', 'through', 'goalposts')

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

        self.add_polyline('goal',(26,6),(26,28),(42,28),(42,6))
        self.add_line('post',(33,28),(33,42)); self.relate('connect','goal','post')
        self.add_line('foot',(25,42),(41,42)); self.relate('connect','post','foot')
        ellipse('ball',12,13,6,4)
        self.add_line('trail-low',(6,42),(7,37))
        self.add_line('trail-high',(10,29),(13,25))
