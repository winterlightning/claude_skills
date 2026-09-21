"""Hand Patting Head.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The patting hand meets the crown; the circular jaw remains above the shoulder line. Fine facial details are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: Shared human_ref/user.svg bust construction and local Lucide users-round; human-reference.md proportions..
Circular jaw to shoulder top is exactly 4 centerline units, giving the shared bust ink tangency; this is not a detached stick-figure neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4077c6c6-c997-4cfb-9962-ebea9a6df687'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pat_4077c6c6-c997-4cfb-9962-ebea9a6df687.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-resting-on-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    human_construction = "bust"
    aliases = ()
    keywords = ('hand', 'resting', 'on', 'head')

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

        self.add_arc('jaw',(14,22),(34,22),radius_x=10,radius_y=10,sweep=False)
        self.add_line('head-top',(14,20),(14,22));self.add_line('head-right',(34,22),(34,20))
        self.add_contour('face','head-top','jaw','head-right')
        self.add_line('body-top',(14,36),(34,36));self.add_line('body-left',(6,42),(14,36));self.add_line('body-right',(34,36),(42,42));self.add_contour('shoulders','body-left','body-top','body-right');join('face','shoulders')
        path('hand',(42,6),[('L',(26,6)),('L',(10,12)),('A',(14,20),5,5,False),('L',(24,18)),('L',(34,20)),('L',(42,20))]);join('hand','face')
