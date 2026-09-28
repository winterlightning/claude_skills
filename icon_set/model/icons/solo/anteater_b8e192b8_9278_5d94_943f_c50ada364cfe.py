"""A broad-backed anteater with lowered elongated muzzle and four-foot suggestion beneath an arched body. Bounds (4,8)-(44,40). Natural side-view asymmetry retained.
Construction reference: Lucide dog: continuous animal outline; source owns arched back and lowered long muzzle.
Omissions: Overlapping far-leg lines omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8e192b8-9278-5d94-943f-c50ada364cfe'
SOURCE_PATH = 'pictographic-primitives/animals/anteater_b8e192b8-9278-5d94-943f-c50ada364cfe.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='anteater'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases=()
    keywords=('anteater',)
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
        path('animal',(4,32),[('C',(10,15),(4,22),(6,18)),('C',(24,8),(14,10),(18,8)),('C',(44,24),(38,8),(44,14)),('L',(44,40)),('L',(36,40)),('L',(35,31)),('C',(28,25),(33,27),(30,26)),('L',(26,40)),('L',(18,40)),('L',(16,24)),('C',(9,27),(13,19),(10,22)),('L',(9,33)),('C',(4,32),(9,38),(4,38))],True)
        line('rear-foot',(28,40),(36,40));join('rear-foot','animal')
