from pathlib import Path
import json,ast,textwrap
W=Path(__file__).parent;ROOT=W.resolve().parents[2]
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/design-repair/mapping.json'
AUTHOR='gpt-6'
# Small authoring notation expands into the ordinary geometry API in each module.
def body(steps):
 lines=[];members=[]
 joined={n for s in steps if s[0]=="C" and len(s)>2 for n in s[2]}
 for s in steps:
  kind,name,*args=s
  if kind=='L':lines.append(f'self.add_line({name!r}, {args[0]!r}, {args[1]!r})');members.append(name)
  elif kind=='A':
   a,b,rx,*rest=args;ry=rest[0] if rest else rx;sweep=rest[1] if len(rest)>1 else True
   lines.append(f'self.add_arc({name!r}, {a!r}, {b!r}, radius_x={rx}, radius_y={ry}, sweep={sweep})');members.append(name)
  elif kind=='P':
   pts=args[0];closed=args[1] if len(args)>1 else False
   if any(n.startswith(name+'-') for n in joined):
    for i,(a,b) in enumerate(zip(pts,pts[1:]),1):lines.append(f'self.add_line({(name+"-"+str(i))!r}, {a!r}, {b!r})')
   else:lines.append(f'self.add_polyline({name!r}, '+', '.join(map(repr,pts))+f', closed={closed})')
  elif kind=='C':
   names=args[0] if args else members;closed=args[1] if len(args)>1 else True
   lines.append(f'self.add_contour({name!r}, '+', '.join(map(repr,names))+f', closed={closed})');members=[]
  elif kind=='D':lines.append(f'self.add_dot({name!r}, {args[0]!r})')
  elif kind=='R':lines.append(f'self.relate("connect", {name!r}, {args[0]!r})')
 return '\n'.join(lines)
def circle(name,x,y,r):return [('A',name+'-a',(x-r,y),(x+r,y),r),('A',name+'-b',(x+r,y),(x-r,y),r),('C',name,[name+'-a',name+'-b'])]
D={}
for name in ['camera','camera-with-shutter-button']:
 s=[('P','housing',[(8,14),(12,14),(18,8),(30,8),(36,14),(40,14)]),('A','tr',(40,14),(44,18),4),('L','right',(44,18),(44,36)),('A','br',(44,36),(40,40),4),('L','bottom',(40,40),(8,40)),('A','bl',(8,40),(4,36),4),('L','left',(4,36),(4,18)),('A','tl',(4,18),(8,14),4),('C','body',[*[f'housing-{i}' for i in range(1,6)],'tr','right','br','bottom','bl','left','tl'])]+circle('lens',24,25,6)
 if name.endswith('button'):s += [('L','shutter',(8,14),(8,8)),('R','shutter','body')]
 D[name]=('HRECT_L',s,'Lucide camera: tangent quarter-circle body corners and a centered lens; raised housing retained.')
D['curved-dam-wall']=('HRECT_L',[
 ('P','wall',[(4,32),(4,8),(14,8),(14,16),(34,16),(34,8),(44,8),(44,32)]),('A','water',(44,32),(4,32),20,8),('C','outline',[*[f'wall-{i}' for i in range(1,8)],'water']),('L','flow-left',(18,25),(16,31)),('L','flow-right',(32,25),(30,31))], 'Shared 10-unit wall thickness and one elliptical lower water edge; paired flow marks. No useful Lucide dam match.')
D['diamond-ring']=('VRECT_L',[
 ('P','gem',[(16,16),(12,8),(18,4),(30,4),(36,8),(32,16)]),('A','band-top-right',(32,16),(40,28),8,12),('A','band-bottom-right',(40,28),(24,44),16),('A','band-bottom-left',(24,44),(8,28),16),('A','band-top-left',(8,28),(16,16),8,12),('C','outline',[*[f'gem-{i}' for i in range(1,6)],'band-top-right','band-bottom-right','band-bottom-left','band-top-left']),('A','crown',(16,16),(32,16),8,4),('R','outline','crown')], 'Lucide gem: deliberate facet corners; band uses exact cardinal ellipse and circle junctions, mirrored about x=24.')
