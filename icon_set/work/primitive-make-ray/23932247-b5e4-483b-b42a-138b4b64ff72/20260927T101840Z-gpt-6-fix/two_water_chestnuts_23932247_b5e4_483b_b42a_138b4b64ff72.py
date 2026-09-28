"""Two Water Chestnuts.

Two broad water-chestnut bulbs with pointed top sprouts, separated rather than occluded. Centerline extremes (4,8)-(44,40); upper/lower placement deliberate. No useful local Lucide match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '23932247-b5e4-483b-b42a-138b4b64ff72'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-water-chestnuts/20260927T101610Z-thuan-mac-1/reference/water chesnut_23932247-b5e4-483b-b42a-138b4b64ff72.svg'
AUTHOR = 'gpt-6'

class TwoWaterChestnuts(Solo48):
    icon_id = 'two-water-chestnuts'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
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
    def build(self) -> None:
        """Unequal chestnut bulbs: a large pointed rear fruit and smaller lower fruit."""
        self.add_bezier('large-neck',(14,8),((16,13),(20,16),(20,19)))
        self.add_bezier('large-shoulder',(20,19),((23,20),(24,21),(24,23)))
        self.add_bezier('large-right',(24,23),((25,27),(24,31),(21,33)))
        self.add_bezier('large-bottom',(21,33),((20,38),(17,40),(14,40)))
        self.add_bezier('large-left-bottom',(14,40),((8,40),(4,35),(4,29)))
        self.add_bezier('large-left',(4,29),((4,24),(7,21),(9,18)))
        self.add_bezier('large-tip',(9,18),((12,15),(13,11),(14,8)))
        self.add_contour('large','large-neck','large-shoulder','large-right','large-bottom',
                         'large-left-bottom','large-left','large-tip',closed=True)
        self.add_line('small-stem',(37,22),(39,28))
        self.add_bezier('small-right-top',(39,28),((43,28),(44,30),(44,32)))
        self.add_bezier('small-right-bottom',(44,32),((44,37),(42,40),(38,40)))
        self.add_bezier('small-left-bottom',(38,40),((34,40),(32,38),(32,34)))
        self.add_bezier('small-left-top',(32,34),((32,30),(33,28),(37,22)))
        self.add_contour('small','small-stem','small-right-top','small-right-bottom',
                         'small-left-bottom','small-left-top',closed=True)
