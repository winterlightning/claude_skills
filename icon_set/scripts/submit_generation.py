#!/usr/bin/env python3
"""Submit generate/fix jobs to the review server from run_icon_agent.sh."""
import argparse
import json
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mission', choices=('generate','fix'))
    parser.add_argument('--name',help='Name of a new icon')
    parser.add_argument('--icon',help='Existing family/icon-id for a fix')
    parser.add_argument('--family',choices=('auto','sub','solo','container'),default='auto')
    parser.add_argument('--prompt',required=True)
    parser.add_argument('--model',default='')
    parser.add_argument('--server',default=os.environ.get('ICON_REVIEW_URL','http://127.0.0.1:8000'))
    args=parser.parse_args()
    base=args.server.rstrip('/')
    data=dict(mode=args.mission,name=args.name,prompt=args.prompt,family=args.family,model=args.model)
    try:
        if args.mission=='fix':
            if not args.icon:parser.error('fix requires --icon family/icon-id')
            with urlopen(base+'/gallery/icons.json',timeout=15) as response:
                icons=json.load(response)['icons']
            icon=next((icon for icon in icons if icon['key']==args.icon),None)
            if not icon:parser.error('Icon not found in the current gallery')
            data.update(icon=icon['key'],name=icon['name'],family=icon['family'],svg_sha256=icon['svg_sha256'])
        elif not args.name:
            parser.error('generate requires --name')
        request=Request(base+'/api/generation',data=json.dumps(data).encode(),headers={'Content-Type':'application/json'},method='POST')
        with urlopen(request,timeout=30) as response:
            row=json.load(response)
        print('Started '+row['mode']+' job '+row['id'])
        print('Review, accept or discard: '+base+'/gallery/generate.html#job-'+row['id'])
    except HTTPError as error:
        try:message=json.load(error).get('error',str(error))
        except ValueError:message='Server did not return JSON. Restart deploy.py.'
        parser.exit(1,message+'\n')
    except (URLError,ValueError) as error:
        parser.exit(1,'Could not reach the review server: '+str(error)+'\n')


if __name__=='__main__':
    main()
