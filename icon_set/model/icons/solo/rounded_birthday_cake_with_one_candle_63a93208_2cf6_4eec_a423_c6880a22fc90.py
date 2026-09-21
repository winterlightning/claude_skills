'Rounded Birthday Cake with One Candle\nPlan: Cake with two icing waves, central single candle and detached flame dot.\nReference: Lucide cake: wavy icing and upright candle.\nReduction: Flame reduced to a detached round mark for legal spacing.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63a93208-2cf6-4eec-a423-c6880a22fc90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/birthday cake_63a93208-2cf6-4eec-a423-c6880a22fc90.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-birthday-cake-with-one-candle'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('rounded', 'birthday', 'cake', 'with', 'one', 'candle')

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

        box('cake',8,24,40,44,4)
        self.add_bezier('icing',(8,33),((13,35),(19,31),(24,33)),((29,35),(35,31),(40,33)));self.relate('connect','icing','cake')
        self.add_polyline('candle',(20,24),(20,14),(28,14),(28,24));self.relate('connect','candle','cake')
        self.add_dot('flame',(24,4))
