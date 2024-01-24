"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.buyer_dao import BuyerDAO
from .orders.purchase_dao import PurchaseDAO
from .orders.robopatrol_dao import RoboPatrolDAO
from .orders.robopatrol_developer_dao import RoboPatrolDeveloperDAO
from .orders.sensor_dao import SensorDAO
from .orders.sensor_developer_dao import SensorDeveloperDAO
from .orders.shop_dao import ShopDAO
from .orders.webcam_dao import WebcamDAO
from .orders.webcam_developer_dao import WebcamDeveloperDAO


buyer_dao = BuyerDAO()
purchase_dao = PurchaseDAO()
robopatrol_dao = RoboPatrolDAO()
robopatrol_developer_dao = RoboPatrolDeveloperDAO()
sensor_dao = SensorDAO()
sensor_developer_dao = SensorDeveloperDAO()
shop_dao = ShopDAO()
webcam_dao = WebcamDAO()
webcam_developer_dao = WebcamDeveloperDAO()
