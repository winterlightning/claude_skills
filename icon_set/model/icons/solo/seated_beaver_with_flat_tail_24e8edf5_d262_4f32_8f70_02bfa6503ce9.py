"""Seated Beaver with Flat Tail
Plan: Seated right-facing beaver and broad flat tail.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Small eye and interior forepaw strokes omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24e8edf5-d262-4f32-8f70-02bfa6503ce9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beaver_24e8edf5-d262-4f32-8f70-02bfa6503ce9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-beaver-with-flat-tail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('beaver', 'rodent', 'animal', 'tail', 'seated', 'wildlife', 'mammal')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('beaver',(14,32),[('C',(10,21),(10,29),(10,24)),('C',(28,14),(10,11),(21,14)),('C',(32,8),(28,10),(29,8)),('C',(36,12),(35,8),(36,10)),('C',(44,20),(41,13),(44,16)),('L',(37,24)),('L',(35,32)),('L',(40,32)),('L',(40,40)),('L',(22,40)),('C',(14,32),(18,40),(14,37))],True)
        path('tail',(14,32),[('L',(8,32)),('A',(8,40),4,4,False),('L',(22,40))]);self.relate('connect','tail','beaver')
