from dependency_injector import containers, providers
from services import wrf_service


class InventoryAppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    connection_settings = providers.Singleton(
        wrf_service.ConnectionSettings,
        hostname=config.hostname,
        username=config.username,
        password=config.password,
    )

    service = providers.Singleton(
        wrf_service.SSHWRFService,
        settings=connection_settings,
        namelist_remote_path=config.namelist_remote_path,
    )
