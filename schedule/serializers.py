from rest_framework import serializers
from .models import Company, Team, Coach, Player, ScheduledPractice, TournamentSchedule, TournamentGame, ParentInformation

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields =  '__all__'

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields =  '__all__'

class CoachSerializer(serializers.ModelSerializer):
  class Meta:
    model = Coach
    fields =  '__all__'
    
class PlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Player
    fields =  '__all__'

class ScheduledPracticeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ScheduledPractice
    fields =  '__all__'

class TournamentScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = TournamentSchedule
    fields =  '__all__'

class TournamentGameSerializer(serializers.ModelSerializer):
  class Meta:
    model = TournamentGame
    fields =  '__all__'
    
class ParentInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = ParentInformation
    fields =  '__all__'