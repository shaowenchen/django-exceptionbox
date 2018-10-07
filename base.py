# -*- coding: utf-8 -*-
from abc import ABCMeta


class BaseReturn(Exception):
    __metaclass__ = ABCMeta


# 1XX Informational
class Continue100(BaseReturn):
    status_code = 100


class SwitchingProtocols101(BaseReturn):
    status_code = 101


class Processing102(BaseReturn):
    status_code = 102


# 2XX Success
class OK200(BaseReturn):
    status_code = 200


class Created201(BaseReturn):
    status_code = 201


class Accepted202(BaseReturn):
    status_code = 202


class NonAuthoritativeInformation203(BaseReturn):
    status_code = 203


class NoContent204(BaseReturn):
    status_code = 204


class ResetContent205(BaseReturn):
    status_code = 205


class PartialContent206(BaseReturn):
    status_code = 206


class MultiStatus207(BaseReturn):
    status_code = 207


class AlreadyReported208(BaseReturn):
    status_code = 208


class IMUsed226(BaseReturn):
    status_code = 226


# 3XX Redirection
class MultipleChoices300(BaseReturn):
    status_code = 300


class MovedPermanently301(BaseReturn):
    status_code = 301


class Found302(BaseReturn):
    status_code = 302


class SeeOther303(BaseReturn):
    status_code = 303


class NotModified304(BaseReturn):
    status_code = 304


class UseProxy305(BaseReturn):
    status_code = 305


class TemporaryRedirect307(BaseReturn):
    status_code = 307


class PermanentRedirect308(BaseReturn):
    status_code = 308


class Accepted202(BaseReturn):
    status_code = 202


# 4XX Client Error
class BadRequest400(BaseReturn):
    status_code = 400


class Unauthorized401(BaseReturn):
    status_code = 401


class PaymentRequired402(BaseReturn):
    status_code = 402


class Forbidden403(BaseReturn):
    status_code = 403


class NotFound404(BaseReturn):
    status_code = 404


class MethodNotAllowed405(BaseReturn):
    status_code = 405


class NotAcceptable406(BaseReturn):
    status_code = 406


class ProxyAuthenticationRequired407(BaseReturn):
    status_code = 407


class RequestTimeout408(BaseReturn):
    status_code = 408


class Conflict409(BaseReturn):
    status_code = 409


class Gone410(BaseReturn):
    status_code = 410


class LengthRequired411(BaseReturn):
    status_code = 411


class PreconditionFailed412(BaseReturn):
    status_code = 412


class PayloadTooLarge413(BaseReturn):
    status_code = 413


class RequestURITooLong414(BaseReturn):
    status_code = 414


class UnsupportedMediaType415(BaseReturn):
    status_code = 415


class RequestedRangeNotSatisfiable416(BaseReturn):
    status_code = 416


class ExpectationFailed417(BaseReturn):
    status_code = 417


class IMATeapot418(BaseReturn):
    status_code = 418


class MisdirectedRequest421(BaseReturn):
    status_code = 421


class UnprocessableEntity422(BaseReturn):
    status_code = 422


class Locked423(BaseReturn):
    status_code = 423


class FailedDependency424(BaseReturn):
    status_code = 424


class UpgradeRequired426(BaseReturn):
    status_code = 426


class PreconditionRequired428(BaseReturn):
    status_code = 428


class TooManyRequests429(BaseReturn):
    status_code = 429


class PreconditionRequired428(BaseReturn):
    status_code = 428


class RequestHeaderFieldsTooLarge431(BaseReturn):
    status_code = 431


class ConnectionClosedWithoutResponse444(BaseReturn):
    status_code = 444


class UnavailableForLegalReasons451(BaseReturn):
    status_code = 451


class ClientClosedRequest499(BaseReturn):
    status_code = 499


# 5XX Server Error

class InternalServerError500(BaseReturn):
    status_code = 500


class NotImplemented501(BaseReturn):
    status_code = 501


class BadGateway502(BaseReturn):
    status_code = 502


class ServiceUnavailable503(BaseReturn):
    status_code = 503


class GatewayTimeout504(BaseReturn):
    status_code = 504


class HTTPVersionNotSupported505(BaseReturn):
    status_code = 505


class VariantAlsoNegotiates506(BaseReturn):
    status_code = 506


class InsufficientStorage507(BaseReturn):
    status_code = 507


class LoopDetected508(BaseReturn):
    status_code = 508


class NotExtended510(BaseReturn):
    status_code = 510


class NetworkAuthenticationRequired511(BaseReturn):
    status_code = 511


class NetworkConnectTimeoutError599(BaseReturn):
    status_code = 599
