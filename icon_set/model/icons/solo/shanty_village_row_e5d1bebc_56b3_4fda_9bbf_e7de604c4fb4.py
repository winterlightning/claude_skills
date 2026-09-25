"""Four modest village dwellings arranged in two overlapping rows, with true pitched rear roofs. Envelope (6,6)-(42,42). Shared wall nodes preserve actual contacts.
Construction reference: Lucide house: simple pitched roofs and coherent wall outlines.
Omissions: Tiny building irregularities simplified."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5d1bebc-56b3-4fda-9bbf-e7de604c4fb4'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/shanty house village_e5d1bebc-56b3-4fda-9bbf-e7de604c4fb4.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='shanty-village-row'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases=()
    keywords=('shanty', 'house', 'village')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        poly('rear-left',(6,25),(6,16),(15,10),(24,16),(24,22))
        poly('rear-right',(24,16),(24,12),(33,6),(42,12),(42,24));join('rear-left','rear-right')
        poly('front',(20,42),(20,33),(30,28),(42,33),(42,42),(20,42),(6,42),(6,34),(20,34))
