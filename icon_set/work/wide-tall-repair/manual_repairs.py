from repair_geometry import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'

def move(r,fn,select=lambda p:True):
 for p in r['primitives']:
  if not select(p):continue
  a,b=p['start'][:],p['end'][:];quarter=p['kind']=='arc' and abs(a[0]-b[0])==p['radius_x'] and abs(a[1]-b[1])==p['radius_y']
  p['start']=list(fn(*a));p['end']=list(fn(*b))
  if quarter:
   p['radius_x']=abs(p['start'][0]-p['end'][0]);p['radius_y']=abs(p['start'][1]-p['end'][1])
def remove(r,names):
 names=set(names);members=set(names)
 for c in r['contours']:
  if c['contour_id'] in names:members.update(c['members'])
 r['primitives']=[p for p in r['primitives'] if p['element_id'] not in members]
 r['contours']=[c for c in r['contours'] if c['contour_id'] not in names and not set(c['members'])&members]
 r['relationships']=[c for c in r['relationships'] if not set(c['members'])&members]
def edit(id,fn,note):
 f=W/'candidates'/f'{id}.json';x=json.loads(f.read_text())
 if x.get('manual_note'):return
 fn(x['record']);x['manual_note']=note;q=check(f,x);print(id,q['status'],q['errors']+q['warnings'],flush=True)
def by(r,name):return next(p for p in r['primitives'] if p['element_id']==name)

if __name__=='__main__':
 def baby(r):
  # Circular head centered (24,10), radius6: bottom16; shoulder station24.
  for n in ['head-top','head-bottom']:
   p=by(r,n);p['start'][0]=18 if p['start'][0]<24 else 30;p['end'][0]=18 if p['end'][0]<24 else 30;p['radius_x']=p['radius_y']=6
  move(r,lambda x,y:(x,24 if y==23 else y))
 edit('baby-figure-v2',baby,'Circular six-unit infant head and shoulder station24 give exactly four units of visible clearance; kept stick arms and diaper.')
 edit('baby-head',lambda r:move(r,lambda x,y:(6 if x==7 else 42 if x==41 else x,y)),'Extended paired shoulder ends to the square envelope; kept curl, cheeks and ears.')
 edit('classical-statue-bust',lambda r:move(r,lambda x,y:(x,36 if y==37 else y)),'Raised the bust base to leave four units of ink clearance above the plinth.')
 edit('classical-temple-facade',lambda r:move(r,lambda x,y:(x,{24:25,35:34}.get(y,y))),'Rebalanced column and step stations for equal legal separations.')
 edit('dog-face-tall-ears',lambda r:(move(r,lambda x,y:(17 if x==16 else 31 if x==32 else x,y),lambda p:'eye' in p['element_id']),move(r,lambda x,y:(x,y-1),lambda p:'nose' in p['element_id'])),'Inset paired eyes and raised the nose one unit for certifiable curved clearances.')
 edit('drop-earrings-with-diamond-beads',lambda r:move(r,lambda x,y:(20 if x==21 else 28 if x==27 else x,y)),'Narrowed the inward diamond tips to retain four units of clear ink between the earrings.')
 edit('flaming-brazier',lambda r:move(r,lambda x,y:(x,18 if y==19 else y),lambda p:p['element_id'].startswith('flame')),'Shortened the flame ends to clear the bowl rim.')
 edit('handbag-with-clasp',lambda r:move(r,lambda x,y:(x,y-1),lambda p:p['element_id'].startswith(('clasp','flap'))),'Raised clasp and attached flap together to open the gap above the bag base.')
 edit('hanging-chinese-lanterns',lambda r:move(r,lambda x,y:(x,y+2 if y==14 else y),lambda p:p['element_id'].startswith('right')),'Lowered the right lantern cap and shared upper attachment; retained the staggered hanging scene.')
 edit('inscribed-stone-tablet',lambda r:move(r,lambda x,y:(20 if x==21 else 28 if x==27 else x,y),lambda p:'middle' in p['element_id']),'Shortened the middle inscription strokes to leave a clear four-unit gap.')
 edit('monitor-with-desk-keyboard',lambda r:move(r,lambda x,y:(x,{28:26,25:23}.get(y,y))),'Raised the screen bottom and its shared stand node, retaining keyboard thickness and eight-unit centerline stand height.')
 edit('necklace-with-teardrop-pendant',lambda r:move(r,lambda x,y:(x,25 if y==27 else y)),'Raised the necklace bowl apex to separate the pendant by four visible units.')
 edit('paired-landscape-window-panels',lambda r:move(r,lambda x,y:(20 if x==21 else 28 if x==27 else x,y)),'Opened the central frame gap symmetrically while retaining both landscape panels.')
 edit('smartwatch',lambda r:move(r,lambda x,y:(x,{12:14,16:18,36:34,32:30}.get(y,y))),'Shortened the watch case vertically and moved shared strap nodes together, leaving eight units between the case and strap crests.')
 edit('trilobite-fossil',lambda r:remove(r,['head-ridge']),'Removed the crowded head ridge; retained the domed head, segmented body, legs and tail.')
 edit('written-scroll',lambda r:(remove(r,['writing-bottom']),move(r,lambda x,y:(24 if x==23 else 29 if x==30 else x,y),lambda p:p['element_id']=='writing-top')),'Retained one centered inscription line; removed the lower crowded line to keep the scroll opening readable.')
