"""Group of People with Leader.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
One raised speaker and three listeners preserve the hierarchy. Fine shoulder contours are reduced to short torso strokes.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: Shared human_ref/full_body_ref.png proportions; circular heads with exactly 8 centerline / 4 ink units to their torso starts..
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37cca7c8-c737-48a1-b84a-f06486e9bba1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/asalha puja group_37cca7c8-c737-48a1-b84a-f06486e9bba1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'speaker-above-three-listeners'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
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
        line('ledge',(18,18),(30,18));join('ledge','torso-speaker')
        for j,x in enumerate([10,24,38]):
         circle(f'head-{j}',x,28,2);line(f'torso-{j}',(x,38),(x,44));self.mark_human_figure(f'listener-{j}',head=f'head-{j}',torso=f'torso-{j}',torso_junction='start')
