from pathlib import Path
from datetime import datetime

Path(str(datetime.now().year) + '/days').mkdir(parents=True, exist_ok=True)
