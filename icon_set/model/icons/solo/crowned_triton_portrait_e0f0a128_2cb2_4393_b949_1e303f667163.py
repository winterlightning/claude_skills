"""A crowned Triton with a broad beard and long hair. Lucide crown informs three peaks and a straight band; omit eyes and hair waves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0f0a128-2cb2-4393-b949-1e303f667163'
SOURCE_PATH = 'pictographic-primitives/religion/triton_e0f0a128-2cb2-4393-b949-1e303f667163.svg'
AUTHOR = 'gpt-6'

class CrownedTritonPortrait(Solo48):
    icon_id = 'crowned-triton-portrait'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('triton', 'crown', 'beard', 'portrait', 'king', 'mythology')

    def oval(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Vertical centerline box (8,4)-(40,44), mirrored about x=24.
        self.add_polyline('crown',(12,18),(12,8),(18,12),(24,4),(30,12),(36,8),(36,18),(12,18))
        self.oval('beard',24,37,8,7)
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            name=str(side)
            self.add_polyline('face-'+name,p(12,18),p(8,26),p(8,37))
            self.add_polyline('hair-'+name,p(16,24),p(16,36),p(8,37))
            self.add_line('shoulder-'+name,p(16,44),p(8,37))
            self.relate('connect','face-'+name,'crown')
            for a,b in [('face-'+name,'beard'),('hair-'+name,'beard'),('shoulder-'+name,'beard'),('face-'+name,'hair-'+name),('face-'+name,'shoulder-'+name),('hair-'+name,'shoulder-'+name)]:
                self.relate('connect',a,b)
