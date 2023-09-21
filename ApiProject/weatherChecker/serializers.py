from rest_framework import serializers
from weatherChecker.models import Contact

class ContactSerializer(serializers.HyperlinkedModelSerializer ):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ['name', 'title', 'email', 'owner']