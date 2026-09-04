ACRONYMS = {
    "gb": "GB",
    "id": "ID",
    "mb": "MB",
    "tb": "TB",
    "api": "API",
    "url": "URL",
    "uri": "URI",
    "iops": "IOPS",
}

def render_to_camel(value: str) -> str:
    parts = value.split("_")

    return parts[0] + "".join(
        ACRONYMS.get(part, part.capitalize())
        for part in parts[1:]
    )