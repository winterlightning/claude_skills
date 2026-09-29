from pathlib import Path
import json, re, sys, textwrap, shutil
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
BATCH=Path(__file__).parent
ITEMS=json.loads((BATCH/'items.json').read_text())
AUTHOR='gpt-6'
# Each source identity and source path are preserved in ITEMS and emitted modules.
SOURCE_ICON_ID=[Path(i['reference']).stem[-36:] for i in ITEMS]
SOURCE_PATH=[i['reference'] for i in ITEMS]
HELPERS='''
    def path(self, name, start, *steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            member=f'{name}-{j}'
            if len(step)==2:
                self.add_line(member,here,step); end=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step;end=(x,y)
                self.add_arc(member,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            else:
                x,y,c1x,c1y,c2x,c2y=step;end=(x,y)
                self.add_bezier(member,here,((c1x,c1y),(c2x,c2y),end))
            members.append(member);here=end
        self.add_contour(name,*members,closed=closed)

    def ring(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),(x,y-ry,rx,ry,True),(x+rx,y,rx,ry,True),
                  (x,y+ry,rx,ry,True),(x-rx,y,rx,ry,True),closed=True)

    def rect(self,name,x,y,w,h,r=3):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),(x+w,y+h-r),
                  (x+w-r,y+h,r,r,True),(x+r,y+h),(x,y+h-r,r,r,True),
                  (x,y+r),(x+r,y,r,r,True),closed=True)

    def cups(self,top=24,bottom=44):
        # Mirrored open wrists, curved outside palms and rounded thumb pads.
        # Only hands are present: no detached head/body spacing applies.
        for side,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
            def a(x,y,rx,ry,sweep):return (*p(x,y),rx,ry,sweep if s==1 else not sweep)
            self.path(side+'-outer',p(11,bottom),c(4,top+10,11,bottom-5,4,top+15),p(4,top),
                      a(10,top,3,3,True),p(10,top+7))
            self.path(side+'-thumb',p(13,top+12),p(10,top+8),
                      c(14,top+4,6,top+4,11,top+1),p(19,top+10),
                      c(20,bottom-5,20,top+12,20,bottom-8),p(20,bottom))
            self.relate('connect',side+'-outer',side+'-thumb')
'''
D={}
def add(n,key,plan,wrong,change,body,ref='No useful exact Lucide brand match; shared geometric construction.'):
 D[n]=dict(keyshape=key,plan=plan,wrong=wrong,change=change,body=textwrap.dedent(body).strip(),construction=ref)
