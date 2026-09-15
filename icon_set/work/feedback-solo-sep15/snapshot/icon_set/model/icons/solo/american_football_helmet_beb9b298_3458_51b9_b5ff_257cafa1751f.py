'Football helmet: smooth protective dome and attached face guard, with a clear ear opening.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'beb9b298-3458-51b9-b5ff-257cafa1751f'
SOURCE_PATH = 'pictographic-primitives/sports/american football helmet_beb9b298-3458-51b9-b5ff-257cafa1751f.svg'
AUTHOR = 'gpt-6'

class AmericanFootballHelmet(Solo48):
    icon_id = 'american-football-helmet'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
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
        self.add_bezier('shell-top',(4,30),((4,17),(15,8),(25,8)),((34,8),(40,15),(44,24)))
        self.add_polyline('mask',(44,24),(44,40),(36,40),(28,33),(28,24),(44,24))
        self.add_bezier('shell-bottom',(28,33),((28,38),(23,40),(17,40)),((10,40),(4,40),(4,36)))
        self.add_line('rear',(4,36),(4,30))
        self.relate('connect','shell-top','mask');self.relate('connect','mask','shell-bottom');self.relate('connect','shell-bottom','rear');self.relate('connect','rear','shell-top')
        self.add_dot('ear',(16,27))
