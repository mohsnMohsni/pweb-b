# Third-party imports.
from rest_framework.routers import Route, DynamicRoute, DefaultRouter


class MainRouter(DefaultRouter):

    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'},
        ),
        Route(
            url=r'^{prefix}/add{trailing_slash}$',
            mapping={'post': 'create'},
            name='{basename}-add',
            detail=False,
            initkwargs={'suffix': 'add'},
        ),
        DynamicRoute(
            url=r'^{prefix}/{url_path}{trailing_slash}$', name='{basename}-{url_name}', detail=False, initkwargs={}
        ),
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'},
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={},
        ),
    ]
