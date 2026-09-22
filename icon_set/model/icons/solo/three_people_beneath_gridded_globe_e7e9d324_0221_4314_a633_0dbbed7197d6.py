"""Global User Community.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
Curved meridian and equator preserve globe identity. Three equal small busts follow human_ref/user.svg: heads r2, shoulder arcs r2, with exactly4 units of visible head/shoulder clearance (8 centerline). Omit extra latitude bands. Source supplies globe-over-three-people arrangement. Wider shoulder experiment violated spacing. Widen globe to radii13/9, reduce meridian width, and retain equal compact shoulders after SVG hole review.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction references: human_ref/user.svg bust vocabulary; Lucide globe and its atoms supply the curved meridian joined at poles and split equator.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7e9d324-0221-4314-a633-0dbbed7197d6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/multiple users network_e7e9d324-0221-4314-a633-0dbbed7197d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-people-beneath-gridded-globe'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ("Global User Community",)
    keywords = ('three', 'people', 'beneath', 'gridded', 'globe')

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

        path('globe',(24,4),[('A',(37,13),13,9,True),('A',(24,22),13,9,True),('A',(11,13),13,9,True),('A',(24,4),13,9,True)],True)
        poly('equator',(11,13),(20,13),(28,13),(37,13))
        path('meridian',(24,4),[('A',(28,13),4,9,True),('A',(24,22),4,9,True),('A',(20,13),4,9,True),('A',(24,4),4,9,True)],True)
        join('equator','meridian');join('equator','globe');join('meridian','globe')
        for j,x in enumerate([10,24,38]):
            circle(f'head-{j}',x,32,2)
            path(f'body-{j}',(x-2,44),[('A',(x+2,44),2,2,True)])
            join(f'head-{j}',f'body-{j}')
