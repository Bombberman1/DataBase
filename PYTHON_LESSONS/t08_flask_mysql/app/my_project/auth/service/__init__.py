"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.buyer_service import BuyerService
from .orders.purchase_service import PurchaseService
from .orders.robopatrol_developer_service import RoboPatrolDeveloperService
from .orders.robopatrol_service import RoboPatrolService
from .orders.sensor_developer_service import SensorDeveloperService
from .orders.sensor_service import SensorService
from .orders.shop_service import ShopService
from .orders.webcam_developer_service import WebcamDeveloperService
from .orders.webcam_service import WebcamService

buyer_service = BuyerService()
purchase_service = PurchaseService()
robopatrol_developer_service = RoboPatrolDeveloperService()
robopatrol_service = RoboPatrolService()
sensor_developer_service = SensorDeveloperService()
sensor_service = SensorService()
shop_service = ShopService()
webcam_developer_service = WebcamDeveloperService()
webcam_service = WebcamService()
