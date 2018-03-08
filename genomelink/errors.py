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
    prevented it from fulfilling the request.  (This error code is needed
    because a 500 Internal Server Error HTTP status code cannot be returned
    to the client via a HTTP redirect.)
    """
    error = 'server_error'
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

_oauth_errors = [
    # TokenExpiredError,
    # InsecureTransportError,
    # MismatchingStateError,
    # MissingCodeError,
    # MissingTokenError,
    # MissingTokenTypeError,
    # FatalClientError,
    InvalidRequestError,
    AccessDeniedError,
    UnsupportedResponseTypeError,
    InvalidScopeError,
    ServerError,
    # TemporarilyUnavailableError,
    InvalidClientError,
    InvalidGrantError,
    UnauthorizedClientError,
    UnsupportedGrantTypeError,
    # UnsupportedTokenTypeError,
    # OpenIDClientError,
    # InvalidTokenError,
    # InsufficientScopeError,
]
_oauth_error_codes = {e.error:e for e in _oauth_errors}

def raise_oauth_error(error_code):
    error = _oauth_error_codes.get(error_code)
    if error:
        raise error
