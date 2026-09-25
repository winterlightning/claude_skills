"""A seated koala facing right with broad round ears, a droplet nose and open reaching forearm. Envelope (6,6)-(42,42).
Construction reference: Lucide rat: coherent rounded animal contour; original koala owns ears, nose and seated pose.
Omissions: Small rear toe notch omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7aff43af-b040-54db-ae24-ae746f735733'
SOURCE_PATH = 'pictographic-primitives/animals/koala body_7aff43af-b040-54db-ae24-ae746f735733.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='sitting-koala'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases=()
    keywords=('koala', 'body')
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
        path('koala',(14,22),[('C',(6,14),(7,24),(6,18)),('C',(12,6),(6,9),(8,6)),('C',(17,8),(14,6),(16,7)),('C',(29,8),(20,6),(26,6)),('C',(36,6),(31,6),(34,6)),('C',(42,14),(40,6),(42,9)),('C',(31,23),(42,22),(36,23)),('L',(29,28)),('L',(41,28)),('C',(31,36),(41,34),(36,36)),('L',(27,36)),('C',(37,40),(32,36),(37,38)),('C',(24,42),(37,42),(29,42)),('L',(17,42)),('C',(9,35),(12,42),(9,40)),('C',(16,25),(9,31),(13,28)),('L',(14,22))],True)
        line('nose',(24,15),(24,19))
