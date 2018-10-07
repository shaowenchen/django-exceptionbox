# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import base


class ERROR_LOGIN_FRONT_NOT_GIFT(base.PreconditionFailed412):
    message = u"礼品不充足"


class ERROR_LOGIN_FRONT_PAY_NOT_MONEY(base.PreconditionFailed412):
    message = u"没有足够余额"


class ERROR_FAULT(base.ServiceUnavailable503):
    message = u"服务器内部错误"
