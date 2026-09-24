"""Poseidon with Trident.

Plan: Poseidon bearded head with trident at right; beard lobes and central hair part. Extremes4,8,44,40.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit eyes and parted hair; retain rounded forehead, short nose and moustache, flared pointed beard and three-pronged trident.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7de24ead-f89e-4e55-9f1f-a90902058d8e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/36-7de24ead-f89e-4e55-9f1f-a90902058d8e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bearded-poseidon-with-trident'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bearded', 'poseidon', 'with', 'trident')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('face',(4,20),[('A',(24,20),10,12,True),('L',(24,24)),('C',(24,31),(24,27),(24,29)),('L',(28,38)),('L',(20,35)),('L',(14,40)),('L',(8,35)),('L',(4,38)),('L',(6,31)),('C',(4,20),(4,28),(4,25))],True)
        
        poly('tines',(30,8),(37,19),(44,8));poly('shaft',(37,8),(37,19),(37,40));join('shaft','tines')
        poly('moustache',(13,25),(14,25),(15,25));line('nose',(14,18),(14,25));join('nose','moustache')
