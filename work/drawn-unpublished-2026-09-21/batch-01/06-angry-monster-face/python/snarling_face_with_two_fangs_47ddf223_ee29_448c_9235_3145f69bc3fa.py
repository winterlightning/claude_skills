'Snarling Face with Two Fangs\nPlan: Rounded square snarling face, slanted eyes and open mouth with two fangs.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove secondary tongue line and under-eye curves to preserve expression at 48px.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47ddf223-ee29-448c-9235-3145f69bc3fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/snarl_47ddf223-ee29-448c-9235-3145f69bc3fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'snarling-face-with-two-fangs'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('snarling', 'face', 'with', 'two', 'fangs')

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

        box('face',6,6,42,42,10)
        self.add_line('left-eye',(16,16),(20,19));self.add_line('right-eye',(32,16),(28,19))
        path('mouth',(16,28),[(32,28),((24,33),8,5,True),((16,28),8,5,True)],True)
        self.add_line('fang-left',(20,28),(20,30));self.add_line('fang-right',(28,28),(28,30))
        for s in ['left','right']:self.relate('connect',f'fang-{s}','mouth')
