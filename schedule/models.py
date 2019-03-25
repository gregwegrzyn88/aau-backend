from django.db import models


# Create your models here.
from django.db import models
from datetime import datetime 


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
    address_line_1 = models.CharField(max_length=1024)
    address_line_2 = models.CharField(max_length=1024)
    company_zip_code = models.CharField(max_length=1024)
    city = models.CharField(max_length=12)
    country = models.CharField(max_length=12)


    def __str__(self):
      return self.company_name

class Team(models.Model):
  company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='teams')
  team_name = models.CharField(max_length=1000)

  def __str__(self):
      return self.team_name

class Coach(models.Model):
  team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='coaches')
  coach_name = models.CharField(max_length=200)
  email = models.EmailField(max_length=70,blank=True)

  def __str__(self):
      return self.coach_name

class Player(models.Model):
  team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
  player_name = models.CharField(max_length=200)
  date_of_birth = models.DateField(null=True)

  def __str__(self):
      return self.player_name

class ScheduledPractice(models.Model):
  team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='practice_schedules')
  practice_facility_name = models.CharField(max_length=1024)
  practice_address_line_1 = models.CharField(max_length=1024)
  practice_address_line_2 = models.CharField(max_length=1024)
  practice_zip_code = models.CharField(max_length=1024)
  practice_city = models.CharField(max_length=12)
  practice_country = models.CharField(max_length=12)
  practice_day = models.CharField(max_length=1024)
  practice_time = models.CharField(max_length=1024)

  def __str__(self):
      return self.practice_facility_name

class TournamentSchedule(models.Model):
  team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tournament_schedules')
  tournament_facility_name = models.CharField(max_length=1024)
  tournament_address_line_1 = models.CharField(max_length=1024)
  tournament_address_line_2 = models.CharField(max_length=1024)
  tournament_zip_code = models.CharField(max_length=1024)
  tournament_city = models.CharField(max_length=12)
  tournament_country = models.CharField(max_length=12)
  tournament_day = models.CharField(max_length=1024)
  tournament_time = models.CharField(max_length=1024)


  def __str__(self):
      return self.tournament_facility_name


class TournamentGame(models.Model):
  team_id = models.ForeignKey(TournamentSchedule, on_delete=models.CASCADE, related_name='tournament_games')
  court = models.CharField(max_length=1024)
  time = models.CharField(max_length=1024)

  def __str__(self):
      return self.court

class ParentInformation(models.Model):
  player_id = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='tournament_schedules')
  parent_email = models.EmailField(max_length=70,blank=True)
  parent_address_line_1 = models.CharField(max_length=1024)
  parent_address_line_2 = models.CharField(max_length=1024)
  parent_company_zip_code = models.CharField(max_length=1024)
  parent_city = models.CharField(max_length=12)
  parent_country = models.CharField(max_length=12)

  def __str__(self):
      return self.post_title

