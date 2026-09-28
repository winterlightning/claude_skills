"""Round Trip Flight.

Plan: Two opposite-facing aircraft profiles; bounds6,6,42,42. Small lower dashed trail reduced to one dash.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5c99c76c-2246-4e49-81d2-870738acb779'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__opposing-airplanes-in-profile/20260927T165437Z-thuan-mac-1/reference/plane trip return_5c99c76c-2246-4e49-81d2-870738acb779.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'opposing-airplanes-in-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('opposing', 'airplanes', 'in', 'profile')

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

        for name,offset,direction in [('upper',0,1),('lower',24,-1)]:
         def p(x,y):return(x if direction==1 else 48-x,y+offset)
         # Each source aircraft is a side-view fuselage with a raised wing and tail.
         path(name,p(12,12),[
             ('L',p(36,12)),('L',p(36,20)),('L',p(12,20)),
             ('A',p(12,12),4,4,direction==1),
         ],closed=True)
         line(name+'-wing',p(20,12),p(26,4));join(name,name+'-wing')
         line(name+'-tail',p(36,12),p(40,8));join(name,name+'-tail')
