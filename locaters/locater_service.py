from functools import cached_property

from locaters.lambda_download import LambdaDownload
from locaters.lambda_table_locater import LambdaTable


class LocatorService:
    def __init__(self):
        pass

    @cached_property
    def lambda_table(self) -> LambdaTable:
        return LambdaTable()

    @cached_property
    def lambda_download(self) -> LambdaDownload:
        return LambdaDownload()



