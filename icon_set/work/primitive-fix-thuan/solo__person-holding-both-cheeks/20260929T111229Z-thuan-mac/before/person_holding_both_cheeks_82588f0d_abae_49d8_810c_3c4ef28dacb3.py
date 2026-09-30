"""Shocked Person Holding Head.

Plan: Retained the blank rounded head, both cupping hands and chin. Merged overlapping hand/face edges into open connected contours.
Construction reference: human_ref/user.svg circular human head vocabulary; source hands-on-cheeks composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82588f0d-abae-49d8-810c-3c4ef28dacb3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/screamer_82588f0d-abae-49d8-810c-3c4ef28dacb3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-holding-both-cheeks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'holding', 'both', 'cheeks')

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

        path('head',(8,24),[('C',(24,4),(8,12),(12,4)),('C',(40,24),(36,4),(40,12))])
        path('left-hand',(8,44),[('L',(8,24)),('C',(16,28),(12,20),(14,24)),('L',(16,44))]);join('head','left-hand')
        path('right-hand',(40,44),[('L',(40,24)),('C',(32,28),(36,20),(34,24)),('L',(32,44))]);join('head','right-hand')
        path('chin',(16,32),[('A',(32,32),10,10,False)]);join('chin','left-hand');join('chin','right-hand')
