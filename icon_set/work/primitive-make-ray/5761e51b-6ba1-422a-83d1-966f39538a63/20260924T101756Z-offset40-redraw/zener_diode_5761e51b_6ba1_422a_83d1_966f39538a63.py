"""A right-pointing diode triangle with a straight cathode bar and two leads. Bounds (4,8)-(44,40). Restore the straight cathode shown by the reference.
Construction reference: No useful exact Lucide match; electrical source symbol owns geometry.
Omissions: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5761e51b-6ba1-422a-83d1-966f39538a63'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__zener-diode/20260924T101756Z-thuan-mac/reference/zener diode_5761e51b-6ba1-422a-83d1-966f39538a63.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='zener-diode'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('zener', 'diode')
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
        poly('anode',(14,8),(34,24),(14,40),closed=True)
        poly('cathode',(34,8),(34,24),(34,40));join('anode','cathode')
        line('lead-left',(4,24),(14,24));join('lead-left','anode')
        line('lead-right',(34,24),(44,24));join('lead-right','cathode');join('lead-right','anode')
