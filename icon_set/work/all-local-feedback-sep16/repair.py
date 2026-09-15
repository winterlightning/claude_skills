from pathlib import Path
import json,re,textwrap,hashlib
W=Path(__file__).resolve().parent
R={r['key'].split('/')[1]:r for r in json.loads((W/'inventory.json').read_text())}
changes={}
def edit(id,fn,note):
 p=Path(R[id]['path']);s=p.read_text();new=fn(s)
 assert new!=s,id
 p.write_text(new);changes[id]=note
helpers='''
        def path(n, start, commands, closed=False):
            names=[];here=start
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                names.append(ident);here=end
            self.add_contour(n,*names,closed=closed)
        def ellipse(n,x,y,rx,ry):
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
'''
def rewrite(id,code,note,key=None):
 def fn(s):
  if key:s=re.sub(r'keyshape = Keyshape\.\w+', 'keyshape = Keyshape.'+key,s)
  s=s[:s.index('    def build(')]+'    def build(self):\n        # '+note+'\n'+helpers+textwrap.indent(textwrap.dedent(code).strip()+'\n','        ')
  return s
 edit(id,fn,note)
# Direct repairs preserve the current construction and source identity.
edit('ant',lambda s:'\n'.join(l for l in s.split('\n') if 'leg-top-' not in l),'Removed the two middle leg arcs.')
for id in ['compact-disc-with-sheen-arcs','disk-platter-with-drive-slots']:
 edit(id,lambda s:s.replace("circle('hub', 24, 24, 2)","self.add_dot('hub', (24,24))"),'Replaced the small center ring with one solid dot.')
