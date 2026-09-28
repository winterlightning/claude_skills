"""One raised speaker over three listeners, each with a circular head and broad shoulder marks. The shared human_ref/user.svg bust informed the head and shoulder arrangement; every detached head has an 8-unit centerline gap."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '37cca7c8-c737-48a1-b84a-f06486e9bba1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__speaker-above-three-listeners/20260927T172707Z-thuan-mac-1/reference/asalha puja group_37cca7c8-c737-48a1-b84a-f06486e9bba1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'speaker-above-three-listeners'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('speaker', 'above', 'three', 'listeners')

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
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        circle('head-speaker',24,6,2);line('torso-speaker',(24,16),(24,18));self.mark_human_figure('speaker',head='head-speaker',torso='torso-speaker',torso_junction='start')
        poly('shoulders',(18,18),(21,16),(27,16),(30,18));join('shoulders','torso-speaker')
        for j,x in enumerate((10,24,38)):
         circle(f'head-{j}',x,28,2)
         self.add_bezier(f'torso-{j}',(x,38),((x-1,38),(x-2,40),(x-2,44)))
         self.add_bezier(f'other-shoulder-{j}',(x,38),((x+1,38),(x+2,40),(x+2,44)))
         join(f'torso-{j}',f'other-shoulder-{j}')
         self.mark_human_figure(f'listener-{j}',head=f'head-{j}',torso=f'torso-{j}',torso_junction='start')
