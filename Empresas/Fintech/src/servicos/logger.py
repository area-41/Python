import logging
import os


# Garante que a pasta de logs exista
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=os.path.join("logs", "app.log"),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("FintechLogger")