D['dinosaur-footprint']=('SQUARE',[
 ('P','toes',[(10,32),(6,10),(17,22),(24,6),(31,22),(42,10),(38,32)]),('A','heel-right',(38,32),(24,42),14,10),('A','heel-left',(24,42),(10,32),14,10),('C','track',[*[f'toes-{i}' for i in range(1,7)],'heel-right','heel-left'])], 'Three pointed toes and one elliptical heel, mirrored about x=24. Lucide footprints informs the simple single-contour footprint, not human toe anatomy.')
D['fuel-pump-with-display']=('HRECT_L',[
 ('P','pump',[(4,40),(4,20),(4,8),(26,8),(26,20),(26,24),(26,40)],True),('L','display',(4,20),(26,20)),('R','pump','display'),('D','button',(15,30)),('L','hose-start',(26,24),(34,24)),('L','hose-drop',(34,24),(34,35)),('A','hose-turn',(34,35),(44,35),5,5,False),('P','nozzle',[(44,35),(44,16),(38,8)]),('C','hose',['hose-start','hose-drop','hose-turn','nozzle-1','nozzle-2'],False),('R','pump','hose')], 'Lucide fuel: upright pump and a separate return hose. Hose walls 10 units apart; loop is a tangent semicircle.')
D['floppy-disk-v2']=('SQUARE',[
 ('P','disk',[(6,6),(36,6),(42,12),(42,42),(6,42)],True),('P','shutter',[(15,6),(15,15),(28,15)]),('R','disk','shutter'),('P','label',[(15,42),(15,29),(33,29),(33,42)]),('R','disk','label')], 'Lucide save: clipped outer corner, open shutter stroke and large lower label. Remove the nonessential hub dot to give the label room; no collapsed counters.')
D['wolf-face']=('SQUARE',[
 ('P','upper',[(6,28),(7,18),(6,6),(16,10),(32,10),(42,6),(41,18),(42,28),(30,40)]),('A','chin',(30,40),(18,40),10),('L','left-jaw',(18,40),(6,28)),('C','head',[*[f'upper-{i}' for i in range(1,9)],'chin','left-jaw'])]+circle('nose',24,30,3), 'Lucide dog: simple face and centered muzzle; pointed ears preserve wolf identity. Mirror x=24; chin radius 10 reaches y=42 exactly.')
D['tank-wagon']=('HRECT_L',[
 ('P','top',[(15,12),(20,12),(20,8),(28,8),(28,12),(33,12)]),('A','right',(33,12),(33,34),11),('L','bottom',(33,34),(15,34)),('A','left-bottom',(15,34),(4,23),11),('A','left-top',(4,23),(15,12),11),('C','tank',[*[f'top-{i}' for i in range(1,6)],'right','bottom','left-bottom','left-top']),('P','ladder',[(15,12),(15,23),(15,34)]),('L','rung',(4,23),(15,23)),('R','ladder','tank'),('R','rung','tank'),('R','ladder','rung')]+circle('rear',15,37,3)+[('R','rear','tank'),('R','rear','ladder')]+circle('front',33,37,3)+[('R','front','tank')], 'Capsule tank with matched radius-11 ends, integral hatch and equally sized wheels. Preserve attached ladder. No useful Lucide tank-wagon match.')
D['pointed-paintbrush']=('SQUARE',[
 ('L','handle-upper',(18,19),(34,7)),('A','cap',(34,7),(40,15),5),('L','handle-lower',(40,15),(24,27)),('L','ferrule',(24,27),(18,19)),('C','handle'),('A','bristle-crown',(18,19),(8,32),14,14,False),('L','bristle-tip',(8,32),(6,42)),('L','bristle-bottom',(6,42),(22,42)),('A','bristle-side',(22,42),(24,27),16,16,False),('C','bristles',['bristle-crown','bristle-tip','bristle-bottom','bristle-side'],False),('R','handle','bristles')], 'Lucide paintbrush: diagonal handle and broad bristle head. Intentional bristle point; coherent cap will be checked against exact square extrema.')
D['hooded-cobra']=('SQUARE',[
 ('L','head-top',(18,6),(30,6)),('A','hood-right',(30,6),(42,18),12),('A','taper-right',(42,18),(30,30),12),('L','neck-right',(30,30),(30,34)),('L','coil-top-right',(30,34),(38,34)),('A','coil-right',(38,34),(38,42),4),('L','coil-bottom',(38,42),(10,42)),('A','coil-left',(10,42),(10,34),4),('L','coil-top-left',(10,34),(18,34)),('L','neck-left',(18,34),(18,30)),('A','taper-left',(18,30),(6,18),12),('A','hood-left',(6,18),(18,6),12),('C','outline'),('D','eye-left',(18,16)),('D','eye-right',(30,16))], 'Symmetric hood uses radius-12 quarters; base coil has a full 8-unit centerline opening and radius-4 ends. Eye pair shares y=16. No useful Lucide cobra match.')
