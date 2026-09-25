"""A rounded cog surrounded by four radial emphasis marks.
Symbol plan: shared parameters and coherent contours.
Construction: settings: repeated rounded teeth.
Omissions: Tiny source specks removed; radial marks retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ac409f41-db55-4174-adc1-189d24e36f0d'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork cog share_ac409f41-db55-4174-adc1-189d24e36f0d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='radiating-gear'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "work"
    categories = ("work", "primitives")
    aliases=()
    keywords=('radiating', 'gear')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        # Rounded teeth share a 24,24 center. Cardinal dots sit 9 units beyond the cog.
        self.path('gear',(21,15),[('L',(27,15)),('L',(28,18)),('L',(31,17)),('L',(34,22)),('L',(31,24)),('L',(34,26)),('L',(31,31)),('L',(28,30)),('L',(27,33)),('L',(21,33)),('L',(20,30)),('L',(17,31)),('L',(14,26)),('L',(17,24)),('L',(14,22)),('L',(17,17)),('L',(20,18)),('L',(21,15))],True)
        for n,p in [('top',(24,6)),('bottom',(24,42)),('left',(6,24)),('right',(42,24))]:self.add_dot(n,p)
