from django.contrib import admin
from schedule.models import Company, Team, Coach, Player, ScheduledPractice, TournamentSchedule, TournamentGame, ParentInformation 

admin.site.register(Company)
admin.site.register(Team)
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(ScheduledPractice)
admin.site.register(TournamentSchedule)
admin.site.register(TournamentGame)
admin.site.register(ParentInformation)