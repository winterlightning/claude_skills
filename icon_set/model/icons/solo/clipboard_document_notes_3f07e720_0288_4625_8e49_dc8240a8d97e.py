from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f07e720-0288-4625-8e49-dc8240a8d97e'
SOURCE_PATH = 'pictographic-primitives/other/clipboard text_3f07e720-0288-4625-8e49-dc8240a8d97e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clipboard-document-notes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('clipboard', 'document', 'notes')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rounded_rect(self, name, x0, y0, x1, y1, r):
        pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}'
            a,b=pts[i],pts[(i+1)%8]
            if i%2: self.add_arc(eid,a,b,radius_x=r)
            else: self.add_line(eid,a,b)
            ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: vertically symmetric board and domed clip share side endpoints; two note rules share left margin.
        # VRECT_L centerlines (8,4)-(40,44).
        left=[(16,12),(16,10),(20,10),(20,8)]
        for i,(a,b) in enumerate(zip(left,left[1:]),1): self.add_line(f'clip-left-{i}',a,b)
        self.add_arc('clip-dome',(20,8),(28,8),radius_x=4)
        right=[(28,8),(28,10),(32,10),(32,12),(32,18),(16,18),(16,12)]
        for i,(a,b) in enumerate(zip(right,right[1:]),1): self.add_line(f'clip-right-{i}',a,b)
        # Merge primitive members into a single clip path.
        self.add_contour('clip','clip-left-1','clip-left-2','clip-left-3','clip-dome',
                         'clip-right-1','clip-right-2','clip-right-3','clip-right-4','clip-right-5','clip-right-6',closed=True)
        self.add_line('board-tl',(16,12),(12,12))
        self.add_arc('board-ul',(12,12),(8,16),radius_x=4,sweep=False)
        self.add_line('board-left',(8,16),(8,40))
        self.add_arc('board-bl',(8,40),(12,44),radius_x=4,sweep=False)
        self.add_line('board-bottom',(12,44),(36,44))
        self.add_arc('board-br',(36,44),(40,40),radius_x=4,sweep=False)
        self.add_line('board-right',(40,40),(40,16))
        self.add_arc('board-ur',(40,16),(36,12),radius_x=4,sweep=False)
        self.add_line('board-tr',(36,12),(32,12))
        self.add_contour('board','board-tl','board-ul','board-left','board-bl','board-bottom','board-br','board-right','board-ur','board-tr')
        self.relate('connect','board','clip')
        for i,(y,end) in enumerate(((27,30),(35,26))):
            self.add_line(f'note-{i}',(18,y),(end,y))
