"""Scientist Wearing Glasses and Lab Coat.

Plan: Retained the centered circular face, round spectacles and broad curved shoulders. Enlarged the spectacles and omitted cramped coat lapels. Face radius 14 at (24,18), jaw bottom 32 and shoulder top 36 give zero visible ink gap.
Construction reference: human_ref/user.svg: circular head and rounded shoulders; avatar contact rule.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c61c2ca8-17c1-4390-9206-72043bde469f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/scientist_c61c2ca8-17c1-4390-9206-72043bde469f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scientist-with-round-glasses'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('scientist', 'with', 'round', 'glasses')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member="body-top" if name=="body" and index==0 else f"{name}-{index}"
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

        self.add_arc('jaw',(10,18),(38,18),radius_x=14,radius_y=14,sweep=False)
        path('scalp',(10,18),[('A',(24,4),14,14,True),('A',(38,18),14,14,True)]);join('jaw','scalp')
        circle('left-lens',16,18,6);circle('right-lens',32,18,6);line('bridge',(22,18),(26,18));join('bridge','left-lens');join('bridge','right-lens');join('jaw','left-lens');join('jaw','right-lens');join('scalp','left-lens');join('scalp','right-lens')
        path('body',(8,44),[('A',(24,36),20,20,True),('A',(40,44),20,20,True)]);join('body','jaw')
