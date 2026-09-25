"""A document letter f reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '603e744e-6453-48b2-bc77-5d86475a6c47'
SOURCE_PATH = 'pictographic-primitives/other/f text in file_603e744e-6453-48b2-bc77-5d86475a6c47.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'document-letter-f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/document'
    aliases = ()
    keywords = ('document', 'letter', 'f')

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

        self.add_line('page-top',(12,4),(31,4))
        self.add_line('page-fold',(31,4),(40,13))
        self.add_line('page-right',(40,13),(40,40))
        self.add_arc('page-se',(40,40),(36,44),radius_x=4)
        self.add_line('page-bottom',(36,44),(12,44))
        self.add_arc('page-sw',(12,44),(8,40),radius_x=4)
        self.add_line('page-left',(8,40),(8,8))
        self.add_arc('page-nw',(8,8),(12,4),radius_x=4)
        self.add_contour('page','page-top','page-fold','page-right','page-se',
                         'page-bottom','page-sw','page-left','page-nw',closed=True)
        self.add_polyline('letter-f',(18,33),(18,17),(29,17))
        self.add_line('f-cross',(18,25),(28,25))
        self.relate('connect','letter-f','f-cross')

