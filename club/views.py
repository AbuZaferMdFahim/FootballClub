from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from .models import Fixture,Player, News
from shop.models import Jersey,FootballAccessory,Turf
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

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
    news_list = News.objects.all().order_by('-created_at')
    
    # Pagination
    paginator = Paginator(news_list, 9)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'news.html', data)

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news_item': news_item})

# UI
def fixture(request):
    today = timezone.now().date()
    upcoming_fixtures = Fixture.objects.filter(date__gte=today).order_by('date')
    
    # Pagination
    paginator = Paginator(upcoming_fixtures, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    data = {
        'page_obj': page_obj,
        'title': 'Upcoming Fixtures - Praetorians United Football Club'
    }
    return render(request, 'fixture.html', data)

def player(request):
    positions = dict(Player.POSITION_CHOICES).values()  # Get the display names
    players_by_position = {position: [] for position in positions}

    if request.method == "GET":
        st = request.GET.get('search')
        if st:
            players = Player.objects.filter(name__icontains=st).order_by('position')
        else:
            players = Player.objects.all().order_by('position')

    # Create a mapping from internal values to display names
    position_map = {internal: display for internal, display in Player.POSITION_CHOICES}

    for player in players:
        position_display = position_map.get(player.position)
        if position_display in players_by_position:
            players_by_position[position_display].append(player)

    # Remove empty positions
    players_by_position = {position: players for position, players in players_by_position.items() if players}

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f"From: {email}\n\n{message}"
            
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['abuzafermdfahim@gmail.com']  # Replace with your static email address
            )
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})





