
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
