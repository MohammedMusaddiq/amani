from django import forms


class AdminLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class TeacherCreateForm(forms.Form):
    name = forms.CharField(label='', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control mb-2', 'placeholder': 'Name'}))
    password = forms.CharField(label='', max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2', 'placeholder': 'Password'}))
    branch = forms.CharField(label='', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control mb-2', 'placeholder': 'Branch'}))


class SubjectForm(forms.Form):
    subject_name = forms.CharField(label='', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control mb-2', 'placeholder': 'Subject Name'}))
    semester = forms.CharField(label='', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control mb-2', 'placeholder': 'Semester'}))


class StudentCreateForm(forms.Form):
    name = forms.CharField(label='', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Name'}))
    password = forms.CharField(label='', max_length=60, widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Password'}))
    branch = forms.CharField(label='', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Branch'}))
    semester = forms.CharField(label='', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Semester'}))
    usn = forms.CharField(label='', max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'USN'}))