D['anteater']=('HRECT_L',[
 ('A','back',(18,20),(36,20),9,12),('L','tail-top',(36,20),(44,32)),('L','tail-bottom',(44,32),(34,30)),('L','hind-leg',(34,30),(34,40)),('L','hind-foot',(34,40),(26,40)),('L','hind-inner',(26,40),(26,30)),('L','belly',(26,30),(18,30)),('L','fore-inner',(18,30),(18,40)),('L','fore-foot',(18,40),(10,40)),('L','fore-front',(10,40),(12,26)),('L','snout-lower',(12,26),(4,30)),('L','snout-tip',(4,30),(4,24)),('L','snout-top',(4,24),(18,20)),('C','animal')], 'Long sloping snout, domed back and tapering tail identify a left-facing anteater. Two broad legs preserve open negative space. No useful Lucide anteater match; natural profile asymmetry is intentional.')
D['hatching-dinosaur-egg']=('SQUARE',[
 ('A','shell-bottom',(42,28),(6,28),18,14),('P','crack',[(6,28),(15,34),(24,28),(33,34),(42,28)]),('C','shell',['shell-bottom',*[f'crack-{i}' for i in range(1,5)]]),('L','neck',(33,34),(33,16)),('A','head-top',(33,16),(23,6),10,10,False),('L','forehead',(23,6),(16,6)),('A','face',(16,6),(6,16),10,10,False),('A','jaw-round',(6,16),(14,24),8,8,False),('L','jaw',(14,24),(18,24)),('L','throat',(18,24),(18,32)),('C','hatchling',['neck','head-top','forehead','face','jaw-round','jaw','throat'],False),('R','shell','hatchling'),('D','eye',(23,16))], 'Baby dinosaur head uses tangent cardinal arcs and a broad muzzle above a single cracked shell. Eye placed with generous head clearance. No useful Lucide hatchling match.')
for row in json.loads((W/'mapping.json').read_text()):
 if not row['changed']:continue
 p=ROOT/row['file'];src=p.read_text();old=row['original']
 if old in D:
  key,steps,plan=D[old];tree=ast.parse(src);cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));build=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='build')
  lines=src.splitlines();src='\n'.join(lines[:build.lineno-1])+ '\n    def build(self):\n        # '+plan+'\n'+textwrap.indent(body(steps),'        ')+'\n'
  src=__import__('re').sub(r'keyshape = Keyshape\.\w+', 'keyshape = Keyshape.'+key,src)
 else:
  # Existing coherent contours need only a corrected owning endpoint construction.
  if old=='airplane-horizontal':src=src.replace('(6, 16)','(4, 16)').replace('(6, 32)','(4, 32)')
  elif old in ('brontosaurus','brontosaurus-v2'):
   src=src.replace("self.add_arc('head', (8, 12), (8, 6), radius_x=6, radius_y=5)","self.add_arc('head', (8, 12), (8, 6), radius_x=2, radius_y=3)")
   src=src.replace("self.add_arc('nape', (12, 6), (18, 8), radius_x=6)","self.add_arc('nape', (12, 6), (18, 12), radius_x=6)").replace("(18, 8), (20, 26)","(18, 12), (20, 26)")
  elif old=='bat-emblem':
   src=src.replace('(6, 26)','(4, 26)').replace('(42, 26)','(44, 26)')
  elif old=='horse-head':
   src=src.replace("self.add_arc('poll-back', (38, 12), (42, 20), radius_x=8, sweep=True)","self.add_arc('poll-back', (38, 12), (42, 20), radius_x=4, radius_y=8, sweep=True)")
   src=src.replace("self.add_arc('muzzle', (10, 36), (6, 28), radius_x=8, sweep=True)","self.add_arc('muzzle', (10, 36), (6, 28), radius_x=4, radius_y=8, sweep=True)")
  src=src.replace('Keyshape.HRECT_XL','Keyshape.HRECT_L')
 p.write_text(src)
print('Design candidates written')
