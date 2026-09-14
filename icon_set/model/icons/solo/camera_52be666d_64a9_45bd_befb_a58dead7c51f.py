"""Front camera with raised housing and centered lens; Lucide camera informs rounded body and lens axis."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52be666d-64a9-45bd-befb-a58dead7c51f'
SOURCE_PATH = 'pictographic-primitives/video/camera_52be666d-64a9-45bd-befb-a58dead7c51f.svg'
AUTHOR = 'gpt-6'

class Camera(Solo48):
    icon_id = 'camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('camera', 'photography', 'lens', 'photo', 'device', 'optics', 'snapshot')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def rounded(self, name, x, y, w, h, r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]; ident=name+'-'+str(i);ids.append(ident)
            if i%2:self.add_arc(ident,a,b,radius_x=r)
            else:self.add_line(ident,a,b)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Front camera with raised housing and centered lens; Lucide camera informs rounded body and lens axis.
        housing = [(8,14),(14,14),(18,8),(30,8),(34,14),(40,14)]
        for n,(a,b) in enumerate(zip(housing,housing[1:]),1):
            self.add_line(f'housing-{n}',a,b)
        self.add_arc('tr',(40,14),(42,18),radius_x=4)
        self.add_line('right',(42,18),(42,36))
        self.add_arc('br',(42,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(8,40))
        self.add_arc('bl',(8,40),(6,36),radius_x=4)
        self.add_line('left',(6,36),(6,18))
        self.add_arc('tl',(6,18),(8,14),radius_x=4)
        self.add_contour('body',*[f'housing-{i}' for i in range(1, 6)],'tr','right','br','bottom','bl','left','tl',closed=True)
        self.circle('lens',24,25,6)
