python3 -c '
import urllib.parse

with open("searchablethings.txt", "r") as f:
    lines = f.read().splitlines()

html = [
    "<html>",
    "<head>",
    "  <title>MY SYSTEM MY RULES</title>",
    "  <style>",
    "    body { background: #111; color: #eee; font-family: monospace; padding: 20px; margin: 0; }",
    "    h1 { color: #00ff00; border-bottom: 2px solid #00ff00; padding-bottom: 10px; margin-bottom: 20px; font-size: 20px; }",
    "    form { margin: 0; padding: 6px; border-bottom: 1px solid #222; display: flex; align-items: center; white-space: nowrap; overflow: hidden; }",
    "    form:hover { background: #1a1a1a; }",
    "    button { background: #00ff00; color: #000; border: none; padding: 4px 10px; font-family: monospace; font-weight: bold; cursor: pointer; width: 45px; flex-shrink: 0; margin-right: 15px; }",
    "    button:hover { background: #fff; }",
    "    input[type=\"text\"] { background: #000; color: #00ff00; border: 1px solid #333; padding: 4px; font-family: monospace; width: 180px; flex-shrink: 0; margin-right: 20px; }",
    "    input[type=\"text\"]:focus { border-color: #00ff00; outline: none; }",
    "    .domain { color: #888; font-weight: bold; width: 220px; flex-shrink: 0; margin-right: 20px; overflow: hidden; text-overflow: ellipsis; display: inline-block; }",
    "    .url { color: #555; overflow: hidden; text-overflow: ellipsis; }",
    "  </style>",
    "</head>",
    "<body>",
    "  <h1>[ MASTER CONTROL SEARCH INTERFACE - CONFORMITY FREE ZONE ]</h1>"
]

for line in lines:
    line = line.strip()
    if not line: continue
    
    if "?" in line:
        base_url, query_string = line.split("?", 1)
        params = query_string.split("&")
        input_name = "q"
        hidden_inputs = []
        
        for p in params:
            if "=" in p:
                k, v = p.split("=", 1)
                if "{{{term}}}" in v:
                    input_name = k
                else:
                    hidden_inputs.append(f"<input type=\"hidden\" name=\"{k}\" value=\"{v}\">")
        
        hidden_html = "".join(hidden_inputs)
        
        try:
            display_name = urllib.parse.urlparse(line).netloc
        except:
            display_name = "SEARCH"
            
        html.append(
            f"  <form action=\"{base_url}\" method=\"GET\" target=\"_blank\">"
            f"    <button type=\"submit\">GO</button>"
            f"    <input type=\"text\" name=\"{input_name}\" placeholder=\"Search term...\">"
            f"    {hidden_html}"
            f"    <span class=\"domain\">{display_name}</span>"
            f"    <span class=\"url\">{line}</span>"
            f"  </form>"
        )
    else:
        html.append(
            f"  <form action=\"{line}\" method=\"GET\" target=\"_blank\">"
            f"    <button type=\"submit\">GO</button>"
            f"    <input type=\"text\" name=\"q\" placeholder=\"Search term...\">"
            f"    <span class=\"domain\">{line}</span>"
            f"    <span class=\"url\">{line}</span>"
            f"  </form>"
        )

html.append("</body>")
html.append("</html>")

with open("search.html", "w") as f:
    f.write("\n".join(html))
'
