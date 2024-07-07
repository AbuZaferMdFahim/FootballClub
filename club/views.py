from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Fixture,Player, News
from shop.models import Jersey,FootballAccessory,Turf
from django.db.models import Q

# Create your views here.

def home(request):
    fixtures = Fixture.objects.all()[:3]
    players = Player.objects.all()[:3]
    news = News.objects.all().order_by('-created_at')[:3]
    jersey = Jersey.objects.all()
    footballAccessory = FootballAccessory.objects.all()
    turf = Turf.objects.all()
    data = {
        "fixtures": fixtures,
        "players": players,
        "news": news,
        "jersey": jersey,
        "footballAccessory": footballAccessory,
        "turf": turf,
    }
    return render(request, "index.html", data)

def news(request):
    news = News.objects.all().order_by('-created_at')
    data={
        "news":news
    }
    return render(request, "news.html", data)

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news_item': news_item})

def fixture(request):
    today = timezone.now().date()
    upcoming_fixtures = Fixture.objects.filter(date__gte=today).order_by('date')
    data = {
        'fixtures': upcoming_fixtures,
        'title': 'Upcoming Fixtures - Praetorians United Football Club'
    }
    return render(request, 'fixture.html', data)

def player(request):
    players = Player.objects.all().order_by('position')
    positions = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
    players_by_position = {position: [] for position in positions}

    if request.method=="GET":
        st = request.GET.get('search')
        if st!=None:
            players = Player.objects.filter(name__icontains = st)
            
    for player in players:
        if player.position in players_by_position:
            players_by_position[player.position].append(player)

    context = {
        'players_by_position': players_by_position,
    }
    return render(request, 'player.html', context)


def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    data = {
        "player":player
    }
    return render(request, 'player_detail.html', data)





