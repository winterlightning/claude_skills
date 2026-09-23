"""A calendar checkmark reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7539933b-41e7-42c6-8893-c05af64c76c8'
SOURCE_PATH = 'pictographic-primitives/interface-essential/calendar check_7539933b-41e7-42c6-8893-c05af64c76c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'calendar-checkmark'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/calendar'
    aliases = ()
    keywords = ('calendar', 'checkmark')

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

        self.add_polyline('check',(15,28),(21,34),(33,24))

