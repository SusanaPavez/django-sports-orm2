from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),

		# Aquí van los filtros. Se hace un nombre de variable en el diccionario
		# Luego se especifica el nombre del modelo, objects, y lo que quiero
		# que se ejecute (en este caso, filtros de distinto tipo).
		# Luego name__contains indica lo que quiero filtrar

		# 1. Find all baseball leagues | 
		# International Collegiate Baseball Conference,
		# Atlantic Federation of Amateur Baseball Players

		'baseball_league' : League.objects.filter(name__contains='baseball'),



		# 2. Find all womens' leagues |
		# International Association of Womens' Basketball Players,
		# Transamerican Womens' Football Athletics Conference

		'women_league' : League.objects.filter(name__contains='women'),



		#3. Find all leagues where sport is any type of hockey |
		# International Conference of Amateur Ice Hockey,
		# Atlantic Amateur Field Hockey League, Pacific Ice Hockey Conference
		
		'hockey_league' : League.objects.filter(name__contains='hockey'),
		


		# 4. Find all leagues where sport is something OTHER THAN football |
		# International Conference of Amateur Ice Hockey,
		# International Collegiate Baseball Conference,
		# Atlantic Federation of Amateur Baseball Players,
		# Atlantic Federation of Basketball Athletics,
		# Atlantic Soccer Conference,
		# International Association of Womens' Basketball Players,
		# Atlantic Amateur Field Hockey League, Pacific Ice Hockey Conference
		
		'no_football_league' : League.objects.exclude(name__contains='football'),
		
		
		
		# 5. Find all leagues that call themselves "conferences" |
		# International Conference of Amateur Ice Hockey,
		# International Collegiate Baseball Conference,
		# Atlantic Soccer Conference,
		# American Conference of Amateur Football,
		# Transamerican Womens' Football Athletics Conference,
		# Pacific Ice Hockey Conference

		'conferences_league' : League.objects.filter(name__contains='conference'),
		
		
		
		# 6. Find all leagues in the Atlantic region |
		# Atlantic Federation of Amateur Baseball Players,
		# Atlantic Federation of Basketball Athletics,
		# Atlantic Soccer Conference,
		# Atlantic Amateur Field Hockey League

		'atlantic_league' : League.objects.filter(name__contains='atlantic'),



		# 7. Find all teams based in Dallas |
		# Dallas Nets,
		# Dallas Angels

		'dallas_teams' : Team.objects.filter(location__contains='dallas'),



		# 8. Find all teams named the Raptors |
		# Atlanta Raptors,
		# Golden State Raptors

		'raptor_teams' : Team.objects.filter(team_name__contains='raptors'),



		# 9. Find all teams whose location includes "City" |
		# Mexico City Cave Spiders,
		# Kansas City Spurs

		'city_teams' : Team.objects.filter(location__contains='city'),



		# 10. Find all teams whose names begin with "T" | 
		# Alberta Texans, Michigan Timberwolves,
		# Manitoba Tiger-Cats, Colorado Twins
		
		'tea_teams' : Team.objects.filter(team_name__startswith='t'),
		

		# 11. Return all teams, ordered alphabetically by location | 
		# *too many to list*

		'teams_lists' : Team.objects.order_by('location'),
		


		# 12. Return all teams, ordered by team name in reverse alphabetical order |
		# *too many to list*

		# Esto ordena por nombre de equipo al revés

		'reversed_teams' : Team.objects.all().order_by('-team_name'),



		# 13. Find every player with last name "Cooper" |
		# Joshua Cooper, Landon Cooper, Michael Cooper, Alexander Cooper
		
		'the_cooper' : Player.objects.filter(last_name__contains='Cooper'),



		# 14. Find every player with first name "Joshua" |
		# Joshua Cooper, Joshua Hayes, Joshua Henderson, Joshua Long,
		# Joshua Coleman, Joshua White, Joshua Parker, Joshua Smith

		'the_joshua' : Player.objects.filter(first_name__contains='joshua'),



		# 15. Find every player with last name "Cooper" EXCEPT FOR Joshua |
		# Landon Cooper, Michael Cooper, Alexander Cooper

		'yes_cooper_no_joshua' : Player.objects.filter(last_name__contains = 'cooper').exclude (first_name__contains ='joshua'),



		# 16. Find all players with first name "Alexander" OR first name "Wyatt" |
		# Wyatt Bell, Alexander Bailey, Wyatt Peterson, Alexander Wright,
		# Wyatt Alexander, Wyatt Bennett, Alexander Parker, Alexander Adams,
		# Alexander Walker, Alexander Flores, Alexander Cooper

		'alex_wyatt' : Player.objects.filter(first_name__contains=['Alexander', 'Wyatt']),
		
		# 1. Find all teams in the Atlantic Soccer Conference |
		# Minneapolis Wizards, Pittsburgh Bruins, Cleveland Dolphins, Toronto Pirates,
		# Golden State Raptors

		'atlantic_soccer' : Team.objects.filter(league__name='Atlantic Soccer Conference'),

		# 2. Find all (current) players on the Boston Penguins |
		# Landon Hernandez, Wyatt Bennett, David Sanchez

		'boston_penguins' : Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston"),



		# 3. Find all (current) players in the International Collegiate Baseball Conference |
		# Michael Flores, Abigail Foster, Ryan Phillips, Elijah Powell, Isaac Perry, Charlotte Jones,
		# Sophia Rivera, Isabella Griffin, Landon Cooper, Elijah James, Abigail Davis, Wyatt Alexander,
		# Abigail Richardson, Jacob Jenkins, Landon Gray, Levi Miller, Joshua Long, Nathan Mitchell,
		# James Ramirez, Samuel Evans, John Edwards, Henry Martin, Andrew Adams, Joshua White,
		# Alexander Flores, Abigail Hernandez, Caleb Parker, Joshua Smith, Jack Phillips

		'current_baseball' : Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		
		# 4. Find all (current) players in the American Conference of Amateur Football with
		# last name "Lopez" | Levi Lopez, Isabella Lopez

		'lopez_football' : Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name="Lopez"),
		
		# 5. Find all football players | Nathan Bryant, Wyatt Bell, Lucas Martin, Luke Lopez,
		# Dylan Rodriguez, Luke Bell, James Ross, Benjamin King, Caleb Martinez, Jack Young,
		# Anthony Martinez, Jaxon Gonzales, Emily Sanchez, Jaxon Torres, Liam Watson, James Smith,
		# Dylan Garcia, Joshua Cooper, Aiden Rivera, Benjamin Alexander, Ava Henderson, Joshua Hayes,
		# Landon Mitchell, Charles Collins, Nathan Brooks, Isabella Bennett, Lucas Perry,
		# Charles Campbell, Alexander Parker, Benjamin Perry, Levi Lopez, Charlotte Ross, Oliver Kelly,
		# Daniel Martinez, Ryan Peterson, Isabella Lopez, Charlotte Harris, Caleb Collins, Ryan Gonzales,
		# Joseph Roberts, David Watson, Abigail Long, Landon James, Daniel Davis, Charlotte Brown,
		# Logan King, Luke Clark, Isabella Lewis, Jacob Gray, Liam Robinson, Aiden Hernandez,
		# Christian Wood, Joshua Parker, Ethan Sanchez, Noah Brooks, Charles Campbell, Mason Henderson,
		# Nathan Flores, Jackson Perry, Noah Taylor, Levi Howard, Jayden Perez, Elijah Richardson,
		# Emily Jackson, Olivia Young, Abigail Torres, Christopher Sanders
		
		'football_players' : Player.objects.filter(curr_team__league__sport="Football"),


		# 6. Find all teams with a (current) player named "Sophia" |
		# Mexico City Cave Spiders, Houston Hornets, Wisconsin Devils

		'sophia' : Team.objects.filter(curr_players__first_name="Sophia"),
		

		# 7. Find all leagues with a (current) player named "Sophia" |
		# International Collegiate Baseball Conference, Atlantic Federation of Basketball Athletics,
		# Atlantic Amateur Field Hockey League

		'sophia2' : League.objects.filter(teams__curr_players__first_name="Sophia"),
		

		# 8. Find everyone with the last name "Flores" who DOESN'T (currently) play for the
		# Washington Roughriders | Michael Flores, Alexander Flores, Nathan Flores

		'roughriders' : Player.objects.exclude(curr_team__team_name="Roughriders", curr_team__location="Washington").filter(last_name="Flores"),



		# 1. Find all teams, past and present, that Samuel Evans has played with |
		# Dallas Nets, Montreal White Sox, Ohio Black Sox, Indianapolis Athletics, Mexico City Cave Spiders, Ontario Outlaws
		
		'evans' : Team.objects.filter(all_players__first_name="Samuel") & Team.objects.filter(all_players__last_name="Evans"),



		# 2. Find all players, past and present, with the Manitoba Tiger-Cats | Jaxon Howard, Sophia Bailey, Alexander Bailey, Levi Rodriguez, William Martin, Olivia Diaz, Jacob Green, Christian Perez, Harper James, Daniel Kelly
		
		'manitoba' : Player.objects.filter(all_teams__team_name="Tiger-Cats") & Player.objects.filter(all_teams__location="Manitoba"),


		# 3. Find all players who were formerly (but aren't currently) with the Wichita Vikings | Dylan Rodriguez, Aiden Rivera, Ava Henderson, Nathan Brooks, Daniel Martinez, Ryan Peterson, Charlotte Harris, Noah Brooks, Levi Howard, Christopher Sanders
		
		'wichita' : Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings").filter(all_teams__location="Wichita").exclude(curr_team__location="Wichita"),


		# 4. Find every team that Jacob Gray played for before he joined the Oregon Colts | Puerto Rico Breakers, Toronto Kings, Ontario Gunslingers
		
		'jacob' : Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(curr_players__first_name="Jacob", curr_players__last_name="Gray"),

		
		# 5. Find everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players | Joshua Long, Joshua White, Joshua Smith
		
		'joshua' : Player.objects.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players").filter(first_name="Joshua"),
		

		# 6. Find all teams that have had 12 or more players, past and present.  (HINT: Look up the Django `annotate` function.) | Dallas Nets, California Padres, Montreal White Sox, Alberta Texans, Puerto Rico Breakers, South Carolina Wolverines, Washington Roughriders, Edmonton Warriors, Toronto Kings, Wisconsin Rams, Michigan Timberwolves, Phoenix Rays, Ontario Gunslingers, Texas Diamondbacks, Oregon Colts, Mexico City Cave Spiders, Raleigh Bulls, Montreal Wild, Wisconsin Devils, Indiana Royals, Maryland Cowboys, Ontario Outlaws, Dallas Angels, Kansas City Spurs
		
		'twelve' : Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),


		# 7. Show all players, sorted by the number of teams they've played for | *too many to list, but the first few are Olivia Rodriguez, Ryan Phillips, and Luke Bell*

		'all_players' : Player.objects.annotate(num_teams=count('all_teams')).order_by('num_teams'),

		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
