'Twin-Prong Nasal Device\nPlan: Wide curved nasal base with two outward prongs; shared prong/base attachments.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Omit prong collars and lower seam; preserve two prongs on curved base.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'daac8d7c-b6f2-41d2-a661-6c4a0fb6210d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/anti snorting device_daac8d7c-b6f2-41d2-a661-6c4a0fb6210d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twin-prong-nasal-device'
    keyshape = Keyshape.HRECT_L
    category = "primitives-generate"
    keywords = ('twin', 'prong', 'nasal', 'device')

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

        path('base',(4,24),[(44,24),((24,40),20,16,True),((4,24),20,16,True)],True)
        self.add_polyline('left-prong',(10,24),(8,8),(18,8),(20,24));self.relate('connect','left-prong','base')
        self.add_polyline('right-prong',(28,24),(30,8),(40,8),(38,24));self.relate('connect','right-prong','base')
