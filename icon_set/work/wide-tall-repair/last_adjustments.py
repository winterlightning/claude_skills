from final_shapes import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
def finish(id,fn,note):
 f=W/'candidates'/f'{id}.json';x=json.loads(f.read_text())
 if x.get('last_adjusted'):return
 fn(x['record']);x['last_adjusted']=True;x['manual_note']=x.get('manual_note','')+' '+note;q=check(f,x);print(id,q['status'],q['errors']+q['warnings'],flush=True)
if __name__=='__main__':
 finish('chinese-dragon-head',lambda r:[by(r,n).update(radius_y=1) for n in ['muzzle-left','muzzle-right']],'Flattened the paired muzzle arches to clear the eyes.')
 finish('distressed-baby-face',lambda r:move(r,lambda x,y:(x,y-1),lambda p:p['element_id']=='frown'),'Raised the frown one unit.')
 finish('feathered-war-bonnet',lambda r:move(r,lambda x,y:(12 if x==13 else 36 if x==35 else x,y),lambda p:'feather' in p['element_id'] and not p['element_id'].startswith('center')),'Inset the paired feather bases away from the central feather.')
 def lamb(r):
  for n in ['face-top','face-bottom']:
   p=by(r,n);p['start'][0]=19 if p['start'][0]<24 else 29;p['end'][0]=19 if p['end'][0]<24 else 29;p['radius_x']=p['radius_y']=5
 for id in ['fluffy-lamb-front','woolly-lamb-front']:finish(id,lamb,'Used a five-unit circular face for clear fleece separation.')
 def knight(r):
  move(r,lambda x,y:({15:14,33:34}.get(x,x),10 if y==11 else 29 if y==28 else y),lambda p:p['element_id'].startswith(('helm','jaw','spike')))
 finish('knight-armor-torso',knight,'Broadened the helmet and its dome around the centered visor.')
 def links(r):
  reset(r,'HRECT_L');line(r,'left-top',(24,8),(14,8));arc(r,'left-upper',(14,8),(4,19),10,11,False);arc(r,'left-lower',(4,19),(14,30),10,11,False);line(r,'left-bottom',(14,30),(24,30));contour(r,'left-link','left-top','left-upper','left-lower','left-bottom')
  line(r,'right-top',(24,18),(34,18));arc(r,'right-upper',(34,18),(44,29),10,11);arc(r,'right-lower',(44,29),(34,40),10,11);line(r,'right-bottom',(34,40),(24,40));contour(r,'right-link','right-top','right-upper','right-lower','right-bottom')
 finish('interlocking-chain-links',links,'Reconstructed opposing open links from exact quarter ellipses, retaining the offset interlocking arrangement.')
