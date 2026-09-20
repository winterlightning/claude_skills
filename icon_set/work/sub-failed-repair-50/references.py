from inspect_batch import paste,Image,ImageDraw,W,ROOT
names=['spray-can','plane','rotate-ccw','mouse-pointer-2','arrow-big-up','shopping-bag','laptop','battery','battery-charging','flask-round','bed','bell','fingerprint','eye-off','bone','book','book-open','briefcase-business','unlink','bug','building','bus-front','camera','car','ship','carrot','cat','message-circle','list-checks','baby']
im=Image.new('RGB',(1000,((len(names)+4)//5)*160),'white');d=ImageDraw.Draw(im)
for i,n in enumerate(names):
 x=i%5*200;y=i//5*160;d.text((x+5,y+3),n,fill='black')
 for j,kind in enumerate(['original','atomic-debug']):
  p=ROOT/'icon_set/references/lucide'/kind/(n+'.svg')
  if p.exists():paste(im,p.read_text(),x+j*100,y+25,90)
im.save(W/'references.png')
