"""Circular kissing face, mirrored closed eyes and one coherent double-lobed puckered mouth. CIRCLE centerline radius20. No body or detached-head spacing applies. Remove the tiny horizontal mouth spur."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6d7ea7dd-e49c-5a02-891f-cdbd627ace40'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kiss/20260924T100528Z-thuan-mac/reference/kiss_6d7ea7dd-e49c-5a02-891f-cdbd627ace40.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'No useful local face match; shared human reference inspected for circular head vocabulary.'
DESIGN_PLAN = 'Circular kissing face, mirrored closed eyes and one coherent double-lobed puckered mouth. CIRCLE centerline radius20. No body or detached-head spacing applies. Remove the tiny horizontal mouth spur.'
class Drawing(Solo48):
    icon_id = 'kiss'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('kiss',)

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
        self.circle('face',24,24,20)
        for n,x in enumerate((17,31)):
            self.path(f'eye-{n}',(x-3,19),[('C',(x+3,19),(x-1,16),(x+1,16))])
        self.path('mouth',(23,27),[('C',(23,31),(29,27),(29,31)),('C',(23,35),(29,31),(29,35))])
