# -*- coding: utf-8 -*-
import json
import logging
import traceback

from django.http import JsonResponse

from .base import BaseReturn

logger = logging.getLogger('root')


class ExceptionBoxMiddleware(object):
    def process_exception(self, request, exception):
        if not issubclass(exception.__class__, BaseReturn):
            return None
        ret_json = {
            'code': exception.__class__.__name__,
            'message': getattr(exception, 'message', ''),
            'result': False,
            'data': ''
        }
        response = JsonResponse(ret_json)
        response.status_code = getattr(exception, 'status_code', 500)
        _logger = logger.error if response.status_code >= 500 else logger.warning
        _logger('status_code->{status_code}, error_code->{code}, url->{url}, '
                'method->{method}, param->{param}, '
                'body->{body}，traceback->{traceback}'.format(
            status_code=response.status_code, code=ret_json['code'], url=request.path,
            method=request.method, param=json.dumps(getattr(request, request.method, {})),
            body=request.body, traceback=traceback.format_exc()
        ))
        return response
