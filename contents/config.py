
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
