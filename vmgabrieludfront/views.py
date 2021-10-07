"""Views of Vmgabrieludfront"""

# Libraries
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Core
from core.views import FilteredListView

# App Contents
from . import models, filters, forms


# Periphepaltype

class ListPeriphepaltypeView(LoginRequiredMixin, FilteredListView):
    template_name = "periphepaltype/list.html"
    filterset_class = filters.PeriphepaltypeFilter
    model = models.periphepaltype.Periphepaltype
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class PeriphepaltypeCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View Periphepaltype"""
    form_class = forms.PeriphepaltypeForm
    success_url = reverse_lazy("vmgabrieludfronts:periphepaltypes")
    template_name = "periphepaltype/new.html"


class PeriphepaltypeUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View Periphepaltype"""
    form_class = forms.PeriphepaltypeForm
    success_url = reverse_lazy("vmgabrieludfronts:periphepaltypes")
    template_name = "periphepaltype/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.periphepaltype.Periphepaltype, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_periphepaltype_view(request, pk):
    periphepaltype = get_object_or_404(models.periphepaltype.Periphepaltype, pk=pk)
    periphepaltype.delete()
    return redirect("vmgabrieludfronts:periphepaltypes")


# Periphepal

class ListPeriphepalView(LoginRequiredMixin, FilteredListView):
    template_name = "periphepal/list.html"
    filterset_class = filters.PeriphepalFilter
    model = models.periphepal.Periphepal
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class PeriphepalCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View Periphepal"""
    form_class = forms.PeriphepalForm
    success_url = reverse_lazy("vmgabrieludfronts:periphepals")
    template_name = "periphepal/new.html"


class PeriphepalUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View Periphepal"""
    form_class = forms.PeriphepalForm
    success_url = reverse_lazy("vmgabrieludfronts:periphepals")
    template_name = "periphepal/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.periphepal.Periphepal, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_periphepal_view(request, pk):
    periphepal = get_object_or_404(models.periphepal.Periphepal, pk=pk)
    periphepal.delete()
    return redirect("vmgabrieludfronts:periphepals")


# Camera

class ListCameraView(LoginRequiredMixin, FilteredListView):
    template_name = "camera/list.html"
    filterset_class = filters.CameraFilter
    model = models.camera.Camera
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class CameraCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View Camera"""
    form_class = forms.CameraForm
    success_url = reverse_lazy("vmgabrieludfronts:cameras")
    template_name = "camera/new.html"


class CameraUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View Camera"""
    form_class = forms.CameraForm
    success_url = reverse_lazy("vmgabrieludfronts:cameras")
    template_name = "camera/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.camera.Camera, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_camera_view(request, pk):
    camera = get_object_or_404(models.camera.Camera, pk=pk)
    camera.delete()
    return redirect("vmgabrieludfronts:cameras")


# Cameraperiphepal

class ListCameraperiphepalView(LoginRequiredMixin, FilteredListView):
    template_name = "cameraperiphepal/list.html"
    filterset_class = filters.CameraperiphepalFilter
    model = models.cameraperiphepal.Cameraperiphepal
    paginate_by = settings.DEFAULT_COUNT_PAGINATE


class CameraperiphepalCreateView(LoginRequiredMixin, generic.CreateView):
    """Create View Cameraperiphepal"""
    form_class = forms.CameraperiphepalForm
    success_url = reverse_lazy("vmgabrieludfronts:cameraperiphepals")
    template_name = "cameraperiphepal/new.html"


class CameraperiphepalUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Update View Cameraperiphepal"""
    form_class = forms.CameraperiphepalForm
    success_url = reverse_lazy("vmgabrieludfronts:cameraperiphepals")
    template_name = "cameraperiphepal/new.html"

    def get_object(self, **kwargs):
        """Return data"""
        return get_object_or_404(models.cameraperiphepal.Cameraperiphepal, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Modify Context"""
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@login_required
def delete_cameraperiphepal_view(request, pk):
    cameraperiphepal = get_object_or_404(models.cameraperiphepal.Cameraperiphepal, pk=pk)
    cameraperiphepal.delete()
    return redirect("vmgabrieludfronts:cameraperiphepals")


