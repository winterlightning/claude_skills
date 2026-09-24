"""A telephone handset inside a speech bubble.
Repair plan: Open receiver cradle with tangent circular sweep and short ear ends. Tail and receiver preserve intended asymmetry.
Omissions: Inner return outline of handset.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='91565135-36f8-42bb-b2ed-6c12f04a7eb5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/tty answer_91565135-36f8-42bb-b2ed-6c12f04a7eb5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tty-answer'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('tty', 'answer')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,left,top,right,bottom,r):
        p=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
           (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        names=[]
        for i,start in enumerate(p):
            n=f'{name}-{i}';end=p[(i+1)%8]
            if i%2:self.add_arc(n,start,end,radius_x=r)
            else:self.add_line(n,start,end)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def cross(self,name,x,y,r,diagonal=False):
        ends=[(-r,-r),(r,r),(r,-r),(-r,r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        for i,(dx,dy) in enumerate(ends):self.add_line(f'{name}-{i}',(x,y),(x+dx,y+dy))
        self.relate('connect',*[f'{name}-{i}' for i in range(4)])

    def monitor(self,left=6,top=6,right=42,bottom=34,foot=42):
        # Matched quarter-round corners, bottom wall split at the stand junction.
        r=4;cx=(left+right)//2
        self.add_line('screen-top',(left+r,top),(right-r,top))
        self.add_arc('screen-tr',(right-r,top),(right,top+r),radius_x=r)
        self.add_line('screen-right',(right,top+r),(right,bottom-r))
        self.add_arc('screen-br',(right,bottom-r),(right-r,bottom),radius_x=r)
        self.add_line('screen-bottom-r',(right-r,bottom),(cx,bottom))
        self.add_line('screen-bottom-l',(cx,bottom),(left+r,bottom))
        self.add_arc('screen-bl',(left+r,bottom),(left,bottom-r),radius_x=r)
        self.add_line('screen-left',(left,bottom-r),(left,top+r))
        self.add_arc('screen-tl',(left,top+r),(left+r,top),radius_x=r)
        self.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-r','screen-bottom-l','screen-bl','screen-left','screen-tl',closed=True)
        self.add_line('stand',(cx,bottom),(cx,foot))
        self.add_polyline('foot',(cx-8,foot),(cx,foot),(cx+8,foot))
        self.relate('connect','stand','screen-bottom-r','screen-bottom-l')
        self.relate('connect','stand','foot')

    def browser(self):
        # Chrome separator joins explicitly split side walls; two tiny source
        # chrome dashes are omitted so the content keeps the available height.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-upper',(42,10),(42,14))
        self.add_line('right-lower',(42,14),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left-lower',(6,38),(6,14))
        self.add_line('left-upper',(6,14),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('browser','top','tr','right-upper','right-lower','br','bottom','bl','left-lower','left-upper','tl',closed=True)
        self.add_line('chrome',(6,14),(42,14))
        self.relate('connect','chrome','left-upper','left-lower','right-upper','right-lower')

    def build(self):
        self.add_line('bubble-top',(14,6),(34,6))
        self.add_arc('bubble-tr',(34,6),(42,14),radius_x=8)
        self.add_line('bubble-right',(42,14),(42,28))
        self.add_arc('bubble-br',(42,28),(34,36),radius_x=8)
        self.add_polyline('tail',(34,36),(22,36),(14,42),(14,36))
        self.add_arc('bubble-bl',(14,36),(6,28),radius_x=8)
        self.add_line('bubble-left',(6,28),(6,14))
        self.add_arc('bubble-tl',(6,14),(14,6),radius_x=8)
        self.add_contour('bubble','bubble-top','bubble-tr','bubble-right','bubble-br','tail-1','tail-2','tail-3','bubble-bl','bubble-left','bubble-tl',closed=True)
        # Open receiver stroke: smooth cradle with short perpendicular ear ends.
        self.add_line('receiver-ear-left',(20,16),(16,16))
        self.add_arc('receiver-cradle',(16,16),(27,27),radius_x=11,sweep=False)
        self.add_polyline('receiver-ear-right',(27,27),(31,27),(31,23))
        self.add_contour('receiver','receiver-ear-left','receiver-cradle','receiver-ear-right-1','receiver-ear-right-2')
        self.contours = [c for c in self.contours if c.contour_id not in ['tail', 'receiver-ear-right']]
