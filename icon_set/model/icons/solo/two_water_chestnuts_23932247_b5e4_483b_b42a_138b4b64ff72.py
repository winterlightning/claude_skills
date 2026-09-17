"""Two Water Chestnuts.

Two broad water-chestnut bulbs with pointed top sprouts, separated rather than occluded. Centerline extremes (4,8)-(44,40); upper/lower placement deliberate. No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23932247-b5e4-483b-b42a-138b4b64ff72'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/water chesnut_23932247-b5e4-483b-b42a-138b4b64ff72.svg'
AUTHOR = 'gpt-6'

class TwoWaterChestnuts(Solo48):
    icon_id = 'two-water-chestnuts'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'water', 'chestnuts')

    def build(self):
        # Symbol plan: Two broad water-chestnut bulbs with pointed top sprouts, separated rather than occluded. Centerline extremes (4,8)-(44,40); upper/lower placement deliberate. No useful local Lucide match.

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

        path('rear-bulb',(10,14),[('L',(12,8)),('L',(16,14)),('C',(22,21),(20,14),(22,16)),('C',(14,25),(22,25),(18,25)),('C',(4,20),(7,25),(4,24)),('C',(10,14),(4,16),(7,14))],True)
        path('front-bulb',(30,29),[('L',(32,23)),('L',(36,29)),('C',(44,35),(41,29),(44,31)),('C',(34,40),(44,39),(40,40)),('C',(26,35),(29,40),(26,39)),('C',(30,29),(26,31),(28,29))],True)
