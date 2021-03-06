# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from requests.auth import HTTPBasicAuth
from .resource_mapping import RESOURCE_MAPPING


class KigoClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://app.kigo.net/api/ra/v1/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(KigoClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        
        params['auth'] = HTTPBasicAuth(
            api_params.get('user'), api_params.get('password'))
        

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        pass


Kigo = generate_wrapper_from_adapter(KigoClientAdapter)
