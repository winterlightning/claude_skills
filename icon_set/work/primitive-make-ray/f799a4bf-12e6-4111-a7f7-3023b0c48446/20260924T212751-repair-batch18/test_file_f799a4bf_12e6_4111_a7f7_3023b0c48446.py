"""A clipped-corner test page with A and B and answer dashes.
Symbol plan and construction: file-text: clipped page corner and separate content rows.
Keyshape: VRECT_L reserves maximum height for the two letter rows.
Omissions: A apex rounded and answer dashes shortened; both letters and both rows retained.
Review: Blocked: B counters close at native size. Page/B, A/answer and B/answer spacing, undersized holes, pinches and internal A clearance remain. Six candidates saved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f799a4bf-12e6-4111-a7f7-3023b0c48446'
SOURCE_PATH = 'pictographic-primitives/other/test file_f799a4bf-12e6-4111-a7f7-3023b0c48446.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'test-file'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('test', 'file')

    def path(self, name, start, operations, closed=False):
        # A coherent path owns its members exactly once.
        current=start; members=[]
        for i,op in enumerate(operations):
            n=f'{name}-{i}'
            if op[0]=='L':
                end=op[1]; self.add_line(n,current,end)
            elif op[0]=='A':
                end,rx,ry,sweep=op[1:]; self.add_arc(n,current,end,radius_x=rx,radius_y=ry,sweep=sweep)
            else:
                c1,c2,end=op[1:]; self.add_bezier(n,current,(c1,c2,end))
            members.append(n);current=end
        if closed and current!=start:
            n=f'{name}-close';self.add_line(n,current,start);members.append(n)
        self.add_contour(name,*members,closed=closed)






    def build(self):
        # Final fit: preserve A above B and both answer dashes. No rules waived.
        self.path('page',(12,4),[('L',(30,4)),('L',(40,14)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.add_polyline('a-left',(17,24),(17,22),(17,18))
        self.add_arc('a-cap',(17,18),(25,18),radius_x=4)
        self.add_polyline('a-right',(25,18),(25,22),(25,24))
        self.add_line('a-bar',(17,22),(25,22))
        for n in ['a-left','a-right']:
            self.relate('connect',n,'a-cap');self.relate('connect',n,'a-bar')
        self.add_polyline('b-stem',(17,32),(17,36),(17,40))
        self.add_arc('b-upper',(17,32),(17,36),radius_x=7,radius_y=2)
        self.add_arc('b-lower',(17,36),(17,40),radius_x=7,radius_y=2)
        self.relate('connect','b-stem','b-upper','b-lower')
        for i,y in enumerate((20,36)):self.add_line(f'answer-{i}',(31,y),(32,y))
