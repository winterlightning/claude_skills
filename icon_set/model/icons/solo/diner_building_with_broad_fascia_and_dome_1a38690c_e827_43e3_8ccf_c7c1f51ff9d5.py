"""Simple Diner Building.

Plan: Broad diner fascia, rooftop dome and lower facade retained. The entrance shares the fascia boundary; the separate small window is omitted. Keyshape HRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a38690c-e827-43e3-8ccf-c7c1f51ff9d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/diner_1a38690c-e827-43e3-8ccf-c7c1f51ff9d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diner-building-with-broad-fascia-and-dome'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('diner', 'building', 'with', 'broad', 'fascia', 'and', 'dome')

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

        path('dome',(14,18),[('A',(24,8),10,10,True),('A',(34,18),10,10,True)])
        rect('fascia',4,18,40,8,3);join('dome','fascia')
        poly('walls',(8,26),(8,40),(40,40),(40,26));join('walls','fascia')
        line('door-left',(24,26),(24,40));join('door-left','walls');join('door-left','fascia')
        line('door-right',(32,26),(32,40));join('door-right','walls');join('door-right','fascia')
