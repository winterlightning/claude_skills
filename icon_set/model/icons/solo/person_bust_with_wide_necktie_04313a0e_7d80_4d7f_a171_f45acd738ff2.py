"""Professional Person with Necktie.

Plan: Professional bust: circular head r8 at24,12; shoulder top24 gives 0 ink gap. Curved open-bottom torso and broad tie. Bounds8,4,40,44.
Construction reference: human_ref/user.svg: circular head and broad curved shoulders; current avatar touching-ink rule
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04313a0e-7d80-4d7f-a171-f45acd738ff2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/congressman_04313a0e-7d80-4d7f-a171-f45acd738ff2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-bust-with-wide-necktie'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'bust', 'with', 'wide', 'necktie')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member='shoulder-top' if name=='body' and index==2 else f"{name}-{index}"
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

        path('head',(24,4),[('A',(32,12),8,8,True),('A',(24,20),8,8,True),('A',(16,12),8,8,True),('A',(24,4),8,8,True)],True)
        path('body',(8,44),[('L',(8,36)),('A',(20,24),12,12,True),('L',(28,24)),('A',(40,36),12,12,True),('L',(40,44))]);join('head','body')
        poly('tie',(24,24),(19,40),(24,44),(29,40),closed=True);join('tie','body')
