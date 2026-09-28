"""Handcuffs and Key.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
Two circular cuffs remain linked, with a separate key beside them. Fine lock housings are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: No useful local Lucide match was found..
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a54478b-4849-4373-b597-046376cb8fb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crime tools shackle key_4a54478b-4849-4373-b597-046376cb8fb9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'handcuff-pair-with-separate-key'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('handcuff', 'pair', 'with', 'separate', 'key')

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

        circle('cuff-left',14,34,8);circle('cuff-right',34,14,8)
        path('chain',(14,26),[('L',(10,18)),('C',(18,6),(6,6),(10,6)),('L',(28,8))]);join('chain','cuff-left');join('chain','cuff-right')
        circle('key-head',34,40,2);poly('key-shaft',(36,38),(42,32),(42,36));join('key-head','key-shaft')
