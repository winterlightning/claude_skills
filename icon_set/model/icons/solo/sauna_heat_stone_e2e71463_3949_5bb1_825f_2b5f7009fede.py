"""Three coherent heat waves rise over a smooth stone bowl.
Symbol plan: shared parameters and coherent contours.
Construction: No useful exact Lucide match; repeated smooth arcs.
Omissions: None
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e2e71463-3949-5bb1-825f-2b5f7009fede'
SOURCE_PATH = 'pictographic-primitives/spas/sauna heat stone_e2e71463-3949-5bb1-825f-2b5f7009fede.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='sauna-heat-stone'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="spas"
    aliases=()
    keywords=('sauna', 'heat', 'stone')

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
        # Identical two-arc waves own spacing; opposing sweeps meet tangentially.
        for i,x in enumerate([12,24,36]):
            self.path('heat-'+str(i),(x+2,6),[('A',(x,15),7,7,False),('A',(x-2,24),7,7,True)])
        self.path('stone',(6,32),[('A',(24,42),18,10,False),('A',(42,32),18,10,False)])
