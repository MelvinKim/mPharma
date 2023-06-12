from django.urls import path

from .views import DiagnosisListCreateView, DiagnosisRetrieveUpdateDeleteView, UploadCSVView

urlpatterns = [
    path("diagnosis/", DiagnosisListCreateView.as_view(), name="diagnosis-list-create"),
    path("diagnosis/<int:pk>/", DiagnosisRetrieveUpdateDeleteView.as_view(), name="diagnosis-retrieve-update-delete"),
    path("upload-csv/", UploadCSVView.as_view(), name="upload_csv"),
]
