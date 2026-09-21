"""Rocket and Launch Tower.

Plan: Rocket beside left gantry; bounds6,6,42,42. Broad rocket fins, one brace and support link.
Construction reference: Lucide rocket: pointed capsule and swept lower fins
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a0b432-8eb4-4dfa-ab45-144db351049a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/space rocket launch_97a0b432-8eb4-4dfa-ab45-144db351049a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-rocket-beside-launch-gantry'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('upright', 'rocket', 'beside', 'launch', 'gantry')

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

        poly('gantry',(6,6),(14,6),(14,24),(14,42),(6,42),(6,6),closed=True)
        poly('brace',(6,14),(14,24),(6,34));join('brace','gantry')
        path('rocket',(26,34),[('L',(26,16)),('C',(32,6),(26,12),(30,8)),('C',(38,16),(34,8),(38,12)),('L',(38,34)),('L',(42,42)),('L',(22,42)),('L',(26,34))],True)
        line('arm',(14,24),(26,24));join('arm','gantry');join('arm','rocket')
