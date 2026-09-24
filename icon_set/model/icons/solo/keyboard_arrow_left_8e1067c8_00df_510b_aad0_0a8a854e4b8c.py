"""A continuous U-turn arrow, with one circular bend and equal arrowhead arms. Retain direction and open return; no omissions. Centerline box (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8e1067c8-00df-510b-aad0-0a8a854e4b8c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard arrow left_8e1067c8-00df-510b-aad0-0a8a854e4b8c.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'corner-down-right'
DESIGN_PLAN = 'A continuous U-turn arrow, with one circular bend and equal arrowhead arms. Retain direction and open return; no omissions. Centerline box (4,8)-(44,40).'
class Drawing(Solo48):
    icon_id = 'keyboard-arrow-left-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'left', 'interface', 'essential')

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
        p=lambda x,y:(48-y,x)
        self.add_line('return',p(8,24),p(8,16))
        self.add_arc('bend-left',p(8,16),p(20,4),radius_x=12)
        self.add_arc('bend-right',p(20,4),p(32,16),radius_x=12)
        self.add_line('shaft',p(32,16),p(32,44))
        self.add_contour('turn','return','bend-left','bend-right','shaft')
        self.add_polyline('head',p(24,36),p(32,44),p(40,36))
        self.relate('connect','turn','head')
