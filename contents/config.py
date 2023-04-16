
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

OPENAI_API_KEY = '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'
