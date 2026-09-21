"""Sanitary Pad with Wings.

Plan: Retained the elongated pad and both wings. Merged their silhouette and reduced the absorbent panel to a central groove.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c0cc94b-c3c9-4fed-9273-dc0721aef56a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/pad_6c0cc94b-c3c9-4fed-9273-dc0721aef56a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winged-sanitary-pad'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('winged', 'sanitary', 'pad')

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

        path('pad',(15,13),[('A',(24,4),9,9,True),('A',(33,13),9,9,True),('L',(33,16)),('L',(36,16)),('A',(40,20),4,4,True),('L',(40,28)),('A',(36,32),4,4,True),('L',(33,32)),('L',(33,35)),('A',(24,44),9,9,True),('A',(15,35),9,9,True),('L',(15,32)),('L',(12,32)),('A',(8,28),4,4,True),('L',(8,20)),('A',(12,16),4,4,True),('L',(15,16)),('L',(15,13))],True)
        line('groove',(24,15),(24,33))
