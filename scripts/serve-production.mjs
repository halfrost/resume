import { createReadStream, existsSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { extname, join, normalize } from "node:path";
import { createBrotliCompress, constants as zlibConstants } from "node:zlib";

const root = normalize(process.env.SITE_DIR || join(process.cwd(), "public"));
const host = process.env.HOST || "127.0.0.1";
const port = Number(process.env.PORT || 1313);

const contentTypes = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".ico": "image/x-icon",
  ".jpeg": "image/jpeg",
  ".jpg": "image/jpeg",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".pdf": "application/pdf",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".webmanifest": "application/manifest+json; charset=utf-8",
  ".webp": "image/webp",
  ".woff2": "font/woff2",
  ".xml": "application/xml; charset=utf-8",
};

const compressible = /^(application\/(javascript|json|xml)|text\/)/;
const immutablePath = /^\/(?:css|dist|js|legacy-media)\//;
const cachedMediaPath = /^\/(?:images|media)\//;

function resolveFile(urlPath) {
  const decoded = decodeURIComponent(urlPath);
  const relative = decoded.replace(/^\/+/, "");
  let filePath = normalize(join(root, relative));

  if (!filePath.startsWith(root)) return null;
  if (decoded.endsWith("/")) filePath = join(filePath, "index.html");
  if (existsSync(filePath) && statSync(filePath).isDirectory()) {
    filePath = join(filePath, "index.html");
  }
  return existsSync(filePath) && statSync(filePath).isFile() ? filePath : null;
}

createServer((request, response) => {
  const url = new URL(request.url || "/", `http://${request.headers.host || host}`);
  const filePath = resolveFile(url.pathname);

  if (!filePath) {
    response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
    response.end("Not found");
    return;
  }

  const contentType = contentTypes[extname(filePath).toLowerCase()] || "application/octet-stream";
  const headers = {
    "Content-Type": contentType,
    "Cross-Origin-Opener-Policy": "same-origin",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Vary": "Accept-Encoding",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
  };

  if (immutablePath.test(url.pathname)) {
    headers["Cache-Control"] = "public, max-age=31536000, immutable";
  } else if (cachedMediaPath.test(url.pathname)) {
    headers["Cache-Control"] = "public, max-age=2592000";
  } else {
    headers["Cache-Control"] = "no-cache";
  }

  const useBrotli =
    request.method !== "HEAD" &&
    compressible.test(contentType) &&
    request.headers["accept-encoding"]?.includes("br");

  if (useBrotli) headers["Content-Encoding"] = "br";
  response.writeHead(200, headers);
  if (request.method === "HEAD") {
    response.end();
    return;
  }

  const source = createReadStream(filePath);
  if (useBrotli) {
    source
      .pipe(createBrotliCompress({
        params: {
          [zlibConstants.BROTLI_PARAM_QUALITY]: 4,
        },
      }))
      .pipe(response);
  } else {
    source.pipe(response);
  }
}).listen(port, host, () => {
  console.log(`Production preview: http://${host}:${port}/`);
});
