def parse_csp(csp_header):
    directives = {}

    if not csp_header:
        return directives

    # Her direktif boşlukla ayrılır: örn. "default-src 'self'; script-src 'unsafe-inline';"
    parts = csp_header.split(";")
    for part in parts:
        part = part.strip()
        if not part:
            continue
        pieces = part.split()
        directive = pieces[0]
        sources = pieces[1:] if len(pieces) > 1 else []
        directives[directive] = sources

    return directives
