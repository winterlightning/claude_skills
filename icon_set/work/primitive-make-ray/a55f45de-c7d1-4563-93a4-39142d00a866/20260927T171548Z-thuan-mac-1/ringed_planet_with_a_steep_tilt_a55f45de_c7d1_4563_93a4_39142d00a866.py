"""Ringed Planet Saturn.

Plan: Circular planet and steep diagonal ring; bounds6,6,42,42. Ring crosses globe as one intrinsic orbit.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a55f45de-c7d1-4563-93a4-39142d00a866'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ringed-planet-with-a-steep-tilt/20260927T171300Z-thuan-mac-1/reference/astronomy planet saturn 2_a55f45de-c7d1-4563-93a4-39142d00a866.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ringed-planet-with-a-steep-tilt'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('ringed', 'planet', 'with', 'a', 'steep', 'tilt')

    def build(self):

        def path(name, start, commands, closed=False):
            start=(48-start[1],48-start[0]); here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                end=(48-end[1],48-end[0])
                if kind=='C': args=[(48-p[1],48-p[0]) for p in args]
                if kind=='A': args=[args[1],args[0],not args[2]]
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('globe',(9,24),[('A',(24,9),15,15,True),('A',(36,15),15,15,True),('A',(39,24),15,15,True),('A',(24,39),15,15,True),('A',(12,33),15,15,True),('A',(9,24),15,15,True)],True)
        path('orbit',(9,24),[('C',(4,40),(4,29),(4,36)),('C',(12,33),(5,40),(8,36)),('C',(36,15),(20,30),(28,22)),('C',(44,8),(40,12),(43,10)),('C',(39,24),(44,14),(44,19))]);join('orbit','globe')
