"""All Urls of Vmgabrieludfront"""

# Libraries
from django.urls import path

# Views
from . import views


app_name = "vmgabrieludfronts"
urlpatterns = [
    # PeriphepalType
    path(
        "periphepaltypes/",
        views.ListPeriphepaltypeView.as_view(),
        name="periphepaltypes",
    ),
    path(
        "periphepaltypes/new/",
        views.PeriphepaltypeCreateView.as_view(),
        name="periphepaltype-new",
    ),
    path(
        "periphepaltypes/<int:pk>/edit/",
        views.PeriphepaltypeUpdateView.as_view(),
        name="periphepaltype-edit",
    ),
    path(
        "periphepaltypes/<int:pk>/delete/",
        views.delete_periphepaltype_view,
        name="periphepaltype-delete",
    ),

    # Periphepal
    path(
        "periphepals/",
        views.ListPeriphepalView.as_view(),
        name="periphepals",
    ),
    path(
        "periphepals/new/",
        views.PeriphepalCreateView.as_view(),
        name="periphepal-new",
    ),
    path(
        "periphepals/<int:pk>/edit/",
        views.PeriphepalUpdateView.as_view(),
        name="periphepal-edit",
    ),
    path(
        "periphepals/<int:pk>/delete/",
        views.delete_periphepal_view,
        name="periphepal-delete",
    ),

    # Camera
    path(
        "cameras/",
        views.ListCameraView.as_view(),
        name="cameras",
    ),
    path(
        "cameras/new/",
        views.CameraCreateView.as_view(),
        name="camera-new",
    ),
    path(
        "cameras/<int:pk>/edit/",
        views.CameraUpdateView.as_view(),
        name="camera-edit",
    ),
    path(
        "cameras/<int:pk>/delete/",
        views.delete_camera_view,
        name="camera-delete",
    ),

    # CameraPeriphepal
    path(
        "cameraperiphepals/",
        views.ListCameraperiphepalView.as_view(),
        name="cameraperiphepals",
    ),
    path(
        "cameraperiphepals/new/",
        views.CameraperiphepalCreateView.as_view(),
        name="cameraperiphepal-new",
    ),
    path(
        "cameraperiphepals/<int:pk>/edit/",
        views.CameraperiphepalUpdateView.as_view(),
        name="cameraperiphepal-edit",
    ),
    path(
        "cameraperiphepals/<int:pk>/delete/",
        views.delete_cameraperiphepal_view,
        name="cameraperiphepal-delete",
    ),

]