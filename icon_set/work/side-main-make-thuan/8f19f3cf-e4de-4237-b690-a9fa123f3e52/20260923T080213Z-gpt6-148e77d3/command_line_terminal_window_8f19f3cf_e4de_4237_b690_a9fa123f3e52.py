"""A command line terminal window reconstructed on the SOLO48 grid. Source silhouette and internal mark are retained; matching paired elements share coordinates. Lucide geometric construction informs the outer device or enclosure."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8f19f3cf-e4de-4237-b690-a9fa123f3e52'
SOURCE_PATH = 'pictographic-primitives/programing/app window code_8f19f3cf-e4de-4237-b690-a9fa123f3e52.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'command-line-terminal-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/computer'
    aliases = ()
    keywords = ('command', 'line', 'terminal', 'window')

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

        self.rounded('terminal',6,6,42,42,4)
        self.add_line('title-divider',(6,17),(42,17))
        self.relate('connect','terminal','title-divider')
        self.add_polyline('prompt',(14,24),(21,29),(14,35))
        self.add_line('cursor',(29,34),(34,34))

