'Football helmet: smooth protective dome and attached face guard, with a clear ear opening.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "beb9b298-3458-51b9-b5ff-257cafa1751f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__american-football-helmet/20260926T085631Z-thuan-mac/reference/american football helmet_beb9b298-3458-51b9-b5ff-257cafa1751f.svg"
AUTHOR = "claude-opus-5-5"

class AmericanFootballHelmet(Solo48):
    icon_id = 'american-football-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('american', 'football', 'helmet')

    def circle(self, name, x, y, radius):
        self.add_arc(name+'-top',(x-radius,y),(x+radius,y),radius_x=radius)
        self.add_arc(name+'-bottom',(x+radius,y),(x-radius,y),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self, branches):
        # Declare only actual shared endpoints in the physical figure.
        segments=[]
        for name,points in branches:
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}'
                self.add_line(key,a,b);segments.append((key,a,b))
            if len(points)>2:self.add_contour(name,*[f'{name}-{i}' for i in range(len(points)-1)])
        for index,(a,p,q) in enumerate(segments):
            for b,r,s in segments[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def oval(self,name,x,y,rx,ry):
        self.add_arc(name+'-top',(x-rx,y),(x+rx,y),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(x+rx,y),(x-rx,y),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Symbol plan (HRECT_L x4..44, y8..40): side-view helmet facing right.
        # Shell: rear x4, dome top y8, front tip (40,20), front edge back to
        # (30,24), straight jaw to (34,40), flat bottom to a r4 rear corner.
        # Face guard: bar from the jaw at (32,32) out to x44, down to y40 and
        # back to the jaw foot. Ear hole: hollow r3 ring at (18,28), 9 above the bottom.
        L = self.add_line
        L('rear', (4, 36), (4, 26))
        self.add_bezier('dome-back', (4, 26), ((4, 16), (12, 8), (22, 8)))
        self.add_bezier('dome-front', (22, 8), ((32, 8), (40, 13), (40, 20)))
        L('front-edge', (40, 20), (30, 24))
        L('jaw-upper', (30, 24), (32, 32))
        L('jaw-lower', (32, 32), (34, 40))
        L('bottom', (34, 40), (8, 40))
        self.add_arc('rear-corner', (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('shell', 'rear', 'dome-back', 'dome-front', 'front-edge', 'jaw-upper',
                         'jaw-lower', 'bottom', 'rear-corner', closed=True)
        self.add_polyline('guard', (32, 32), (44, 32), (44, 40), (34, 40))
        self.relate('connect', 'shell', 'guard')
        self.circle('ear', 18, 28, 3)
