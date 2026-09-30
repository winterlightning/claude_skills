#!/usr/bin/env python3
"""The Python graphics work the Worker cannot do, as a stateless HTTP service inside a Cloudflare Container.

Every request carries what it needs (the icon's baseline graph, the stored documents, the user) and gets back
a document or an SVG; nothing is stored here. Combinations are built in the browser (combine.js, combine-side.js),
not here. The functions are the gallery's own (icon_set/scripts), so the
cloud and a local deploy.py compute identical edits, validation reports and drawings.

    POST /edit      {icon, data, old, user}        -> the stroke-edit document to store (stroke_edits.build_edit_document)
    POST /validate  {icon, data}                   -> validation report of the edited graph (stroke_edits.validate_edit)
    POST /render    {graph}                        -> {svg, svg_sha256}
    POST /artwork   {icon, data, old, edit, user}  -> {choice, selected}: the artwork choice to store and its drawing
    GET  /health
"""
from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import traceback

from icon_set.scripts.edit_validation import icon_from_graph
from icon_set.scripts.icon_artwork import baseline, build_artwork_choice, resolve_artwork, sha
from icon_set.scripts.stroke_edits import EditConflict, GRAPH_FIELDS, build_edit_document, validate_edit

MAX_BODY = 4 * 1024 * 1024


def render(graph: dict) -> dict:
    document = icon_from_graph(graph).to_svg()
    return {'svg': document, 'svg_sha256': sha(document)}


def artwork(icon: dict, data: dict, old: dict | None, edit: dict | None, user: str) -> dict:
    choice = build_artwork_choice(icon, data, old, edit, user)
    selected = resolve_artwork(baseline(icon), choice)
    if selected is None:  # use_org: the generated drawing is already stored
        return {'choice': choice, 'selected': None}
    graph = selected['graph']
    return {'choice': choice, 'selected': {
        'svg': selected['svg'], 'svg_sha256': selected['svg_sha256'], 'source_mode': selected['source_mode'],
        'graph': {k: graph[k] for k in GRAPH_FIELDS if k in graph} if graph else None,
        'validation_override': selected['validation_override'], 'automatic_status': selected['automatic_status']}}


ROUTES = {
    '/edit': lambda b: build_edit_document(b['icon'], b['data'], b.get('old'), b['user']),
    '/validate': lambda b: validate_edit(b['icon'], b['data']),
    '/render': lambda b: render(b['graph']),
    '/artwork': lambda b: artwork(b['icon'], b['data'], b.get('old'), b.get('edit'), b['user']),
}


class Handler(BaseHTTPRequestHandler):
    def reply(self, status: int, payload) -> None:
        body = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == '/health':
            return self.reply(200, {'ok': True})
        return self.reply(404, {'error': 'Not found'})

    def do_POST(self):
        route = ROUTES.get(self.path)
        if route is None:
            return self.reply(404, {'error': 'Not found'})
        length = int(self.headers.get('Content-Length') or 0)
        if length <= 0 or length > MAX_BODY:
            return self.reply(413, {'error': 'Request body is empty or too large.'})
        try:
            body = json.loads(self.rfile.read(length))
            if not isinstance(body, dict):
                raise ValueError('A JSON object is required.')
            return self.reply(200, route(body))
        except EditConflict as error:
            return self.reply(409, {'error': str(error)})
        except (ValueError, TypeError) as error:
            return self.reply(400, {'error': str(error)})
        except KeyError as error:
            # Same wording as deploy.py: a catalog record without the fields validation needs.
            return self.reply(400, {'error': 'The catalog is missing geometry metadata required for validation: ' + str(error)})
        except Exception as error:  # noqa: BLE001 - report, never crash the service
            traceback.print_exc()
            return self.reply(500, {'error': f'Graphics service error: {type(error).__name__}: {error}'})

    def log_message(self, format, *args):  # one line per request on stdout (wrangler tail / dashboard logs)
        print(f'{self.command} {self.path} -> ' + (format % args), flush=True)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8080'))
    print(f'graphics service on :{port}', flush=True)
    ThreadingHTTPServer(('0.0.0.0', port), Handler).serve_forever()
