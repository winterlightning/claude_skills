"""Smiling Face Hugging Ribboned Gift
Plan: Round smiling face embraces a ribboned gift.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide gift: box/ribbon topology; full original physical group.
Reduction: Bow loops and mouth require spacing review."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4de1746e-1e17-4608-9148-82107fed5099'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/emoji gift lover hug 1_4de1746e-1e17-4608-9148-82107fed5099.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-face-hugging-ribboned-gift'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('emoji', 'gift', 'box', 'ribbon', 'hug', 'smile', 'face')

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
        path('face',(6,24),[('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(32,37),(42,31),(39,35))])
        self.add_polyline('gift',(6,29),(24,22),(32,40),(14,42),closed=True)
        self.add_line('ribbon',(15,26),(23,41));self.relate('connect','ribbon','gift')
        path('arm',(32,37),[('C',(23,38),(27,30),(19,36)),('C',(39,29),(27,43),(37,35))]);self.relate('connect','arm','face');self.relate('connect','arm','gift')
        for x in (19,29):path(f'eye-{x}',(x-2,17),[('C',(x+2,17),(x-1,13),(x+1,13))])
