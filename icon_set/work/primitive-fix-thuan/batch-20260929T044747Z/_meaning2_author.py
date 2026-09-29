from pathlib import Path
import json,sys,textwrap,re,io
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T044747Z');claims=json.loads((B/'claims.json').read_text())
# The same public geometry helpers are retained; all subjects below are newly authored.
old=Path('/tmp/meaning_batch_author.py').read_text();helpers=old.split("helpers='''",1)[1].split("'''",1)[0]
specs={}
def add(i,key,why,body,omit='Secondary source detail simplified only where needed for 48 px legibility.',ref='No useful Lucide subject match; original reference establishes silhouette and arrangement.'):
 specs[i]=dict(keyshape=key,comparison=why,body=textwrap.dedent(body).strip(),omissions=omit,construction=ref)
add(0,'VRECT_L','The rejected page has square corners and loses the lower caption rule. Restore a rounded clipped-corner page, readable clock and baseline.', '''
self.path('page',(12,4),[('L',(32,4)),('L',(40,12)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
self.circle('clock',24,21,8)
self.add_polyline('hands',(24,16),(24,21),(28,21))
self.add_line('caption',(16,36),(32,36))
''')
add(1,'VRECT_L','Rejected diagonal marks merge into the frame and the person becomes two small marks. Restore four independent right-angle focus brackets around a head and shoulder bust.', '''
self.box('frame',8,4,40,44,4)
self.circle('head',24,18,3)
self.path('shoulders',(18,33),[('L',(18,32)),('C',(24,29),(18,30),(21,29)),('C',(30,32),(27,29),(30,30)),('L',(30,33))])
for n,points in enumerate((((14,16),(14,11),(19,11)),((29,11),(34,11),(34,16)),((14,32),(14,37),(19,37)),((29,37),(34,37),(34,32)))):self.add_polyline(f'focus-{n}',*points)
''')
add(2,'SQUARE','Rejected short hooked ribbon and angular limbs lose the flowing running action. Restore a waved ribbon, an aligned head, outstretched arms and bent running legs.', '''
self.circle('head',29,11,5)
self.add_bezier('torso',(24,23),((23,25),(22,28),(20,30)))
self.add_polyline('arm-front',(24,23),(33,27),(42,20))
self.add_polyline('arm-back',(24,23),(16,22),(9,28))
self.add_polyline('leg-back',(20,30),(13,39),(6,36))
self.add_polyline('leg-front',(20,30),(31,33),(37,42))
self.path('ribbon',(6,7),[('C',(12,14),(10,7),(8,14)),('C',(18,7),(17,14),(14,7)),('C',(21,9),(20,7),(19,9))])
self.relate('connect','torso','arm-front','arm-back','leg-back','leg-front')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''',ref='Shared full_body_ref.png and approved approaching-ball head alignment: circular head, coherent limbs and analytically exact detached head gap.')
add(3,'SQUARE','Rejected face is an open C-shaped notch with disconnected wind dots. Restore the forehead, nose, lips, chin and neck, plus two continuous outward breath curls.', '''
self.path('profile',(10,42),[('L',(10,35)),('C',(6,23),(10,31),(6,28)),('C',(19,6),(6,13),(10,6)),('C',(33,21),(28,6),(33,12)),('L',(34,25)),('L',(30,25)),('L',(30,29)),('L',(26,29)),('C',(26,34),(22,29),(22,34)),('L',(29,34)),('C',(22,39),(29,38),(26,39)),('L',(22,42))])
self.path('breath-top',(34,31),[('L',(40,31)),('A',(40,25),3,3,False)])
self.path('breath-bottom',(34,38),[('C',(40,42),(40,37),(43,40)),('L',(38,42))])
''')
# Finger contours carry natural stepped finger lengths; no small side bumps.
add(5,'HRECT_L','Rejected three tiny bumps no longer read as curled fingers. Restore a long index, raised thumb and three broad rounded folded-finger levels.', '''
self.path('palm',(24,17),[('C',(26,8),(30,13),(30,8)),('L',(13,14)),('C',(4,27),(7,17),(4,20)),('L',(4,30)),('A',(14,40),10,10,False),('L',(25,40)),('A',(25,33),4,4,False),('L',(20,33))])
self.path('index',(24,17),[('L',(40,17)),('A',(40,25),4,4,True),('L',(23,25))])
self.path('middle',(30,25),[('A',(30,33),4,4,True),('L',(23,33))])
self.relate('connect','palm','index');self.relate('connect','index','middle');self.relate('connect','middle','palm')
''',ref='Previously inspected Lucide hand: round finger tips and one flowing palm contour.')
# Lower-thumb variant is authored in its inverted hand pose, with wide curled fingers.
add(4,'HRECT_L','Rejected tight sawtooth knuckles obscure the folded fingers. Restore broad finger arcs and the downward thumb below the extended index.', '''
self.path('palm',(23,31),[('C',(25,40),(30,36),(29,40)),('L',(12,33)),('C',(4,21),(7,30),(4,27)),('L',(4,18)),('A',(14,8),10,10,True),('L',(25,8)),('A',(25,16),4,4,True),('L',(20,16))])
self.path('index',(23,31),[('L',(40,31)),('A',(40,23),4,4,False),('L',(23,23))])
self.path('middle',(30,23),[('A',(30,16),4,4,False),('L',(23,16))])
self.relate('connect','palm','index');self.relate('connect','index','middle');self.relate('connect','middle','palm')
''',ref='Previously inspected Lucide hand: rounded fingers and coherent palm; thumb orientation follows original.')
add(6,'VRECT_L','Rejected single inner blob loses brain folds and the head has an oversized angular nose. Restore a rounded skull and chin, a compact profile and recognizable lobed brain with folds.', '''
self.path('head',(12,44),[('L',(12,36)),('C',(8,22),(12,32),(8,30)),('C',(23,4),(8,11),(13,4)),('C',(36,20),(32,4),(36,10)),('L',(40,26)),('L',(35,26)),('L',(35,34)),('A',(31,38),4,4,True),('L',(25,38)),('L',(25,44))])
self.path('brain',(17,26),[('C',(13,20),(11,26),(11,21)),('C',(19,13),(12,15),(15,12)),('C',(25,12),(19,8),(24,8)),('C',(31,17),(31,10),(33,13)),('C',(29,25),(36,20),(34,25)),('L',(24,25)),('C',(17,26),(22,29),(19,30))],True)
self.path('fold',(25,12),[('L',(25,17)),('C',(20,20),(25,20),(22,20))])
self.add_line('brainstem',(24,25),(27,30));self.relate('connect','brain','fold','brainstem')
''',ref='Lucide brain original and atomic-debug: lobed outline and a small number of connected internal folds.')
add(7,'SQUARE','Rejected planet uses one slash and a solid X. Restore an elliptical orbit around a round planet and a pointed four-way sparkle.', '''
self.circle('planet',21,28,14)
self.path('ring',(8,27),[('C',(4,36),(0,32),(2,37)),('C',(43,22),(15,41),(48,24)),('C',(34,20),(46,16),(39,18))])
self.path('star',(38,5),[('C',(43,10),(38,8),(40,10)),('C',(38,15),(40,10),(38,12)),('C',(33,10),(38,12),(36,10)),('C',(38,5),(36,10),(38,8))],True)
self.relate('connect','planet','ring')
''',ref='Lucide orbit original/atomic-debug: clean circular planet; supplied reference owns elliptical ring and star.')
add(8,'SQUARE','Rejected orbital band is a thick diagonal slash. Restore a complete steeply tilted elliptical loop with visible front and rear lobes around the globe.', '''
self.circle('planet',24,24,15)
self.path('orbit',(42,6),[('C',(29,29),(45,9),(39,19)),('C',(6,42),(19,39),(9,45)),('C',(19,19),(3,39),(9,29)),('C',(42,6),(29,9),(39,3))],True)
self.relate('connect','planet','orbit')
''',ref='Lucide orbit: simple circle and smooth orbital arcs; original establishes steep ellipse.')
add(9,'SQUARE','Rejected arrow is short and heavy inside the square. Restore the reference tall shaft and wider upward arrow, balanced within a softly rounded square.', '''
self.box('frame',6,6,42,42,5)
self.add_polyline('arrow',(15,22),(24,13),(33,22))
self.add_line('shaft',(24,13),(24,35));self.relate('connect','arrow','shaft')
''')
add(10,'HRECT_L','Rejected bicycle has tiny wheels and a dense blocky frame. Restore two large thin-rim wheels, an open diamond frame, saddle and dropped road handlebar.', '''
self.circle('rear-wheel',11,33,7);self.circle('front-wheel',37,33,7)
self.add_polyline('frame',(11,33),(20,19),(31,19),(23,33),(11,33))
self.add_line('seat-tube',(18,12),(23,33));self.add_line('saddle',(15,12),(23,12))
self.add_line('fork',(29,8),(37,33));self.path('bars',(29,8),[('L',(36,8)),('A',(40,12),4,4,True),('L',(40,14))])
self.relate('connect','frame','rear-wheel','seat-tube','fork');self.relate('connect','fork','front-wheel','bars');self.relate('connect','seat-tube','saddle')
''',ref='Lucide bike original and atomic-debug: true circular wheels and diagonal structural strokes; source owns road-bike geometry.')
add(11,'SQUARE','Rejected stick figures and trapezoid do not communicate robbery. Restore a threatening robber holding a knife toward a victim marked with money.', '''
self.circle('robber-head',13,11,5);self.circle('victim-head',36,12,4)
self.add_line('robber-torso',(13,24),(13,34));self.add_polyline('robber-legs',(7,42),(13,34),(19,42))
self.add_line('victim-torso',(36,24),(36,33));self.add_polyline('victim-legs',(31,42),(36,33),(41,42))
self.add_polyline('robber-arm',(13,26),(20,29),(25,29))
self.add_polyline('blade',(25,25),(33,29),(25,33),closed=True)
self.add_line('blade-guard',(25,24),(25,34));self.relate('connect','blade','blade-guard','robber-arm');self.relate('connect','robber-torso','robber-arm','robber-legs');self.relate('connect','victim-torso','victim-legs')
self.add_polyline('threat-brow-left',(10,10),(12,11));self.add_polyline('threat-brow-right',(16,10),(14,11))
self.mark_human_figure('robber',head='robber-head',torso='robber-torso',torso_junction='start');self.mark_human_figure('victim',head='victim-head',torso='victim-torso',torso_junction='start')
''','Money symbol omitted to keep knife and two opposing people legible; knife retained as the defining robbery cue.',ref='Shared human full_body_ref.png: circular heads, aligned torsos and coherent limbs.')
add(12,'VRECT_L','Rejected angular claw has a tiny pivot and diagonal rod, losing the reference robot hand. Restore curved gripping jaws around the sample and a broad rounded wrist.', '''
self.circle('sample',24,12,6)
self.path('jaw-left',(19,14),[('C',(9,24),(12,14),(8,18)),('C',(18,32),(9,28),(14,32)),('L',(18,26)),('C',(19,20),(13,24),(14,21))])
self.path('jaw-right',(29,14),[('C',(39,24),(36,14),(40,18)),('C',(30,32),(39,28),(34,32)),('L',(30,26)),('C',(29,20),(35,24),(34,21))])
self.path('wrist',(18,28),[('L',(30,28)),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,28))],True)
self.add_line('feed-top',(8,4),(20,6));self.add_line('feed-bottom',(8,11),(13,12))
self.relate('connect','sample','jaw-left','jaw-right');self.relate('connect','wrist','jaw-left','jaw-right')
''')
add(13,'SQUARE','Rejected face is an M-shaped slit without eyes and the crest is a square tab. Restore a rounded helmet crest, ear pods, broad face opening and two eyes.', '''
self.path('helmet',(12,35),[('C',(6,23),(8,33),(6,29)),('C',(24,8),(6,13),(14,8)),('C',(42,23),(34,8),(42,13)),('C',(36,35),(42,29),(40,33))])
self.path('face',(24,25),[('C',(12,24),(17,19),(12,19)),('C',(10,33),(10,26),(10,30)),('C',(24,42),(12,39),(18,42)),('C',(38,33),(30,42),(36,39)),('C',(36,24),(38,30),(38,26)),('C',(24,25),(36,19),(31,19))],True)
self.path('crest',(18,6),[('L',(30,6)),('L',(30,15)),('A',(18,15),6,6,True),('L',(18,6))],True)
self.path('ear-left',(7,18),[('L',(4,18)),('L',(4,28)),('L',(8,28))]);self.path('ear-right',(41,18),[('L',(44,18)),('L',(44,28)),('L',(40,28))])
self.add_dot('eye-left',(19,30));self.add_dot('eye-right',(29,30))
self.relate('connect','helmet','face','crest','ear-left','ear-right')
''')
add(14,'VRECT_L','Rejected horns hand merges middle fingers into bumps and draws the thumb as a horizontal bar. Restore long index and little fingers, two folded knuckles, and a diagonally crossing thumb.', '''
self.path('hand',(10,27),[('L',(10,8)),('A',(18,8),4,4,True),('L',(18,22)),('C',(25,20),(18,17),(25,17)),('C',(32,22),(25,17),(32,17)),('L',(32,12)),('A',(40,12),4,4,True),('L',(40,30)),('C',(25,44),(40,39),(33,44)),('C',(10,33),(16,44),(10,39)),('L',(10,27))],True)
self.path('thumb',(10,29),[('C',(17,24),(10,26),(13,24)),('L',(24,24)),('C',(24,31),(28,24),(28,31)),('L',(20,31)),('C',(23,36),(23,32),(23,34))])
self.add_line('fold',(25,20),(25,24));self.relate('connect','hand','thumb','fold');self.relate('connect','thumb','fold')
''',ref='Previously inspected Lucide hand original and atoms: circular finger ends, continuous palm and articulated thumb.')
add(15,'SQUARE','Rejected rocket and planet are loose hooks and bars. Restore the pointed rocket with fins, a detached exhaust flame and a round planet with an elliptical departure path.', '''
self.path('planet',(27,15),[('C',(7,22),(18,10),(8,14)),('C',(20,42),(2,34),(9,42)),('C',(34,25),(31,42),(39,34))])
self.path('rocket',(31,17),[('C',(42,6),(33,10),(38,7)),('C',(38,21),(42,12),(40,17)),('L',(36,25)),('L',(27,16)),('L',(31,17))],True)
self.add_polyline('flame',(29,25),(22,29),(25,32),(29,25))
self.path('trail',(21,29),[('C',(6,42),(12,39),(4,48)),('C',(7,32),(2,39),(5,34))])
self.relate('connect','planet','trail')
''',ref='Lucide rocket original/atomic-debug: tapered pointed shell and distinct exhaust; original defines planet and orbit.')
add(16,'SQUARE','Rejected rocket loses its fins and the globe becomes a semicircular cross. Restore a diagonal finned rocket and a round lower globe with a continent contour.', '''
self.path('rocket',(15,23),[('L',(27,10)),('C',(42,6),(33,7),(38,6)),('C',(38,20),(42,11),(40,17)),('L',(25,32)),('L',(15,23))],True)
self.add_polyline('fin-left',(19,19),(12,19),(7,24),(15,27));self.add_polyline('fin-right',(29,29),(29,36),(24,41),(21,33))
self.add_line('nose-seam',(30,9),(39,18));self.relate('connect','rocket','fin-left','fin-right','nose-seam')
self.path('globe',(35,30),[('C',(42,36),(40,30),(42,33)),('C',(31,44),(42,42),(36,44)),('C',(25,38),(27,44),(25,41))])
self.path('continent',(42,36),[('L',(36,37)),('C',(35,43),(33,38),(37,40))]);self.relate('connect','globe','continent')
self.add_line('exhaust-a',(12,31),(6,37));self.add_line('exhaust-b',(16,35),(12,39))
''',ref='Lucide rocket original and atomic-debug: pointed body and attached fins; original defines globe placement.')
add(17,'SQUARE','Rejected descending objects become angular shield-like symbols. Restore two rounded downward rockets with side fins, falling trails and a curved planetary horizon.', '''
for n,x,y in [('left',14,19),('right',34,15)]:
 self.path(n+'-body',(x-4,y),[('A',(x+4,y),4,4,True),('L',(x+4,y+10)),('C',(x,y+15),(x+4,y+12),(x+2,y+14)),('C',(x-4,y+10),(x-2,y+14),(x-4,y+12)),('L',(x-4,y))],True)
 self.path(n+'-left-fin',(x-4,y),[('L',(x-10,y-3)),('L',(x-10,y+2)),('C',(x-4,y+6),(x-10,y+5),(x-7,y+6))])
 self.path(n+'-right-fin',(x+4,y),[('L',(x+10,y-3)),('L',(x+10,y+2)),('C',(x+4,y+6),(x+10,y+5),(x+7,y+6))])
 self.relate('connect',n+'-body',n+'-left-fin',n+'-right-fin')
self.add_line('trail-left',(14,8),(14,11));self.add_line('trail-right',(34,4),(34,7))
self.add_bezier('horizon',(4,44),((17,39),(31,39),(44,44)))
''')
for i in (18,19):
 add(i,'SQUARE','Rejected angular horse has a flat body and narrow head; the toy variant also has a flat sled base. Restore a rounded horse silhouette, arched belly and a visibly curved rocker.', '''
self.path('horse',(8,22),[('C',(6,15),(3,21),(4,17)),('L',(16,9)),('C',(21,12),(19,7),(20,9)),('L',(25,22)),('L',(33,22)),('C',(39,29),(38,22),(38,25)),('L',(42,36)),('L',(35,39)),('C',(27,31),(33,33),(32,31)),('C',(15,36),(21,29),(17,31)),('L',(12,39)),('L',(6,36)),('L',(15,24)),('L',(13,19)),('L',(8,22))],True)
self.path('rocker',(6,36),[('C',(42,36),(16,44),(32,44)),('A',(44,42),3,3,True),('C',(4,42),(32,49),(16,49)),('A',(6,36),3,3,True)],True)
self.path('tail',(37,25),[('C',(44,29),(41,21),(44,25))])
self.relate('connect','horse','rocker','tail')
''','Eye omitted to keep muzzle open; rounded neck, arched belly, tail and curved rocker retained.')
# Generic author/export implementations, rebased onto this batch.
chunk=old.split('def author(i,version=1):',1)[1].split("if __name__=='__main__':",1)[0]
chunk=chunk.replace('20260929T041010Z','20260929T044747Z')
exec('def author(i,version=1):'+chunk)
if __name__=='__main__':
 results=[]
 for i in range(20):
  run,module,md=author(i);results.append(export(run,module,md))
 (B/'drafts.json').write_text(json.dumps(results,indent=2))
