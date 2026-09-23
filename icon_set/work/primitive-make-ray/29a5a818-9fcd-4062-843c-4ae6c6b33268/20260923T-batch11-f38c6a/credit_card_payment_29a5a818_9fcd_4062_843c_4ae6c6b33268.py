"""credit card payment. Reconstructed whole reference on SOLO48.
Plan: HRECT_L visible bounds (2, 6, 46, 42).
Construction: credit-card. Shared dimensions and relationships are recorded in build.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '29a5a818-9fcd-4062-843c-4ae6c6b33268'
SOURCE_PATH = 'icon_set/work/todo-references/credit card payment_29a5a818-9fcd-4062-843c-4ae6c6b33268.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'credit-card-payment'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('credit', 'card', 'payment')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8];eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Left terminal and receipt; right detached card above insertion arrow.
        self.add_line('terminal-tl',(10,16),(7,16))
        self.add_arc('terminal-lt',(7,16),(4,19),radius_x=3,sweep=False)
        self.add_line('terminal-left',(4,19),(4,37))
        self.add_arc('terminal-bl',(4,37),(7,40),radius_x=3,sweep=False)
        self.add_line('terminal-bottom',(7,40),(23,40))
        self.add_arc('terminal-br',(23,40),(26,37),radius_x=3,sweep=False)
        self.add_line('terminal-right',(26,37),(26,19))
        self.add_arc('terminal-tr',(26,19),(23,16),radius_x=3,sweep=False)
        self.add_line('terminal-top',(23,16),(22,16))
        self.add_contour('terminal','terminal-tl','terminal-lt','terminal-left','terminal-bl','terminal-bottom','terminal-br','terminal-right','terminal-tr','terminal-top')
        self.add_polyline('receipt',(10,24),(10,8),(13,10),(16,8),(19,10),(22,8),(22,24))
        self.relate('connect','terminal','receipt')
        self.add_line('slot',(4,24),(26,24))
        self.relate('connect','terminal','slot')
        self.relate('connect','receipt','slot')
        for row,y in enumerate((30,36)):
            for col,x in enumerate((10,18)):
                self.add_line(f'key-{row}-{col}',(x,y),(x+2,y))
        self.rounded_rect('card',34,8,10,16,2)
        self.add_line('stripe',(39,8),(39,24))
        self.relate('connect','card','stripe')
        self.add_line('shaft',(39,32),(39,40))
        self.add_polyline('arrow',(35,36),(39,40),(43,36))
        self.relate('connect','shaft','arrow')

