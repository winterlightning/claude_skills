"""Roaring Lion Head Profile.

Plan: Right-facing lion head, mane and deep mouth notch; bounds6,6,42,42. Ear and eye reduced to simple marks.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7d2768e6-6b3f-4e84-8b06-c307fc8fb78c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__roaring-lion-head-in-profile/20260927T171905Z-thuan-mac-1/reference/roar_7d2768e6-6b3f-4e84-8b06-c307fc8fb78c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'roaring-lion-head-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('roaring', 'lion', 'head', 'in', 'profile')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('lion',(28,42),[
            ('C',(6,24),(18,34),(6,38)),
            ('C',(24,6),(6,14),(12,6)),
            ('C',(34,11),(30,6),(34,8)),
            ('L',(42,16)),('L',(42,21)),('L',(39,24)),
            ('C',(33,24),(37,23),(35,23)),
            ('C',(31,31),(30,25),(29,29)),
            ('C',(36,35),(32,34),(34,35)),
            ('C',(28,42),(38,40),(33,42))
        ],True)
        path('ear',(24,18),[('C',(20,24),(18,14),(17,20))])
