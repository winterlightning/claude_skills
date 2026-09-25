'Amphitheater Seating and Round Stage\nPlan: Broad two-tier seating arc above separate round stage; radial separators omitted.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Omit radial aisle dividers; preserve tier arc and separate cylindrical stage.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a4178c7-eedb-4a97-930f-a81a357d0119'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amfitheater in delphi_8a4178c7-eedb-4a97-930f-a81a357d0119.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'amphitheater-seating-and-round-stage'
    keyshape = Keyshape.HRECT_L
    category = "objects"
    keywords = ('amphitheater', 'seating', 'and', 'round', 'stage')

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

        path('seating',(4,24),[((44,24),20,16,True),(36,24),((12,24),12,7,False),(4,24)],True)
        path('stage',(16,34),[((32,34),8,3,True),(32,37),((16,37),8,3,True),(16,34)],True)
