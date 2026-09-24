"""Crossed Guitar and Microphone
Plan: Diagonal guitar crossing microphone
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide guitar body and narrow neck.
Reduction: Remove strings and sound hole; keep waist and mic capsule."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae731560-756d-4bfe-9aa1-bcd0df250afa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/party music_ae731560-756d-4bfe-9aa1-bcd0df250afa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-guitar-microphone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('guitar', 'microphone', 'music', 'instruments', 'performance', 'audio')

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
        path('guitar',(6,34),[('C',(16,24),(6,24),(12,30)),('L',(32,8)),('L',(40,16)),('L',(24,32)),('C',(14,42),(28,40),(14,42)),('A',(6,34),8,8,True)],True)
        path('mic',(6,14),[('C',(14,6),(6,6),(10,6)),('L',(20,12))]);path('mic-lower',(16,24),[('L',(6,14))]);self.relate('connect','mic-lower','mic');self.relate('connect','mic-lower','guitar')
        self.add_line('mic-handle',(28,28),(42,42));self.relate('connect','mic-handle','guitar')

        self.relate('connect','mic','guitar')

# Final review: Omit hidden microphone edge beneath guitar neck; retain visible microphone capsule, guitar waist and crossing handles.
