class Config(object):
    """Common Configuration."""

    def __init__(self, arg):
        super(Config, self).__init__()
        self.arg = arg


class DevelopmentConfig(Config):
    """Put all Development level Configuration."""

    DEBUG = True
    SQLALCHEMY_ECHO = True
    APP_PORT = 9090

    def __init__(self, arg):
        super(DevelopmentConfig, self).__init__()
        self.arg = arg
        APP_PORT = 9090
        DEBUG = True
        SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """Put all Production level Configuration."""
    APP_PORT = 9090

    def __init__(self, arg):
        super(ProductionConfig, self).__init__()
        self.arg = arg
        APP_PORT = 9090
        DEBUG = False


app_config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
