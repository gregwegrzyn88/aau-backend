from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, TeamViewSet, CoachViewSet, PlayerViewSet, ScheduledPracticeViewSet, TournamentScheduleViewSet, TournamentGameViewSet, ParentInformationViewSet


router = DefaultRouter()


router.register(r'company', CompanyViewSet)
router.register(r'team', TeamViewSet)
router.register(r'coach', CoachViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'scheduledPractice', ScheduledPracticeViewSet)
router.register(r'tournamentSchedule', TournamentScheduleViewSet)
router.register(r'tournamentGame', TournamentGameViewSet)
router.register(r'parentInformation', ParentInformationViewSet)
urlpatterns = router.urls


