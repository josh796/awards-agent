def format_email(results):
    html = "<h2>Weekly Awards Digest</h2>"
    html += "<ul>"

    if not results:
        html += "<li>No results returned — check API</li>"

    for r in results:
        title = r.get("title", "Unknown award")
        url = r.get("url", "#")

        html += f"""
        <li>
            <strong>{title}</strong><br>
            <a href="{url}">Visit Website</a>
        </li>
        """

    html += "</ul>"
    return html
``
