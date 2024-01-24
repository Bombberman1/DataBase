"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.buyer_controller import BuyerController
from .orders.purchase_controller import PurchaseController
from .orders.robopatrol_controller import RoboPatrolController
from .orders.robopatrol_developer_controller import RoboPatrolDeveloperController
from .orders.sensor_controller import SensorController
from .orders.sensor_developer_controller import SensorDeveloperController
from .orders.shop_controller import ShopController
from .orders.webcam_controller import WebcamController
from .orders.webcam_developer_controller import WebcamDeveloperController

buyer_controller = BuyerController()
purchase_controller = PurchaseController()
robopatrol_controller = RoboPatrolController()
robopatrol_developer_controller = RoboPatrolDeveloperController()
sensor_controller = SensorDeveloperController()
sensor_developer_controller = BuyerController()
shop_controller = ShopController()
webcam_controller = WebcamController()
webcam_developer_controller = WebcamDeveloperController()
