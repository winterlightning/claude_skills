"""Upward Flip Arrow — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '796af6ba-8fcf-4504-9889-b0d48fb06d81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/flip vertical up_796af6ba-8fcf-4504-9889-b0d48fb06d81.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upward-flip-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('upward', 'flip', 'arrow')

    def build(self):
        # Plan: rounded U base, centered upward curved arrow, five evenly repeated top dashes.
        # SQUARE extremes6,6,42,42. Lucide arrow-up informs open head; source owns U and series.
        for i,x in enumerate(range(8,41,8)):self.add_line(f'dash-{i}',(x,6),(x,8))
        self.add_line('left',(8,24),(8,34));self.add_arc('bl',(8,34),(16,42),radius_x=8,sweep=False)
        self.add_line('bottom',(16,42),(32,42));self.add_arc('br',(32,42),(40,34),radius_x=8,sweep=False)
        self.add_line('right',(40,34),(40,24));self.add_contour('base','left','bl','bottom','br','right')
        for n,x in [('left',8),('right',40)]:
            self.add_polyline(n+'-cap',(x-2,24),(x,24),(x+2,24));self.relate('connect',n+'-cap','base')
        self.add_bezier('shaft',(28,32),((24,32),(24,28),(24,26)))
        self.add_line('upper-shaft',(24,26),(24,18));self.add_contour('arrow','shaft','upper-shaft')
        self.add_polyline('head',(18,24),(24,18),(30,24));self.relate('connect','arrow','head')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

