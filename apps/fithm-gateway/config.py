from .settings import (
    LOG_CONFIG,
    FITHM_SMTP_HOST,
    FITHM_SMTP_PORT,
    FITHM_SMTP_USER,
    FITHM_SMTP_PASS,
    FITHM_ADMIN_MAIL,
    FITHM_ADMIN_PASS,
    FITHM_SERVICE_URL,
    GATEWAY_SEC_KEY,
    DEBUG
)
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'root': LOG_CONFIG
})

class Config:
    """General Configuration"""

    # flask mail service
    MAIL_SERVER = FITHM_SMTP_HOST
    MAIL_PORT = FITHM_SMTP_PORT
    MAIL_USERNAME = FITHM_SMTP_USER
    MAIL_PASSWORD = FITHM_SMTP_PASS
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    ADMIN_MAIL_USER = FITHM_ADMIN_MAIL
    ADMIN_MAIL_PASS = FITHM_ADMIN_PASS

    ALLOWED_FILES = ['png', 'jpg', 'jpeg', 'gif']

    SERVICE_URL = FITHM_SERVICE_URL
    SECURITY_KEY = GATEWAY_SEC_KEY
    DEBUG = DEBUG
