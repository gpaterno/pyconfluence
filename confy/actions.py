import api as _api
import json as _json


def get_page_content(id):
    """Return XHTML content of a page.

    Parameters:
    - id: id of a Confluence page.
    """
    data = _json.loads(_api.rest(id + "?expand=body.storage"))
    return data["body"]["storage"]["value"]
