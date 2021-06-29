"""Scholarly Encoder
Encoder for converting set, scholarly data types to json format
"""

import json
import scholarly.data_types as data_types


class ScholarlyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, data_types.AuthorSource):
            return None
        if isinstance(obj, data_types.PublicationSource):
            return None
        return json.JSONEncoder.default(self, obj)
