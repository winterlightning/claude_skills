"""Two Cookies in a Small Bowl.

Bowl with two overlapping cookie domes; centerline extremes (4,8)-(44,40). Lucide cookie contributes simple rounded mass; omit crowded crumb strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8eef550-2ab3-4736-80d5-010f20e00309'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear cookies_d8eef550-2ab3-4736-80d5-010f20e00309.svg'
AUTHOR = 'gpt-6'

class TwoCookiesSmallBowl(Solo48):
    icon_id = 'two-cookies-small-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'cookies', 'in', 'a', 'small', 'bowl')

    def build(self):
        # Symbol plan: Bowl with two overlapping cookie domes; centerline extremes (4,8)-(44,40). Lucide cookie contributes simple rounded mass; omit crowded crumb strokes.

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

        path('bowl',(4,28),[('L',(10,28)),('L',(24,28)),('L',(40,28)),('L',(44,28)),('C',(24,40),(44,36),(34,40)),('C',(4,28),(14,40),(4,36))],True)
        path('rear-cookie',(10,28),[('C',(16,8),(4,17),(7,8)),('C',(28,12),(22,8),(25,10))])
        path('front-cookie',(24,28),[('C',(28,12),(17,23),(19,12)),('C',(40,28),(38,12),(43,20))])
        join('rear-cookie','front-cookie');join('rear-cookie','bowl');join('front-cookie','bowl')
