class GenomeLinkError(Exception):
    pass

class OAuthError(GenomeLinkError):
    """cf. https://github.com/oauthlib/oauthlib oauthlib/oauth2/rfc6749/errors.py"""
    error = None
    description = ''

    def __init__(self, description=None):
        if description is not None:
            self.description = description
        message = '(%s) %s' % (self.error, self.description)
        super(OAuthError, self).__init__(message)

class TokenExpiredError(OAuthError):
    error = 'token_expired'

class InsecureTransportError(OAuthError):
    error = 'insecure_transport'
    description = 'OAuth 2 MUST utilize https.'

class MismatchingStateError(OAuthError):
    error = 'mismatching_state'
    description = 'CSRF Warning! State not equal in request and response.'

class MissingCodeError(OAuthError):
    error = 'missing_code'

class MissingTokenError(OAuthError):
    error = 'missing_token'

class MissingTokenTypeError(OAuthError):
    error = 'missing_token_type'

class FatalClientError(OAuthError):
    """
    Errors during authorization where user should not be redirected back.
    """
    pass

class InvalidRequestError(OAuthError):
    """
    The request is missing a required parameter, includes an invalid
    parameter value, includes a parameter more than once, or is
    otherwise malformed.
    """
    error = 'invalid_request'
    description = __doc__

class AccessDeniedError(OAuthError):
    """
    The resource owner or authorization server denied the request.
    """
    error = 'access_denied'
    description = __doc__

class UnsupportedResponseTypeError(OAuthError):
    """
    The authorization server does not support obtaining an authorization
    code using this method.
    """
    error = 'unsupported_response_type'
    description = __doc__

class InvalidScopeError(OAuthError):
    """
    The requested scope is invalid, unknown, or malformed.
    """
    error = 'invalid_scope'
    description = __doc__

class ServerError(OAuthError):
    """
    The authorization server encountered an unexpected condition that
    prevented it from fulfilling the request.
    """
    error = 'server_error'
    description = __doc__

class TemporarilyUnavailableError(OAuthError):
    """
    The authorization server is currently unable to handle the request
    due to a temporary overloading or maintenance of the server.
    """
    error = 'temporarily_unavailable'
    description = __doc__

class InvalidClientError(OAuthError):
    """
    Either your client_id or client_secret is invalid.
    """
    error = 'invalid_client'
    description = __doc__

class InvalidGrantError(OAuthError):
    """
    The provided authorization grant (e.g. authorization code)
    or refresh token is invalid, expired, revoked, does
    not match the redirection URI used in the authorization request, or was
    issued to another client.
    You can generate multiple access tokens, but you can only use the latest
    generated refresh_token.
    """
    error = 'invalid_grant'
    description = __doc__

class UnauthorizedClientError(OAuthError):
    """
    The authenticated client is not authorized to use this authorization
    grant type.
    """
    error = 'unauthorized_client'
    description = __doc__

class UnsupportedGrantTypeError(OAuthError):
    """
    The authorization server does not support obtaining an authorization
    code using this method.
    """
    error = 'unsupported_grant_type'
    description = __doc__

class UnsupportedTokenTypeError(OAuthError):
    """
    The authorization server does not support the revocation of the
    presented token type.  I.e. the client tried to revoke an access token
    on a server not supporting this feature.
    """
    error = 'unsupported_token_type'
    description = __doc__

class InvalidTokenError(OAuthError):
    """
    The access token provided is expired, revoked, malformed,
    or invalid for other reasons.
    """
    error = 'invalid_token'
    description = __doc__

class InsufficientScopeError(OAuthError):
    """
    The request requires higher privileges than provided by
    the access token.
    """
    error = 'insufficient_scope'
    description = __doc__

_oauth_errors = [
    TokenExpiredError,
    InsecureTransportError,
    MismatchingStateError,
    MissingCodeError,
    MissingTokenError,
    MissingTokenTypeError,
    FatalClientError,
    InvalidRequestError,
    AccessDeniedError,
    UnsupportedResponseTypeError,
    InvalidScopeError,
    ServerError,
    TemporarilyUnavailableError,
    InvalidClientError,
    InvalidGrantError,
    UnauthorizedClientError,
    UnsupportedGrantTypeError,
    UnsupportedTokenTypeError,
    InvalidTokenError,
    InsufficientScopeError,
]
_oauth_error_codes = {e.error:e for e in _oauth_errors}

def raise_oauth_error(error_code):
    error = _oauth_error_codes.get(error_code)
    if error:
        raise error
