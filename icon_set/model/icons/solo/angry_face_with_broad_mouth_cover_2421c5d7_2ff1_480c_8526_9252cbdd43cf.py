'Angry Face with Broad Mouth Cover\nPlan: Round upper face over broad rectangular mask and visible chin arc; angry eye strokes inset from dome.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2421c5d7-2ff1-480c-8526-9252cbdd43cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/smiley decode_2421c5d7-2ff1-480c-8526-9252cbdd43cf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angry-face-with-broad-mouth-cover'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('angry', 'face', 'with', 'broad', 'mouth', 'cover')

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

        self.add_arc('dome',(6,24),(42,24),radius_x=18)
        path('cover',(6,24),[(42,24),(42,31),((38,35),4,4,True),(10,35),((6,31),4,4,True),(6,24)],True)
        self.relate('connect','dome','cover')
        self.add_arc('chin',(12,35),(36,35),radius_x=12,radius_y=7,sweep=False);self.relate('connect','chin','cover')
        self.add_line('eye-left',(19,15),(20,16));self.add_line('eye-right',(29,15),(28,16))
