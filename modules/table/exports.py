from typing import Optional

from app.table_data import table_data
from modules.table.schemas import Signatures


def get_data_from_table(id: str) -> Optional[Signatures]:
    try:
        return Signatures(**table_data.loc[id])
    except KeyError:
        return None
