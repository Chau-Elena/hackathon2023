
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
OPENAI_API_KEY = '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'
