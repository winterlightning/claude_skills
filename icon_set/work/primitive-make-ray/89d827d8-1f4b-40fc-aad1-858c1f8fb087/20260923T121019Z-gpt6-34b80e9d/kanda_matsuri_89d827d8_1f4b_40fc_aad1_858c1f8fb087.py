from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '89d827d8-1f4b-40fc-aad1-858c1f8fb087'
SOURCE_PATH = 'icon_set/work/todo-references/kanda matsuri_89d827d8-1f4b-40fc-aad1-858c1f8fb087.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A Kanda Matsuri festival crest with three inward-facing rounded lobes and lower hanging strokes.'
CONSTRUCTION_PLAN = 'Retain the crest arrangement and circular border; no useful direct Lucide subject match.'
# Keyshape extremes are fixed by SOLO48; all geometry authored directly at 48.

def circle(icon, name, cx, cy, radius):
    icon.add_arc(name+'-a', (cx-radius,cy), (cx+radius,cy), radius_x=radius)
    icon.add_arc(name+'-b', (cx+radius,cy), (cx-radius,cy), radius_x=radius)
    icon.add_contour(name, name+'-a', name+'-b', closed=True)

def rounded_rect(icon, name, left, top, right, bottom, radius=4):
    r=radius
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
    members=[]
    for i,start in enumerate(points):
        end=points[(i+1)%8]; member=f'{name}-{i}'; members.append(member)
        if i%2: icon.add_arc(member,start,end,radius_x=r)
        else: icon.add_line(member,start,end)
    icon.add_contour(name,*members,closed=True)

class Drawing(Solo48):
    icon_id = 'kanda-matsuri'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('kanda', 'matsuri')

    def build(self):
        circle(self,'crest',24,20,16)
        self.add_line('top-spoke',(24,4),(24,11))
        self.add_bezier('top-lobe',(24,18),((9,11),(19,6),(24,11)),((29,6),(39,11),(24,18)))
        self.add_line('left-spoke',(10,28),(16,27))
        self.add_bezier('left-lobe',(22,23),((22,40),(12,32),(16,27)),((5,23),(12,15),(22,23)))
        self.add_line('right-spoke',(38,28),(32,27))
        self.add_bezier('right-lobe',(26,23),((26,40),(36,32),(32,27)),((43,23),(36,15),(26,23)))
        self.relate('connect','crest','top-spoke')
        self.relate('connect','top-spoke','top-lobe')
        self.relate('connect','left-spoke','left-lobe')
        self.relate('connect','right-spoke','right-lobe')
        for name,x,dx in [('left',8,4),('right',40,-4)]:
            self.add_line(name+'-fringe',(x,38),(x+dx,44))
        self.add_line('middle-fringe',(24,42),(24,44))

KEYSHAPE_CENTERLINE_BOUNDS = [8, 4, 40, 44]
