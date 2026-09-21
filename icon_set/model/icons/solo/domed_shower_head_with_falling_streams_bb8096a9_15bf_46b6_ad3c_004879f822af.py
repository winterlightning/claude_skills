"""Shower Head with Water.

Plan: Retained the domed shower head, curved supply pipe and all three broken water columns. Short water dashes become six well-separated marks.
Construction reference: Lucide shower-head: coherent pipe/head geometry and spaced water marks; source upright dome retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb8096a9-15bf-46b6-ad3c-004879f822af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shower_bb8096a9-15bf-46b6-ad3c-004879f822af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-shower-head-with-falling-streams'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('domed', 'shower', 'head', 'with', 'falling', 'streams')

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

        path('head',(8,24),[('A',(18,14),10,10,True),('A',(28,24),10,10,True),('L',(8,24))],True)
        path('pipe',(18,14),[('A',(28,4),10,10,True),('L',(40,4))]);join('pipe','head')
        for x in (10,20,30):line('water-a-'+str(x),(x,34),(x,35));line('water-b-'+str(x),(x,44),(x,44))
