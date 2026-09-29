// pictographic-graphics: hosts the Python graphics container (server.py) for the pictographic-review Worker.
// Not public (workers_dev false, no routes): only the review Worker reaches it through its GRAPHICS service binding.
import { Container, getContainer } from "@cloudflare/containers";

export class GraphicsContainer extends Container {
  defaultPort = 8080;
  // Stay warm through an editing session; asleep costs nothing.
  sleepAfter = "10m";
}

// Bump when server.py or the code it runs changes: an instance keeps the image it started with, so a new name
// starts from the image just deployed instead of waiting for the old instance to roll over.
const INSTANCE = "main-5";

export default {
  async fetch(request, env) {
    // One named instance: edits are rare and a warm instance answers in well under a second.
    return getContainer(env.GRAPHICS, INSTANCE).fetch(request);
  },
};
