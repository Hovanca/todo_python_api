#potiahneme moduly

from rest_framework import serializers
from .models import Todo

#vytvoriime ze co ma vypisovat v jsone
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','status') #tu uz chceme vsetky vypisat
