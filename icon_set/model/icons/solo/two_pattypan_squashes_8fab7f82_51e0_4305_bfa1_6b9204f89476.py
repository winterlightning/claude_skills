"""Two Pattypan Squashes.

Two scalloped squat squash outlines in a diagonal pair, with short attached stems. Shared scallop construction translated for each squash. Centerline extremes (6,6)-(42,42). Drop ribs to keep clear scallops; no useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fab7f82-51e0-4305-bfa1-6b9204f89476'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/patty pan squashes_8fab7f82-51e0-4305-bfa1-6b9204f89476.svg'
AUTHOR = 'gpt-6'

class TwoPattypanSquashes(Solo48):
    icon_id = 'two-pattypan-squashes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'pattypan', 'squashes')

    def build(self):
        # Symbol plan: Two scalloped squat squash outlines in a diagonal pair, with short attached stems. Shared scallop construction translated for each squash. Centerline extremes (6,6)-(42,42). Drop ribs to keep clear scallops; no useful local Lucide match.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        for i,(x,y) in enumerate(((28,13),(16,34))):
            depth=6 if i==0 else 8
            path(f'squash-{i}',(x,y-4),[('C',(x+8,y-4),(x+3,y-7),(x+7,y-7)),('C',(x+14,y),(x+10,y-2),(x+14,y-3)),('C',(x+8,y+6),(x+14,y+4),(x+11,y+5)),('C',(x,y+depth),(x+6,y+depth),(x+3,y+depth)),('C',(x-10,y+2),(x-7,y+depth),(x-10,y+6)),('C',(x-6,y-4),(x-10,y-2),(x-9,y-4)),('C',(x,y-4),(x-3,y-4),(x-2,y-2))],True)
            line(f'stem-{i}',(x,y-4),(x-2,y-(7 if i==0 else 8)));join(f'stem-{i}',f'squash-{i}')
