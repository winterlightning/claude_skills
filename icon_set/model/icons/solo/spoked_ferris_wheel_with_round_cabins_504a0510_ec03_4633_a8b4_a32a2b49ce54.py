'Spoked Ferris Wheel with Round Cabins\nPlan: Five round cabins physically join the circular wheel at shared cardinal points; spokes meet at one hub.\nReference: Lucide ferris-wheel: radial members and triangular stand.\nReduction: Retain all five cabins; wheel rebuilt with coherent shared nodes.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '504a0510-ec03-4633-a8b4-a32a2b49ce54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amusement park ferris wheel 1_504a0510-ec03-4633-a8b4-a32a2b49ce54.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spoked-ferris-wheel-with-round-cabins'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('spoked', 'ferris', 'wheel', 'with', 'round', 'cabins')

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

        self.add_bezier('wheel-upper-left',(24,10),((19,10),(14,11),(14,16)))
        self.add_bezier('wheel-left',(14,16),((14,20),(14,24),(14,28)))
        self.add_bezier('wheel-bottom',(14,28),((14,33),(34,33),(34,28)))
        self.add_bezier('wheel-right',(34,28),((34,24),(34,20),(34,16)))
        self.add_bezier('wheel-upper-right',(34,16),((34,11),(29,10),(24,10)))
        self.add_contour('wheel','wheel-upper-left','wheel-left','wheel-bottom','wheel-right','wheel-upper-right',closed=True)
        for k,(x,y) in enumerate([(24,7),(11,16),(37,16),(11,28),(37,28)]):
            circle(f'cabin-{k}',x,y,3); self.relate('connect',f'cabin-{k}','wheel')
        for k,p in enumerate([(24,10),(14,16),(34,16),(14,28),(34,28)]):
            self.add_line(f'spoke-{k}',(24,22),p); self.relate('connect',f'spoke-{k}','wheel')
            for j in range(k):self.relate('connect',f'spoke-{k}',f'spoke-{j}')
        self.add_polyline('stand',(24,22),(8,44),(40,44),(24,22));self.relate('connect','stand','wheel')
        for k in range(5):self.relate('connect','stand',f'spoke-{k}')