add(1,'SQUARE','Two diagonal, nested L-shaped outlined bands, each with shared cap and corner radii.',
 'The two bands were narrow, heavy hooks with cramped counters and unmatched proportions.',
 'Widened the bands, regularized rounded ends and elbows, and restored the diagonal nesting.', '''
for name,x,y,w,h in [('upper',20,6,22,23),('lower',10,23,17,19)]:
    r=5;right=x+w
    self.path(name,(x,y),(right-r,y),(right,y+r,r,r,True),(right,y+h-r),
              (right-10,y+h-r,5,5,True),(right-10,y+10),(x,y+10),
              (x,y,5,5,True),closed=True)
''')
add(2,'HRECT_M','Single-line G Pay wordmark, with a circular G, rounded P, open single-storey a and descending y.',
 'The reference wordmark had been stacked and its Pay characters reduced to blocky symbols.',
 'Restored the horizontal G Pay arrangement and curved letterforms; retained the compact wordmark envelope.', '''
self.path('g',(13,19),(9,17,12,17,10,17),(4,24,5,17,4,20),
          (9,31,4,28,5,31),(14,25,12,31,14,29),(10,25))
self.path('p',(21,31),(21,17),(25,17),(25,25,30,17,30,25),(21,25))
self.ring('a',33,27,3,4)
self.path('a-stem',(36,23),(36,27),(36,31))
self.relate('connect','a','a-stem')
self.path('y',(40,23),(43,30),(46,23))
self.path('y-tail',(43,30),(40,36))
self.relate('connect','y','y-tail')
''')
add(3,'HRECT_M','Circular G on the left, detached plus centered at the G crossbar on the right.',
 'The G was tall and uneven rather than circular; its opening and plus felt cramped.',
 'Rebuilt a balanced circular G and aligned plus, preserving the brand letter and clean opening.', '''
self.path('g',(27,14),(17,10,24,10,20,10),(4,24,9,10,4,16),
          (17,38,4,32,9,38),(30,24,25,38,30,32),(18,24))
self.path('plus-h',(38,24),(41,24),(44,24))
self.path('plus-v',(41,18),(41,24),(41,30))
self.relate('connect','plus-h','plus-v')
''')
add(4,'VRECT_L','Rounded page outline, folded top corner and two-column spreadsheet panel.',
 'The square page corners and missing fold seam made the document crude; table cells were crowded.',
 'Rounded the page, restored the corner fold, and opened an even two-by-two table.', '''
self.path('page',(12,4),(28,4),(40,16),(40,40),(36,44,4,4,True),(12,44),
          (8,40,4,4,True),(8,8),(12,4,4,4,True),closed=True)
self.path('fold',(28,4),(28,12),(32,16,4,4,False),(40,16))
self.relate('connect','page','fold')
self.path('table',(16,23),(24,23),(32,23),(32,30),(32,37),(24,37),(16,37),(16,30),(16,23),closed=True)
self.path('row',(16,30),(24,30),(32,30))
self.path('column',(24,23),(24,30),(24,37))
for a,b in [('table','row'),('table','column'),('row','column')]:self.relate('connect',a,b)
''','Lucide file-spreadsheet original and atomic-debug: rounded page and shared fold junctions.')
add(5,'SQUARE','Diagonal tag with rounded corners, eyelet at upper right and centered curved G.',
 'The tag pointed sideways, lacked its eyelet, and used a squared-off G.',
 'Restored the diagonal tag, round eyelet and curved G with separate clear counters.', '''
self.path('tag',(28,6),(38,6),(42,10,4,4,True),(42,21),
          (40,25,42,23,42,23),(23,42),(19,42,22,43,20,43),(6,29),
          (6,25,5,28,5,26),(24,8),(28,6,25,7,26,6),closed=True)
self.ring('eye',34,14,3)
self.path('g',(24,23),(19,22,22,21,20,21),(13,29,15,22,13,25),
          (20,36,13,33,16,36),(27,29,24,36,27,33),(21,29))
''')
add(6,'HRECT_L','Smooth oval bubble with a single low left-pointing tail; continuous tangent curves around oval.',
 'The lower oval flattened and the tail joined the bubble at a stiff inward kink.',
 'Rebalanced the oval and shaped a coherent tapered tail with smooth transitions.', '''
self.path('bubble',(4,22),(24,8,4,14,13,8),(44,22,35,8,44,14),
          (24,36,44,30,35,36),(17,35,21,36,19,36),(7,40),
          (10,31,9,36,11,33),(4,22,6,29,4,26),closed=True)
''','Lucide message-circle original and atomic-debug: continuous bubble contour and intentional tail.')
add(7,'CIRCLE','Circle with a left-high asymmetric wave dividing it; source asymmetry retained.',
 'The wave was flattened, joining the rim at cardinal points instead of reproducing its higher crest.',
 'Restored the higher flowing crest and lower right trough with smooth cubic transitions.', '''
self.path('rim',(4,24),(24,4,20,20,True),(44,24,20,20,True),
          (44,28,44,25,44,27),(24,44,43,38,34,44),(4,28,14,44,5,38),(4,24,4,27,4,25),closed=True)
self.path('wave',(4,28),(17,12,10,25,9,12),(32,25,25,12,25,21),(44,28,36,28,40,29))
self.relate('connect','rim','wave')
''')
add(8,'CIRCLE','Concentric circles, four diagonal spokes, central open loop; all radii shared.',
 'The identifying central loop was omitted and the ring structure became a generic lifebuoy.',
 'Restored the central open loop, diagonal spokes and three clear nested levels.', '''
for name,r in [('outer',20),('inner',12)]:self.ring(name,24,24,r)
# Diagonal spokes use exact integer nodes on the circular outlines (12,16 and 0,12 triangles).
for name,a,b in [('nw',(10,10),(16,16)),('ne',(38,10),(32,16)),('se',(38,38),(32,32)),('sw',(10,38),(16,32))]:
    self.add_line(name,a,b)
self.path('loop',(27,28),(24,19,32,23,29,19),(21,28,19,19,17,25))
''')
add(9,'VRECT_L','Tall left capsule and outlined flagged numeral one; distinct cap radii and shared band width.',
 'The numeral looked like a hooked blob and the two bars had inconsistent proportions.',
 'Rebuilt a long capsule and a clearly flagged numeral with smooth ends and an open interior.', '''
self.rect('bar',8,4,8,40,4)
self.path('one',(27,22),(24,24,25,24,24,24),(22,18,20,23,20,21),(34,10),
          (40,13,37,8,40,9),(40,40),(32,40,4,4,True),(32,21),(27,22),closed=True)
''')
add(10,'SQUARE','Central sphere above two mirrored cupped hands with curved palms and articulated thumbs.',
 'The hands had collapsed into four angular bars with no fingertip or palm silhouette.',
 'Restored mirrored rounded fingers, open wrists and thumb contours around a larger sphere.', '''
self.ring('sphere',24,15,11)
self.cups(24,44)
''','Human full_body_ref.png for rounded anatomy vocabulary; the supplied hand reference owns the pose.')
add(11,'VRECT_L','Clipboard with a rounded top clip and two hands gripping its sides; shared bilateral hand definition.',
 'The hands became zigzags and the clipboard lost its readable lines and grip.',
 'Restored rounded gripping hands, clipboard edges and two clean content lines.', '''
self.path('board',(12,8),(19,8),(29,8,5,5,True),(36,8),(36,25))
self.path('board-bottom',(14,39),(34,39))
self.add_line('text-1',(18,16),(30,16));self.add_line('text-2',(18,23),(28,23))
for side,s in [('left',1),('right',-1)]:
    def p(x,y):return (24+s*(x-24),y)
    def c(x,y,a,b,d,e):return (*p(x,y),*p(a,b),*p(d,e))
    self.path(side+'-edge',p(12,8),p(12,25))
    self.path(side+'-outer',p(5,43),p(5,30),c(12,20,5,25,9,23))
    self.path(side+'-grip',p(10,30),p(15,25),c(20,29,18,22,23,25),p(16,35),p(14,39),p(11,44))
    self.relate('connect',side+'-outer',side+'-edge')
self.relate('connect','board','left-edge');self.relate('connect','board','right-edge')
''','Lucide file-spreadsheet enclosure construction; supplied hand reference and human round-ended anatomy.')
add(12,'SQUARE','Diagonal puzzle piece above mirrored cupped hands, preserving its tab and inward socket.',
 'The puzzle became a tiny upright lump and the hands looked like hooks.',
 'Restored diagonal puzzle silhouette with a tab and socket, and redrew articulated cupped hands.', '''
self.path('piece',(16,13),(20,9),(23,12),(26,5,21,6,22,3),
          (29,12,33,3,34,10),(33,16),(29,20),
          (24,25,24,17,20,21),(20,29),(10,19),(14,15),
          (16,13,19,20,22,15),closed=True)
self.cups(28,44)
''','Human round-ended limb vocabulary; source diagonal puzzle and hand arrangement.')
add(13,'SQUARE','Heart between upper giving hand and lower open palm, with intentional diagonal movement.',
 'The lower hand was a heavy stack of strokes and the upper hand read as a floating hook.',
 'Redrew both hands as continuous open palms and placed a clear heart between them.', '''
self.path('heart',(23,21),(16,21,20,17,16,17),(23,29,14,23,18,26),
          (30,21,28,26,32,23),(23,21,30,17,26,17),closed=True)
self.path('lower',(4,33),(13,33),(20,38,17,33,19,36),(29,38),
          (37,44,34,38,36,41),(4,44))
self.add_line('palm',(15,38),(20,38));self.relate('connect','lower','palm')
self.path('upper',(44,4),(32,4),(24,10,28,4,25,7))
self.path('upper-thumb',(44,14),(39,14),(34,20),
          (29,16,30,24,26,19),(32,12),(28,10,31,9,30,9))
''','Lucide hand-heart original and atomic-debug: open palm, rounded thumb and legible heart.')
add(14,'SQUARE','Rounded pottery vessel with elliptical open rim above two mirrored sculpting hands.',
 'The pot rim was flattened and the hands consisted of disconnected vertical strokes.',
 'Restored an open oval rim, smooth pot belly and complete cupped hand contours.', '''
self.ring('rim',24,8,10,4)
self.path('pot',(14,8),(13,19,15,12,13,15),(24,30,13,26,18,30),
          (35,19,30,30,35,26),(34,8,35,15,33,12))
self.relate('connect','rim','pot')
self.cups(27,44)
''','Human full_body_ref.png rounded anatomy; reference vessel and mirrored hands.')
add(15,'SQUARE','Front-facing car supported above mirrored cupped hands; even wheels and sloped windshield.',
 'The car had dot-like wheels and no lamps, while the hands looked like curled stubs.',
 'Opened the windshield, restored tire shapes and paired lamps, and drew longer cupped hands.', '''
self.path('car',(11,15),(15,5),(33,5),(37,15),(37,23),(34,26,3,3,True),
          (14,26),(11,23,3,3,True),(11,15),closed=True)
self.path('windshield',(11,15),(37,15));self.relate('connect','car','windshield')
for name,x in [('left',15),('right',29)]:
    self.path(name+'-wheel',(x,26),(x,29),(x+4,29,2,2,False),(x+4,26))
    self.relate('connect','car',name+'-wheel')
    self.add_line(name+'-lamp',(x,21),(x+4,21))
self.cups(33,44)
''','Supplied front-car proportions and human round-ended anatomy; original mirrored hands.')
# Handshake plan derived from source and Lucide, independently parameterized cuffs and shared clasp.
for n,kind in [(16,'short'),(17,'shirt'),(18,'compact')]:
 add(n,'HRECT_M','Two overlapping palms with a rounded thumb, two finger turns and paired '+kind+' cuffs.',
 'The clasp had oversized hooks, angular palms and lost finger/cuff structure.',
 'Rebuilt a natural overlapping thumb and smooth joined fingers with matched '+kind+' cuffs.', '''
self.path('left-cuff',(4,12),(9,12),(9,17),(9,29),(9,32),(4,32))
self.path('right-cuff',(44,12),(39,12),(39,17),(39,29),(39,32),(44,32))
self.path('left-top',(9,17),(18,13,12,17,15,13),(23,14,20,13,21,13))
self.path('thumb',(39,17),(28,12),(23,14,26,11,25,12),(18,18),
          (21,24,13,22,17,27),(27,21))
self.path('fingers',(27,21),(35,29),(31,34,38,32,34,36),(27,30),
          (23,37,31,35,27,41),(19,33),
          (15,36,20,37,18,39),(9,29))
self.path('right-palm',(39,29),(35,29))
for a,b in [('left-cuff','left-top'),('left-top','thumb'),('thumb','right-cuff'),('thumb','fingers'),
            ('fingers','left-cuff'),('fingers','right-palm'),('right-palm','right-cuff')]:self.relate('connect',a,b)
''','Lucide handshake original and atomic-debug: overlapping thumb, tangent finger curls and paired cuffs.')
# Subtle distinctions taken from cuff lengths in sources.
D[17]['body']=D[17]['body'].replace('(4,12)','(4,10)').replace('(9,12)','(9,10)').replace('(4,32)','(4,34)').replace('(9,32)','(9,34)').replace('(44,12)','(44,10)').replace('(39,12)','(39,10)').replace('(44,32)','(44,34)').replace('(39,32)','(39,34)')
D[18]['body']=D[18]['body'].replace('(4,12)','(4,14)').replace('(9,12)','(9,14)').replace('(44,12)','(44,14)').replace('(39,12)','(39,14)')
add(19,'SQUARE','Diagonal straight handle joins flared axe blade; circular cutting edge and curved blade shoulders.',
 'The handle was bent and tapered into a polygon; the blade had abrupt shoulder kinks.',
 'Restored a straight parallel handle with rounded butt and a smoothly flared cutting head.', '''
self.path('head',(22,6),(15,13),(19,17),(25,23),(29,34,28,26,29,30),
          (42,21,37,32,40,27),(31,17,38,20,34,19),(22,6),closed=True)
self.path('handle',(19,17),(5,35),(11,41,2,40,7,44),(25,23))
self.relate('connect','head','handle')
''','Lucide axe original and atomic-debug: parallel diagonal handle and curved flared blade.')
add(20,'SQUARE','Rounded frame holding lowercase h, a separate upper accent and a right-pointing triangle at the stem foot.',
 'The small arrow was missing and the accent had collapsed into a dot-like stroke.',
 'Restored the arrow and distinct slanted accent with a smooth h shoulder inside a regular frame.', '''
self.rect('frame',6,4,36,40,4)
self.path('stem',(16,11),(16,26),(16,37))
self.path('h',(16,26),(26,23,21,24,24,23),(33,29,31,23,33,25),(33,37))
self.relate('connect','stem','h')
self.path('arrow',(16,37),(23,33),(16,29));self.relate('connect','stem','arrow')
self.path('accent',(29,16),(32,10),(36,10),(33,15,36,13,35,15),(29,16),closed=True)
''')

