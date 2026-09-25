"""Businessman Hailing Taxi.

Plan: Headr5 at24,11, torso y24..42 exact gap8; raised left arm, right hand above small case.
Construction: Human full_body_ref.png: torso-aligned head and coherent action limbs.
Reduction: Omitted small briefcase handle and body outline; hand meets case top.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '459ca9bc-41c3-44a7-bd18-4322e40df660'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/21-459ca9bc-41c3-44a7-bd18-4322e40df660.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'briefcase-carrying-hailing-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('briefcase', 'carrying', 'hailing', 'person')

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
        circle('head',24,11,5)
        line('torso',(24,24),(24,42));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        poly('raised-arm',(24,24),(16,24),(6,10));join('raised-arm','torso')
        poly('carrying-arm',(24,24),(37,24),(37,34));join('carrying-arm','torso')
        rect('case',32,34,10,8,2);join('case','carrying-arm')
