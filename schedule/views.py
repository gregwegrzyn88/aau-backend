from .models import Company, Team, Coach, Player, ScheduledPractice, TournamentSchedule, TournamentGame, ParentInformation
from .serializers import CompanySerializer, TeamSerializer, CoachSerializer, PlayerSerializer, ScheduledPracticeSerializer, TournamentScheduleSerializer, TournamentGameSerializer, ParentInformationSerializer  

from rest_framework import viewsets


class CompanyViewSet(viewsets.ModelViewSet):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer

class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

class CoachViewSet(viewsets.ModelViewSet):
  queryset = Coach.objects.all()
  serializer_class = CoachSerializer

class PlayerViewSet(viewsets.ModelViewSet):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer

class ScheduledPracticeViewSet(viewsets.ModelViewSet):
  queryset = ScheduledPractice.objects.all()
  serializer_class = ScheduledPracticeSerializer


class TournamentScheduleViewSet(viewsets.ModelViewSet):
  queryset = TournamentSchedule.objects.all()
  serializer_class = TournamentScheduleSerializer

class TournamentGameViewSet(viewsets.ModelViewSet):
  queryset = TournamentGame.objects.all()
  serializer_class = TournamentGameSerializer


class ParentInformationViewSet(viewsets.ModelViewSet):
  queryset = ParentInformation.objects.all()
  serializer_class = ParentInformationSerializer

