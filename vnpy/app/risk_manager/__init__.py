from pathlib import Path
from vnpy.trader.app import BaseApp
from .engine import RiskManagerEngine, APP_NAME


class RiskManagerApp(BaseApp):
    """"""
    app_name = APP_NAME
    app_module = __module__
    app_path = Path(__file__).parent
    display_name = " transaction risk control "
    engine_class = RiskManagerEngine
    widget_name = "RiskManager"
    icon_name = "rm.ico"
