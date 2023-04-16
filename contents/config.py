
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
