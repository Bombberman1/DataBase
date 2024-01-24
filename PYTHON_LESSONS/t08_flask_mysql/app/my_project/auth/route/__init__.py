"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.sensor_developer_route import sensor_dev_bp
    from .orders.sensor_route import sensor_bp
    from .orders.buyer_route import buyer_bp
    from .orders.purchase_route import purchase_bp
    from .orders.robopatrol_developer_route import robo_patrol_developer_bp
    from .orders.robopatrol_route import robo_patrol_bp
    from .orders.shop_route import shop_bp
    from .orders.webcam_developer_route import webcam_dev_bp
    from .orders.webcam_route import webcam_bp

    app.register_blueprint(sensor_dev_bp)
    app.register_blueprint(sensor_bp)
    app.register_blueprint(buyer_bp)
    app.register_blueprint(purchase_bp)
    app.register_blueprint(robo_patrol_developer_bp)
    app.register_blueprint(robo_patrol_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(webcam_dev_bp)
    app.register_blueprint(webcam_bp)
