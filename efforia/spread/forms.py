from django.forms import Form,CharField,Textarea

class FriendSearch(Form):
    name = CharField(label="")

class SpreadForm(Form):
    content = CharField(label="")
