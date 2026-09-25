"""A smartwatch yuan sign reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '130ae17c-e9b2-44fc-bcbf-03cd5a3dc1d9'
SOURCE_PATH = 'pictographic-primitives/combination/smart watch square yuan sign_130ae17c-e9b2-44fc-bcbf-03cd5a3dc1d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smartwatch-yuan-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('smartwatch', 'yuan', 'sign')

    def rounded(self, name, left, top, right, bottom, radius=4):
        p = [(left+radius,top),(right-radius,top),(right,top+radius),
             (right,bottom-radius),(right-radius,bottom),(left+radius,bottom),
             (left,bottom-radius),(left,top+radius),(left+radius,top)]
        ids=[]
        for j,(a,b) in enumerate(zip(p,p[1:]),1):
            elem=f"{name}-{j}"
            if j%2: self.add_line(elem,a,b)
            else: self.add_arc(elem,a,b,radius_x=radius)
            ids.append(elem)
        self.add_contour(name,*ids,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def build(self) -> None:

        # One watch silhouette keeps a larger readable square dial.
        self.add_line('watch-top',(17,4),(31,4))
        self.add_line('watch-top-right-band',(31,4),(32,8))
        self.add_line('watch-top-right-shoulder',(32,8),(36,8))
        self.add_arc('watch-ne',(36,8),(40,12),radius_x=4)
        self.add_line('watch-right',(40,12),(40,36))
        self.add_arc('watch-se',(40,36),(36,40),radius_x=4)
        self.add_line('watch-bottom-right-shoulder',(36,40),(32,40))
        self.add_line('watch-bottom-right-band',(32,40),(31,44))
        self.add_line('watch-bottom',(31,44),(17,44))
        self.add_line('watch-bottom-left-band',(17,44),(16,40))
        self.add_line('watch-bottom-left-shoulder',(16,40),(12,40))
        self.add_arc('watch-sw',(12,40),(8,36),radius_x=4)
        self.add_line('watch-left',(8,36),(8,12))
        self.add_arc('watch-nw',(8,12),(12,8),radius_x=4)
        self.add_line('watch-top-left-shoulder',(12,8),(16,8))
        self.add_line('watch-top-left-band',(16,8),(17,4))
        self.add_contour('watch',*(x for x in (
            'watch-top','watch-top-right-band','watch-top-right-shoulder','watch-ne',
            'watch-right','watch-se','watch-bottom-right-shoulder','watch-bottom-right-band',
            'watch-bottom','watch-bottom-left-band','watch-bottom-left-shoulder','watch-sw',
            'watch-left','watch-nw','watch-top-left-shoulder','watch-top-left-band')),closed=True)

        self.add_polyline('yuan-forks',(19,18),(24,25),(29,18))
        self.add_line('yuan-bar',(20,25),(28,25))
        self.add_line('yuan-stem',(24,25),(24,31))
        self.relate('connect','yuan-forks','yuan-bar')
        self.relate('connect','yuan-forks','yuan-stem')
        self.relate('connect','yuan-bar','yuan-stem')

