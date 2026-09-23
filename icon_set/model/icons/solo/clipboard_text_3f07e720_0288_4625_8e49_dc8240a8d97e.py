"""clipboard text: complete reference reconstructed on SOLO48.
Keyshape: VRECT_L, visible bounds (6, 2, 42, 46).
Construction reference: clipboard. See build comments for symbols and relationships.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3f07e720-0288-4625-8e49-dc8240a8d97e'
SOURCE_PATH = 'icon_set/work/todo-references/clipboard text_3f07e720-0288-4625-8e49-dc8240a8d97e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clipboard-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('clipboard', 'text')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def rounded_rect(self, name, x, y, w, h, r):
        nodes=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=nodes[i],nodes[(i+1)%8]; eid=f'{name}-{i}';members.append(eid)
            if i%2:self.add_arc(eid,a,b,radius_x=r)
            else:self.add_line(eid,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Page sides terminate at the separate top clip; corners share one radius.
        self.add_line('page-tl',(16,12),(12,12))
        self.add_arc('page-lt',(12,12),(8,16),radius_x=4,sweep=False)
        self.add_line('page-left',(8,16),(8,40))
        self.add_arc('page-bl',(8,40),(12,44),radius_x=4,sweep=False)
        self.add_line('page-bottom',(12,44),(36,44))
        self.add_arc('page-br',(36,44),(40,40),radius_x=4,sweep=False)
        self.add_line('page-right',(40,40),(40,16))
        self.add_arc('page-tr',(40,16),(36,12),radius_x=4,sweep=False)
        self.add_line('page-top',(36,12),(32,12))
        self.add_contour('page','page-tl','page-lt','page-left','page-bl','page-bottom','page-br','page-right','page-tr','page-top')
        # Raised dome tab; tiny shoulders reduced to preserve the clip opening.
        self.add_polyline('clip-bottom',(16,12),(16,16),(32,16),(32,12))
        self.add_arc('clip-dome',(32,12),(16,12),radius_x=8,sweep=False)
        self.relate('connect','clip-bottom','clip-dome')
        self.relate('connect','page','clip-bottom')
        self.relate('connect','page','clip-dome')
        for i,(end,y) in enumerate(((31,25),(26,35))):
            self.add_line('text-'+str(i),(17,y),(end,y))
