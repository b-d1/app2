# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import connexion
import logging
from flask import request
from flask_cors import CORS
from logging.config import dictConfig

from app2 import commands
from app2.extensions import db, migrate, ma

dictConfig({
    'version': 1,
    'formatters': {
        'request_formatter': {
            'format': '\n***************\n'
            'Logger level: %(levelname)s\n'
            'Module: %(module)s\n'
            'Request time: %(asctime)s\n'
            '%(message)s',
        },
        'response_formatter': {
            'format': '---------------\n'
            'Response time: %(asctime)s\n%(message)s\n'
        }
    },
    'handlers': {
        'request': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'request_formatter'
        },
        'response': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'response_formatter'
        }
    },
    'loggers': {
        'request': {
            'level': 'INFO',
            'handlers': ['request']
        },
        'response': {
            'level': 'INFO',
            'handlers': ['response']
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': []
    }
})


def create_app(config_object='app2.settings'):
    """
    An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    connexion_app = connexion.FlaskApp(__name__.split('.')[0])
    app = connexion_app.app
    app.config.from_object(config_object)
    connexion_app.add_api('apis/api_spec.yaml')
    CORS(app)

    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    # app.register_blueprint(views.test1.blueprint)
    return None


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {'db': db}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
