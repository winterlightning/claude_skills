#!/usr/bin/env python3
"""The Python graphics work the Worker cannot do, as a stateless HTTP service inside a Cloudflare Container.

Every request carries what it needs (the icon's baseline graph, the stored documents, the user) and gets back
a document or an SVG; nothing is stored here. The functions are the gallery's own (icon_set/scripts), so the
cloud and a local deploy.py compute identical edits, validation reports and drawings.

    POST /edit      {icon, data, old, user}        -> the stroke-edit document to store (stroke_edits.build_edit_document)
    POST /validate  {icon, data}                   -> validation report of the edited graph (stroke_edits.validate_edit)
    POST /render    {graph}                        -> {svg, svg_sha256}
    POST /artwork   {icon, data, old, edit, user}  -> {choice, selected}: the artwork choice to store and its drawing
    POST /side/render {row, main, sub, documents, layout, elements}
                                                   -> one side pair combined (combination_experiment.render) with
                                                      the current main / sub drawings in `documents`
    POST /side/apply  {row, main, sub, layout, documents, targets: [{row, sub, documents}]}
                                                   -> {results: [{pair_id, ok, layout, result} | {pair_id, ok, error}]}:
                                                      the layout moved onto other pairs with the same main
    GET  /health
"""
from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import threading
import traceback

from icon_set.scripts.edit_validation import icon_from_graph
from icon_set.scripts.icon_artwork import baseline, build_artwork_choice, resolve_artwork, sha
from icon_set.scripts.stroke_edits import EditConflict, GRAPH_FIELDS, build_edit_document, validate_edit

MAX_BODY = 16 * 1024 * 1024  # /side/apply carries up to 200 pair rows


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


def side_pair(row: dict, main: str | None, sub: str | None, documents: dict | None) -> tuple[dict, dict]:
    from icon_set.scripts.side_recombine import pair_with_documents
    return pair_with_documents(row, main, sub, documents)


def side_render(body: dict) -> dict:
    from icon_set.scripts.combination_experiment import render
    row, chosen = side_pair(body['row'], body.get('main'), body.get('sub'), body.get('documents'))
    request = {'id': row['id'], **chosen, **{k: body[k] for k in ('layout', 'elements') if body.get(k) is not None}}
    return render(request, row=row)


def container_render(body: dict) -> dict:
    """A container pair's combined icon (container_combination_render): the container with its symbol on the grid."""
    from icon_set.scripts.container_combination_render import render as combine
    return combine(body['main'], body['symbol'], body['center'], body.get('ink'))


def side_apply(body: dict) -> dict:
    """deploy.py apply_side_layout without the saving: each target's moved layout and its render."""
    from icon_set.scripts.combination_experiment import default_groups
    from icon_set.scripts.combination_layouts import transfer
    source = body['row']
    _, chosen = side_pair(source, body.get('main'), body.get('sub'), None)
    results = []
    for target in body.get('targets') or []:
        row = target.get('row') or {}
        try:
            if not row or row.get('id') == source['id']:
                raise ValueError('Not an available side pair.')
            if not any(m['icon'] == chosen['main'] for m in row['mains']):
                raise ValueError('This pair does not use the same main.')
            sub = target.get('sub') or row['subs'][0]['icon']
            if not any(s['icon'] == sub for s in row['subs']):
                raise ValueError('The sub does not belong to this pair.')
            # The target's own sub groups from the drawings it is rendered with, not the published ones.
            current, _ = side_pair(row, chosen['main'], sub, target.get('documents'))
            canvas, groups = default_groups(current, chosen['main'], sub)
            moved = transfer(body['layout'], source['position'], chosen['sub'], row['position'], sub, canvas, groups.get('sub'))
            if not moved:
                raise ValueError('Nothing to apply.')
            result = side_render({'row': row, 'main': chosen['main'], 'sub': sub, 'documents': target.get('documents'), 'layout': moved})
            results.append({'pair_id': row['id'], 'ok': True, 'sub': sub, 'layout': moved, 'result': result})
        except (ValueError, KeyError) as error:
            results.append({'pair_id': row.get('id'), 'ok': False, 'error': str(error) or 'Could not apply the layout.'})
    return {'results': results}


# Combining runs subprocesses that need the whole (small) CPU: one at a time, the rest wait their turn
# instead of slowing each other past the engine's timeouts.
_COMBINE = threading.Lock()


def one_at_a_time(handler):
    def run(body):
        with _COMBINE:
            return handler(body)
    return run


ROUTES = {
    '/edit': lambda b: build_edit_document(b['icon'], b['data'], b.get('old'), b['user']),
    '/validate': lambda b: validate_edit(b['icon'], b['data']),
    '/render': lambda b: render(b['graph']),
    '/artwork': lambda b: artwork(b['icon'], b['data'], b.get('old'), b.get('edit'), b['user']),
    '/side/render': one_at_a_time(side_render),
    '/side/apply': one_at_a_time(side_apply),
    '/container/render': one_at_a_time(container_render),
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
