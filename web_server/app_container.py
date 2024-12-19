from dependency_injector import containers, providers


class InventoryAppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
