'A Ferris wheel with five round cabins and a triangular stand.\nPlan: VRECT_L accommodates the top cabin and lower stand.\nReduction: Reduced five spokes to three; retained all five cabins. Moved the stand junction below the wheel to remove small enclosed pockets.\nConstruction: Lucide ferris-wheel: radial members and a distinct triangular support.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '504a0510-ec03-4633-a8b4-a32a2b49ce54'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/amusement park ferris wheel 1_504a0510-ec03-4633-a8b4-a32a2b49ce54.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spoked-ferris-wheel-with-round-cabins'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
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

        self.add_bezier('wheel-upper-left',(24,10),((19,10),(14,11),(14,13)))
        self.add_line('wheel-left-top',(14,13),(14,22))
        self.add_line('wheel-left',(14,22),(14,28))
        self.add_arc('wheel-bottom-left',(14,28),(24,34),radius_x=10,radius_y=6,sweep=False)
        self.add_arc('wheel-bottom',(24,34),(34,28),radius_x=10,radius_y=6,sweep=False)
        self.add_line('wheel-right-bottom',(34,28),(34,22))
        self.add_line('wheel-right',(34,22),(34,13))
        self.add_bezier('wheel-upper-right',(34,13),((34,11),(29,10),(24,10)))
        self.add_contour('wheel','wheel-upper-left','wheel-left-top','wheel-left','wheel-bottom-left','wheel-bottom','wheel-right-bottom','wheel-right','wheel-upper-right',closed=True)
        for k,(x,y) in enumerate([(24,7),(11,13),(37,13),(11,28),(37,28)]):
            circle(f'cabin-{k}',x,y,3); self.relate('connect',f'cabin-{k}','wheel')
        for k,p in enumerate([(24,10),(14,22),(34,22)]):
            self.add_line(f'spoke-{k}',(24,22),p); self.relate('connect',f'spoke-{k}','wheel')
            for j in range(k):self.relate('connect',f'spoke-{k}',f'spoke-{j}')
        self.add_polyline('stand',(24,34),(8,44),(40,44),closed=True);self.relate('connect','stand','wheel')

