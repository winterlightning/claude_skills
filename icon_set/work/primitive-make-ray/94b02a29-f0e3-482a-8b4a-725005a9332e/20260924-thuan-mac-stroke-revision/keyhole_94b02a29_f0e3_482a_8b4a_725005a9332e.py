"""Symmetric keyhole with a circular crown and flared stem. VRECT_M centerlines (10,4)-(38,44); replace segmented crown with one shared circle. No omissions."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '94b02a29-f0e3-482a-8b4a-725005a9332e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__keyhole/20260924T100528Z-thuan-mac/reference/keyhole_94b02a29-f0e3-482a-8b4a-725005a9332e.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'key-round'
DESIGN_PLAN = 'Symmetric keyhole with a circular crown and flared stem. VRECT_M centerlines (10,4)-(38,44); replace segmented crown with one shared circle. No omissions.'
class Drawing(Solo48):
    icon_id = 'keyhole'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('keyhole',)

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
        self.path('outline',(16,26),[('A',(10,18),14,14,True),('A',(24,4),14,14,True),('A',(38,18),14,14,True),('A',(32,26),14,14,True),('L',(38,44)),('L',(10,44)),('L',(16,26))],True)
