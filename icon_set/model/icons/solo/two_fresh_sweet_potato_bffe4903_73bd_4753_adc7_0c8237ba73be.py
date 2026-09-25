"""Two Fresh Sweet Potatoes.

Two taper-ended tubers separated vertically, with broad organic bodies. Centerline extremes (4,8)-(44,40). Preserve natural asymmetry; omit small skin creases and replace overlap with clearance. No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bffe4903-73bd-4753-adc7-0c8237ba73be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/sweet potato yam_bffe4903-73bd-4753-adc7-0c8237ba73be.svg'
AUTHOR = 'gpt-6'

class TwoFreshSweetPotato(Solo48):
    icon_id = 'two-fresh-sweet-potato'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('two', 'fresh', 'sweet', 'potatoes')

    def build(self):
        # Symbol plan: Two taper-ended tubers separated vertically, with broad organic bodies. Centerline extremes (4,8)-(44,40). Preserve natural asymmetry; omit small skin creases and replace overlap with clearance. No useful local Lucide match.

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

        path('upper-tuber',(12,14),[('C',(26,8),(16,10),(20,8)),('C',(44,16),(34,8),(40,12)),('C',(28,22),(40,19),(34,22)),('C',(12,14),(20,22),(15,18))],True)
        path('lower-tuber',(4,34),[('C',(18,30),(8,31),(13,30)),('C',(36,34),(26,30),(31,31)),('C',(18,40),(32,37),(26,40)),('C',(4,34),(12,40),(7,37))],True)
