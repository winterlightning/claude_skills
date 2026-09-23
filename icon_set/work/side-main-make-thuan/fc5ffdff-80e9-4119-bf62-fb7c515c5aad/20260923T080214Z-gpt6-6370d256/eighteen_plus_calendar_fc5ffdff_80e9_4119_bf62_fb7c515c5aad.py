"""A eighteen plus calendar reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fc5ffdff-80e9-4119-bf62-fb7c515c5aad'
SOURCE_PATH = 'pictographic-primitives/other/browser with 18+ text_fc5ffdff-80e9-4119-bf62-fb7c515c5aad.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eighteen-plus-calendar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/calendar'
    aliases = ()
    keywords = ('eighteen', 'plus', 'calendar')

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

        self.rounded('calendar',6,10,42,42,4)
        self.add_line('header-divider',(6,18),(42,18))
        self.relate('connect','calendar','header-divider')
        self.add_line('left-binding',(14,6),(14,13))
        self.add_line('right-binding',(34,6),(34,13))
        self.relate('connect','calendar','left-binding')
        self.relate('connect','calendar','right-binding')

        self.add_line('one',(13,27),(13,34))
        self.circle('eight-upper',23,27,3)
        self.circle('eight-lower',23,33,3)
        self.relate('connect','eight-upper','eight-lower')
        self.add_line('plus-h',(32,30),(38,30))
        self.add_line('plus-v',(35,27),(35,33))
        self.relate('connect','plus-h','plus-v')