def create(n,revision=1,body=None):
 it=ITEMS[n-1];d=D[n];uuid=Path(it['reference']).stem[-36:];concept=Path(it['reference']).stem[:-37]
 run=ROOT/'icon_set/work/primitive-make-ray'/uuid/f'20260928T173050Z-fix-{n:02}-r{revision}'
 run.mkdir(parents=True,exist_ok=False)
 metadata=dict(concept=concept,source_uuid=uuid,reference_path=it['reference'],icon_id=it['icon_id'],author=AUTHOR)
 (run/(it['icon_id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
 (run/'review-before.md').write_text(f"Reference: {it['reference']}\nRejected: {it['before']}\n\nObserved: {d['wrong']}\n\nReviewer: {it['feedback']}\n\nRevision: {d['change']}\n\nConstruction: {d['construction']}\n")
 module=run/(it['icon_id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
 code=f'''"""{d['plan']}\nKeyshape: {d['keyshape']}. Uniform 4px SOLO48 stroke.\nConstruction: {d['construction']}\nRevision: {d['change']}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uuid!r}\nSOURCE_PATH = {it['reference']!r}\nAUTHOR = 'gpt-6'\n\nclass Drawing(Solo48):\n    icon_id = {it['icon_id']!r}\n    keyshape = Keyshape.{d['keyshape']}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = {'logos' if n<10 or n==20 else 'objects'!r}\n    aliases = ()\n    keywords = {tuple(it['icon_id'].split('-'))!r}\n\n    def build(self):\n'''
 code+=textwrap.indent(body or d['body'],'        ')+'\n'+HELPERS
 module.write_text(code)
 return run,module
if __name__=='__main__':
 runs=[]
 for n in range(1,21):
  run,module=create(n);runs.append(dict(n=n,run=str(run.relative_to(ROOT)),module=str(module.relative_to(ROOT))))
 (BATCH/'runs.json').write_text(json.dumps(runs,indent=2))
 print('Created',len(runs),'fresh standalone modules')
