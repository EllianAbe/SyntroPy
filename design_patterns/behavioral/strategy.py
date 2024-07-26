from abc import ABC, abstractmethod


class AuthenticationStrategy(ABC):
    @abstractmethod
    def authenticate(self, *args, **kwargs):
        pass


class BasicAuthentication(AuthenticationStrategy):
    def authenticate(self, username, password):
        pass


class OAuth1Authentication(AuthenticationStrategy):
    def authenticate(self, consumer_key, consumer_secret, token, token_secret):
        pass


class OAuth2Authentication(AuthenticationStrategy):
    def authenticate(self, access_token):
        pass


class APIKeyAuthentication(AuthenticationStrategy):
    def authenticate(self, api_key):
        pass


class JWTAuthentication(AuthenticationStrategy):
    def authenticate(self, payload, secret, algorithm='HS256'):
        pass


class HMACAuthentication(AuthenticationStrategy):
    def authenticate(self, client_id, client_secret):
        pass


class DigestAuthentication(AuthenticationStrategy):
    def authenticate(self, username, password, realm, nonce, uri, qop, nc, cnonce):
        pass


class HawkAuthentication(AuthenticationStrategy):
    def authenticate(self, id, key, algorithm):
        pass
