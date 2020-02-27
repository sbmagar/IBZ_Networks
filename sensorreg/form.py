from django import forms
from sensorreg.models import DeviceStatus,Operator, InterlockDevice


class DeviceStatusForm(forms.ModelForm):
    class Meta:
        model = DeviceStatus
        fields = ['DeviceID', 'IP', 'Port', "MacAddress", "AdministrativeRegion", "InstallationRoute", "InstallationLocation",
                  "GPSCoordinates", "InterlockDeviceInformation"]


class InterlockDeviceForm(forms.ModelForm):
    class Meta:
        model = InterlockDevice
        fields = ['Device_ID', 'IP', 'Port', 'Device_Type', 'Remarks']
class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ('PhoneNo', 'Password', 'MacAddress', 'ManagerName', 'ManagerPhoneNo', 'Department', 'FinalApprover')