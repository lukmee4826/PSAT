from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'category', 'quantity', 'expiration_date', 'supplier']

    # Custom validation for quantity (e.g., it should be a positive number)
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than 0.")
        return quantity

    # Custom validation for expiration_date (e.g., expiration date should not be in the past)
    def clean_expiration_date(self):
        expiration_date = self.cleaned_data.get('expiration_date')
        if expiration_date and expiration_date < forms.DateField.today():
            raise forms.ValidationError("Expiration date cannot be in the past.")
        return expiration_date

    # Optional: Custom widgets for fields (e.g., a DatePicker widget for expiration_date)
    expiration_date = forms.DateField(
        widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"))
    )