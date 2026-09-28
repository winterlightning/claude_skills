"""A horizontal fork with two visible tines, wrapped noodle and a curling hanging strand. Envelope (4,8)-(44,40). Gentle S curve restores the hanging pasta.
Construction reference: Lucide utensils: open fork and rounded tine junction.
Omissions: Repeated fine wraps and outlined handle reduced for stroke spacing."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='21cd9183-a949-443f-9aa0-592ab7600755'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__spaghetti-wrapped-fork/20260924T100518Z-thuan-mac/reference/pasta fork_21cd9183-a949-443f-9aa0-592ab7600755.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='spaghetti-wrapped-fork'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('pasta', 'fork')
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
        path('fork',(44,16),[('L',(22,16)),('A',(18,20),4,4,False),('A',(22,24),4,4,False),('L',(44,24))])
        line('handle',(4,20),(18,20));join('handle','fork')
        path('pasta',(28,24),[('L',(28,12)),('A',(36,12),4,4,True),('L',(36,28)),('C',(28,34),(36,32),(32,34)),('C',(24,40),(24,34),(24,37))]);join('pasta','fork')
