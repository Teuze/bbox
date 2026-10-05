"""Script mitmproxy pour contourner CORS et déplacer BBOX-ID."""

# Cette manipulation est nécessaire pour utiliser swagger-ui comme client d'API Bbox.
# https://swagger.io/docs/specification/v3_0/authentication/cookie-authentication/
# https://swagger.io/docs/open-source-tools/swagger-ui/usage/limitations/
# https://swagger.io/docs/open-source-tools/swagger-ui/usage/cors/

from mitmproxy import http

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Expose-Headers": "*",
}


def request(flow: http.HTTPFlow):
    if flow.request.method == "OPTIONS":
        flow.response = http.Response.make(200, b"", CORS_HEADERS)
    if "X-BBOX-ID" in flow.request.headers:
        flow.request.cookies["BBOX_ID"] = flow.request.headers.pop("X-BBOX-ID")


def response(flow: http.HTTPFlow):
    if flow.response is not None:
        flow.response.headers.update(CORS_HEADERS)
        if "BBOX_ID" in flow.response.cookies:
            flow.response.headers["X-BBOX-ID"] = flow.response.cookies["BBOX_ID"][0]
