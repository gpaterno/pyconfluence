import api as _api
import json as _json


def get_page_content(id):
    print _json.loads(_api.rest(id + "?expand=body.storage"))["body"]["storage"]["value"]


if __name__ == "__main__":
    get_content("57869261")
