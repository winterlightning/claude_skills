# The gallery's Python graphics code (edit geometry, validation, SVG render) for the Worker.
# Build context is the repository root (wrangler.jsonc image_build_context); see the root .dockerignore.
FROM --platform=linux/amd64 python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends libcairo2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY icon_set/requirements-qa.txt /app/requirements-qa.txt
RUN pip install --no-cache-dir -r /app/requirements-qa.txt
# The side-combination engine (vendor/combination) runs as a subprocess of combination_experiment.render.
COPY icon_set/vendor/combination/requirements.txt /app/requirements-combination.txt
RUN pip install --no-cache-dir -r /app/requirements-combination.txt svgpathtools

# Only the modules the edit, validation and render paths import; authored icon modules stay out.
COPY icon_set /app/icon_set
COPY cloud/graphics/server.py /app/server.py

ENV PYTHONPATH=/app PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8080
EXPOSE 8080
CMD ["python", "/app/server.py"]
