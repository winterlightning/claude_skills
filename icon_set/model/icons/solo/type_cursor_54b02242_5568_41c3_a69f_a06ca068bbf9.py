from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='54b02242-5568-41c3-a69f-a06ca068bbf9'
SOURCE_PATH='icon_set/work/todo-references/type cursor_54b02242-5568-41c3-a69f-a06ca068bbf9.svg'
AUTHOR='gpt-6'
PLAN='Rounded text input crossed by a tall cursor with a curved lower hook.'
CONSTRUCTION_REFERENCE='text-cursor-input: rounded field and cursor crossing the field'

class Drawing(Solo48):
    icon_id='type-cursor'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('type', 'cursor')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,left,top,right,bottom,r):
        p=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
           (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        names=[]
        for i,start in enumerate(p):
            n=f'{name}-{i}';end=p[(i+1)%8]
            if i%2:self.add_arc(n,start,end,radius_x=r)
            else:self.add_line(n,start,end)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def cross(self,name,x,y,r,diagonal=False):
        ends=[(-r,-r),(r,r),(r,-r),(-r,r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        for i,(dx,dy) in enumerate(ends):self.add_line(f'{name}-{i}',(x,y),(x+dx,y+dy))
        self.relate('connect',*[f'{name}-{i}' for i in range(4)])

    def monitor(self,left=6,top=6,right=42,bottom=34,foot=42):
        # Matched quarter-round corners, bottom wall split at the stand junction.
        r=4;cx=(left+right)//2
        self.add_line('screen-top',(left+r,top),(right-r,top))
        self.add_arc('screen-tr',(right-r,top),(right,top+r),radius_x=r)
        self.add_line('screen-right',(right,top+r),(right,bottom-r))
        self.add_arc('screen-br',(right,bottom-r),(right-r,bottom),radius_x=r)
        self.add_line('screen-bottom-r',(right-r,bottom),(cx,bottom))
        self.add_line('screen-bottom-l',(cx,bottom),(left+r,bottom))
        self.add_arc('screen-bl',(left+r,bottom),(left,bottom-r),radius_x=r)
        self.add_line('screen-left',(left,bottom-r),(left,top+r))
        self.add_arc('screen-tl',(left,top+r),(left+r,top),radius_x=r)
        self.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-r','screen-bottom-l','screen-bl','screen-left','screen-tl',closed=True)
        self.add_line('stand',(cx,bottom),(cx,foot))
        self.add_polyline('foot',(cx-8,foot),(cx,foot),(cx+8,foot))
        self.relate('connect','stand','screen-bottom-r','screen-bottom-l')
        self.relate('connect','stand','foot')

    def browser(self):
        # Chrome separator joins explicitly split side walls; two tiny source
        # chrome dashes are omitted so the content keeps the available height.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-upper',(42,10),(42,14))
        self.add_line('right-lower',(42,14),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left-lower',(6,38),(6,14))
        self.add_line('left-upper',(6,14),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('browser','top','tr','right-upper','right-lower','br','bottom','bl','left-lower','left-upper','tl',closed=True)
        self.add_line('chrome',(6,14),(42,14))
        self.relate('connect','chrome','left-upper','left-lower','right-upper','right-lower')

    def build(self):
        # Split both horizontal field walls where the cursor passes through them.
        self.add_polyline('field-top',(8,16),(34,16),(40,16))
        self.add_arc('field-tr',(40,16),(44,20),radius_x=4)
        self.add_line('field-right',(44,20),(44,28))
        self.add_arc('field-br',(44,28),(40,32),radius_x=4)
        self.add_polyline('field-bottom',(40,32),(34,32),(8,32))
        self.add_arc('field-bl',(8,32),(4,28),radius_x=4)
        self.add_line('field-left',(4,28),(4,20))
        self.add_arc('field-tl',(4,20),(8,16),radius_x=4)
        self.add_contour('field','field-top-1','field-top-2','field-tr','field-right','field-br','field-bottom-1','field-bottom-2','field-bl','field-left','field-tl',closed=True)
        self.add_polyline('cursor',(34,8),(34,16),(34,32),(34,34))
        self.add_arc('hook',(34,34),(28,40),radius_x=6)
        self.relate('connect','cursor','field-top-1','field-top-2','field-bottom-1','field-bottom-2','hook')
        self.contours = [c for c in self.contours if c.contour_id not in ['field-top', 'field-bottom']]
