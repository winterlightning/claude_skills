"""A snarling face with two fangs.
Repair plan: Mirrored slanting brows and enlarged mouth; shared fang dimensions.
Omissions: Tongue and lower eye contours from the detailed source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '47ddf223-ee29-448c-9235-3145f69bc3fa'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/snarl_47ddf223-ee29-448c-9235-3145f69bc3fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'snarling-face-with-two-fangs'
    keyshape = Keyshape.VRECT_L
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

        box('face',8,4,40,44,8)
        self.add_line('left-eye',(17,15),(20,18));self.add_line('right-eye',(31,15),(28,18))
        path('mouth',(17,27),[(31,27),((24,35),7,8,True),((17,27),7,8,True)],True)
        self.add_line('fang-left',(20,27),(20,29));self.add_line('fang-right',(28,27),(28,29))
        for s in ['left','right']:self.relate('connect',f'fang-{s}','mouth')
