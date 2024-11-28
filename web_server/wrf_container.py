import wrf_service
from dependency_injector import containers, providers


class WRFContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    namelist_paths = providers.Singleton(
        wrf_service.NamelistPaths,
        local_path=config.namelist_local_path,
        remote_path=config.namelist_remote_path,
    )

    namelist_sender = providers.Singleton(
        wrf_service.SFTPNamelistSender,
        namelist_file_path="/",
    )

    connection_settings = providers.Singleton(
        wrf_service.ConnectionSettings,
        hostname=config.hostname,
        username=config.username,
        password=config.password,
    )

    service = providers.Singleton(
        wrf_service.SSHWRFService,
        settings=connection_settings,
        namelist_sender=namelist_sender,
    )
