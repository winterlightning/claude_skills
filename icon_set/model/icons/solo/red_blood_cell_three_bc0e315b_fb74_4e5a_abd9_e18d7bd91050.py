"""Three separate red blood cells in a triangular arrangement.
Symbol plan: shared parameters and coherent contours.
Construction: No useful exact Lucide match; coherent elliptical contours.
Omissions: Small source tilts reduced to horizontal ovals to avoid fragmented curves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc0e315b-fb74-4e5a-abd9-e18d7bd91050'
SOURCE_PATH = 'pictographic-primitives/health/red blood cell three_bc0e315b-fb74-4e5a-abd9-e18d7bd91050.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='red-blood-cell-three'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "health"
    categories = ("health", "primitives")
    aliases=()
    keywords=('red', 'blood', 'cell', 'three')

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
        # Three oval definitions retain the source count and broad triangular arrangement.
        self.oval('upper-left',12,12,8,4)
        self.oval('upper-right',36,18,8,5)
        self.oval('lower',17,33,11,7)
