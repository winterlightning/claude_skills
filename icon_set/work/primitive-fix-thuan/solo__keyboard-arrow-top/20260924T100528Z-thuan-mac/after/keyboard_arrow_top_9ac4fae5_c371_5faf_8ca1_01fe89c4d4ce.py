"""A continuous U-turn arrow, with one circular bend and equal arrowhead arms. Retain direction and open return; no omissions. Centerline box (8,4)-(40,44)."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9ac4fae5-c371-5faf-8ca1-01fe89c4d4ce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__keyboard-arrow-top/20260924T100528Z-thuan-mac/reference/keyboard arrow top_9ac4fae5-c371-5faf-8ca1-01fe89c4d4ce.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'corner-down-right'
DESIGN_PLAN = 'A continuous U-turn arrow, with one circular bend and equal arrowhead arms. Retain direction and open return; no omissions. Centerline box (8,4)-(40,44).'
class Drawing(Solo48):
    icon_id = 'keyboard-arrow-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'top')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)

    def build(self):
        p=lambda x,y:(48-x,48-y)
        self.add_line('return',p(8,24),p(8,16))
        self.add_arc('bend-left',p(8,16),p(20,4),radius_x=12)
        self.add_arc('bend-right',p(20,4),p(32,16),radius_x=12)
        self.add_line('shaft',p(32,16),p(32,44))
        self.add_contour('turn','return','bend-left','bend-right','shaft')
        self.add_polyline('head',p(24,36),p(32,44),p(40,36))
        self.relate('connect','turn','head')
