from django.db import models
from users.models import User


class Medicine(models.Model):
    DISEASE_CHOICES = [
        ("BP", "Blood Pressure"),
        ("DIABETES", "Diabetes"),
        ("THYROID", "Thyroid"),
        ("HEART", "Heart"),
        ("VITAMINS", "Vitamins"),
        ("ANTIBIOTICS", "Antibiotics"),
        ("OTHER", "Other"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="medicines"
    )

    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    frequency = models.CharField(max_length=100)

    disease = models.CharField(
        max_length=20,
        choices=DISEASE_CHOICES,
        default="OTHER"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.medicine_name


class MedicationSchedule(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("TAKEN", "Taken"),
        ("MISSED", "Missed"),
    ]

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    reminder_time = models.TimeField()
    quantity_per_dose = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine.medicine_name} - {self.reminder_time}"
class Prescription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="prescriptions"
    )

    prescription_image = models.ImageField(
        upload_to="prescriptions/"
    )

    doctor_name = models.CharField(max_length=100)

    notes = models.TextField(
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} Prescription"