edit('leaning-tower-of-pisa',lambda s:'\n'.join(l for l in s.split('\n') if "line('floor-upper'" not in l),'Removed both interior floor lines; kept the leaning silhouette.')
edit('sloth-face',lambda s:s.replace('radius_x=22, radius_y=19','radius_x=18, radius_y=18'),'Replaced the pointed face outline with an exact circle.')
edit('vintage-studio-microphone',lambda s:s[:s.index('        for y in (14,22):')]+s[s.index("        self.add_line('stem'"):],'Removed all four interior grille lines.')
edit('wolf-face',lambda s:s[:s.index("        self.add_arc('nose-top'")]+"        self.add_dot('nose', (24,30))\n",'Replaced the nose ring with a solid dot.')
edit('saturn-astrological-symbol',lambda s:s.replace('(16, 22)','(16, 26)').replace('(40, 22)','(40, 26)').replace('radius_y=22','radius_y=18'),'Lowered the shoulder curve to give the crossbar a clear nine-unit centerline gap.')
edit('standing-stag',lambda s:s.replace("('L',(36,42))", "('L',(36,34)),('L',(36,42))").replace("[('L',(20,34)),('A',(28,42),8,8,True)]", "[('L',(36,34))]"),'Replaced the extra curved leg with a belly joining the two straight legs.')
edit('standing-giraffe',lambda s:s.replace('(24, 4),(32, 4),(32, 8)','(32, 8)').replace("        self.add_contour('body'", "        self.add_line('ear',(24,8),(20,4))\n        self.relate('connect','ear','body')\n        self.add_contour('body'").replace("*[", "*["),'Replaced the rectangular ear projection with a single short line.')
# Rebuild giraffe contour automatically after its shortened polyline.
p=Path(R['standing-giraffe']['path']);s=p.read_text();s=re.sub(r"'neck-head-11','neck-head-12','neck-head-13'", "'neck-head-11'",s);p.write_text(s)
edit('rubber-duck',lambda s:s[:s.index("        self.add_polyline('bill'")]+"        self.add_line('bill-base',(10,28),(10,26))\n        self.add_arc('bill-curve',(10,26),(10,18),radius_x=6,radius_y=4,sweep=True)\n        self.add_contour('body','head-top','head-back','neck','back','tail','body-right','belly','body-left','bill-base','bill-curve',closed=True)\n",'Rounded the projecting beak with one half ellipse instead of a rectangle.')
edit('woolly-lamb-front',lambda s:s.replace("self.add_line('ear-right-0', p_30_22, p_33_26)","self.add_arc('ear-right-0', p_30_22, p_33_26, radius_x=4, radius_y=4)").replace("self.add_line('ear-right-1', p_33_26, p_30_26)","self.add_arc('ear-right-1', p_33_26, p_30_26, radius_x=4, radius_y=4)").replace("self.add_line('ear-left-0', p_18_26, p_15_26)","self.add_arc('ear-left-0', p_18_26, p_15_26, radius_x=4, radius_y=4)").replace("self.add_line('ear-left-1', p_15_26, p_18_22)","self.add_arc('ear-left-1', p_15_26, p_18_22, radius_x=4, radius_y=4)"),'Rounded both triangular ears with paired mirrored arcs.')
rewrite('teacher-presenting-at-whiteboard', '''
path('board',(28,2),[('L',(56,2)),('A',(62,8),6,6,True),('L',(62,48)),('A',(56,54),6,6,True),('L',(38,54))])
ellipse('head',15,11,9,9)
line('torso',(15,28),(15,46))
poly('legs',(2,62),(15,46),(28,62));join('legs','torso')
poly('arms',(2,40),(15,28),(28,40),(38,30));join('arms','torso')
self.mark_human_figure('teacher',head='head',torso='torso',torso_junction='start')
''','Stick-line torso and limbs follow the human reference; head-to-torso ink gap is exactly four.')
rewrite('arched-stone-bridge', '''
path('stone',(6,42),[('L',(6,6)),('L',(42,6)),('L',(42,42)),('L',(34,42)),('L',(34,26)),('A',(24,16),10,10,False),('A',(14,26),10,10,False),('L',(14,42)),('L',(6,42))],True)
''','Reduced the double-storey bridge to one broad rounded arch and two stone piers; Lucide bridge informs simple structural strokes.','SQUARE')
rewrite('cat-paw', '''
for name,x,y in [('left',10,16),('middle',24,10),('right',38,16)]:ellipse(name,x,y,4,4)
ellipse('pad',24,35,12,7)
''','Three rounded toe circles above one simple pad, following the Lucide paw-print vocabulary.','SQUARE')
rewrite('face-wearing-round-glasses', '''
ellipse('face',24,24,20,20)
for name,x in [('left',14),('right',34)]:ellipse(name,x,22,5,5)
line('bridge',(19,22),(29,22));join('bridge','left');join('bridge','right')
''','Enlarged both glasses equally and removed the smile to reserve clear space; Lucide glasses uses paired circles.','CIRCLE')
rewrite('hydroelectric-dam', '''
poly('left-pier',(4,24),(4,8),(12,8),(12,16),(12,24),closed=True)
poly('right-pier',(36,24),(36,16),(36,8),(44,8),(44,24),closed=True)
line('crest',(12,16),(36,16));join('crest','left-pier');join('crest','right-pier')
for j,(a,b,c) in enumerate([(4,10,16),(18,24,30),(32,38,44)]):
 path(f'water-{j}',(a,36),[('C',(c,36),(b-3,41+1/3),(b+3,41+1/3))])
''','Three separate shallow curved water strokes replace the central straight stream and two-wave baseline.','HRECT_L')
rewrite('cobra-head', '''
path('hood',(18,42),[('L',(18,34)),('C',(6,20),(10,30),(6,26)),('A',(24,6),18,14,True),('A',(42,20),18,14,True),('C',(30,34),(42,26),(38,30)),('L',(30,42)),('L',(18,42))],True)
dot('eye-left',(18,18));dot('eye-right',(30,18))
''','Simplified to a broad symmetric cobra hood, two eyes and a narrow neck; natural hood silhouette, no useful exact Lucide match.','SQUARE')
rewrite('necklace-bust-form', '''
path('form',(16,4),[('L',(32,4)),('C',(40,16),(32,12),(36,16)),('L',(36,44)),('L',(12,44)),('L',(8,16)),('C',(16,4),(12,16),(16,12))],True)
path('necklace',(16,4),[('C',(24,28),(16,20),(18,28)),('C',(32,4),(30,28),(32,20))]);join('form','necklace')
''','Widened the bust base and shortened the necklace drop to open the side and bottom gaps.','VRECT_L')
rewrite('round-bud-vase', '''
poly('mouth',(8,30),(24,30),(40,30))
path('vase',(40,30),[('A',(24,44),16,14,True),('A',(8,30),16,14,True)]);join('mouth','vase')
for name,x,y in [('left',11,15),('top',24,7)]:
 ellipse(name,x,y,3,3);line(name+'-stem',(x,y+3),(24,30));join(name,name+'-stem');join(name+'-stem','mouth')
join('left-stem','top-stem')
''','Removed the lower-right branch and rebalanced the vase width to retain the profile envelope.','VRECT_L')
rewrite('selene-astrological-symbol', '''
path('moon',(24,4),[('A',(36,16),12,12,True),('A',(24,28),12,12,True)])
poly('stem',(24,28),(24,36),(24,44));poly('crossbar',(16,36),(24,36),(32,36));join('moon','stem');join('stem','crossbar')
''','The moon is now an exact half circle above a clearly separated cross.','CIRCLE')
rewrite('sitting-penguin', '''
ellipse('body',24,24,16,20)
dot('eye-left',(20,17));dot('eye-right',(28,17));dot('beak',(24,26))
poly('feet',(8,44),(24,44),(40,44));join('body','feet')
''','An oval body replaces the pinched waist; paired eyes and a beak preserve the penguin face.','VRECT_L')
rewrite('three-bead-drop-earring', '''
ellipse('stud',10,10,4,4);ellipse('middle',24,24,7,7);ellipse('drop',38,38,4,4)
line('upper-link',(14,10),(24,17));line('lower-link',(24,31),(34,38))
for a,b in [('stud','upper-link'),('middle','upper-link'),('middle','lower-link'),('drop','lower-link')]:join(a,b)
''','Increased the top and bottom beads and rebalanced the middle bead for clear diagonal spacing.','SQUARE')
rewrite('tropical-island-with-palm-tree', '''
path('island',(8,40),[('A',(24,32),16,8,True),('A',(40,40),16,8,True),('A',(24,44),16,4,True),('A',(8,40),16,4,True)],True)
path('trunk',(24,12),[('C',(24,32),(28,18),(28,26))]);join('trunk','island')
path('left-frond',(24,12),[('C',(8,18),(18,8),(10,10))])
path('right-frond',(24,12),[('C',(40,18),(30,8),(38,10))])
path('top-frond',(24,12),[('C',(34,4),(24,6),(30,4))])
for a in ['left-frond','right-frond','top-frond']:
 join(a,'trunk')
for a,b in [('left-frond','right-frond'),('left-frond','top-frond'),('right-frond','top-frond')]:join(a,b)
''','Reduced to one island, a curved trunk and three fronds; removed the decorative waves.','VRECT_L')
# Save outcomes, allowing subsequent focused refinement rather than rerunning this file.
(W/'changes.json').write_text(json.dumps(changes,indent=2))
print(len(changes),'models updated')
