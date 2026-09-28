'Two-Seat Swing Carousel\nPlan: Mirrored seats on diagonal suspension lines beneath canopy; center post and base share true joins.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Two larger seats; preserve canopy, pole and ground.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fca3e902-bfef-4a53-9e7b-f8aed479be76'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amusement park rides_fca3e902-bfef-4a53-9e7b-f8aed479be76.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-seat-swing-carousel'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('two', 'seat', 'swing', 'carousel')

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

        self.add_polyline('canopy',(6,16),(24,6),(42,16),(24,16),(6,16))
        self.add_line('post',(24,16),(24,42));self.relate('connect','post','canopy')
        self.add_line('ground',(6,42),(42,42));self.relate('connect','ground','post')
        for k,x in enumerate([11,37]):
            self.add_line(f'rope-{k}',(x,16),(x,25));self.relate('connect',f'rope-{k}','canopy')
            path(f'seat-{k}',(x-5,25),[(x+5,25),((x-5,25),5,8,True)],True)
            self.relate('connect',f'rope-{k}',f'seat-{k}')
