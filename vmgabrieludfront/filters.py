"""Filter App Vmgabrieludfront"""

# Libraries
import django_filters

# Models
from . import models


class PeriphepaltypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label="Name", lookup_expr="icontains")
    description = django_filters.CharFilter(label="Description", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("name", "Name"),
            ("description", "Description"),
        ),
    )

    class Meta:
        model = models.periphepaltype.Periphepaltype
        fields = ["name", "description", ]


class PeriphepalFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label="Name", lookup_expr="icontains")
    description = django_filters.CharFilter(label="Description", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("name", "Name"),
            ("description", "Description"),
            ("type_periphepal", "Type_periphepal"),
        ),
    )

    class Meta:
        model = models.periphepal.Periphepal
        fields = ["name", "description", "type_periphepal", ]


class CameraFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label="Name", lookup_expr="icontains")
    sort = django_filters.OrderingFilter(
        fields=(
            ("name", "Name"),
        ),
    )

    class Meta:
        model = models.camera.Camera
        fields = ["name", ]


class CameraperiphepalFilter(django_filters.FilterSet):
    sort = django_filters.OrderingFilter(
        fields=(
            ("camera", "Camera"),
            ("periphepal", "Periphepal"),
        ),
    )

    class Meta:
        model = models.cameraperiphepal.Cameraperiphepal
        fields = ["camera", "periphepal", ]


