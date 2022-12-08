 
#####FRONT END ___ BACKEND

import pygame
from random import randint 
import math
from sklearn.cluster import KMeans





### DISTANCE FUNCTION
def distance(p1,p2):
	return math.sqrt( (p1[0]-p2[0]) * (p1[0]-p2[0])   +   (p1[1]-p2[1])*(p1[1]-p2[1])  );




pygame.init()

screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Demo K-means for cluster")


clock = pygame.time.Clock()

SCREEN_COLOR = (150,150,150)
BLACK = (0,0,0)
BACKGROUND_PANEL =(249,255,230)
WHITE = (255,255,255)
running = True

font = pygame.font.SysFont("sans" ,40)
font_small = pygame.font.SysFont("sans" ,20)
text_plus = font.render("+", True, WHITE)
text_minus = font.render("-", True, WHITE)
text_run = font.render("Run", True, WHITE)
text_random = font.render("Random", True, WHITE)
text_algorithm = font.render("Algorithm", True, WHITE)
text_reset = font.render("Reset", True, WHITE)

#Color for cluster
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147,153,35)
PURPLE = (255,0,255)
ORANGE = (255,125,25)
 
COLORS = [RED,GREEN,BLUE,YELLOW,PURPLE,ORANGE]

#Variable
K=0

points = []
clusters =[]
labels = []

while running:
	clock.tick(60)
	screen.fill(SCREEN_COLOR)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# print(str(mouse_x) + "," + str(mouse_y))


#####Draw interface
	
	#Draw panel
	pygame.draw.rect(screen, BLACK , (50,50,700,500))
	pygame.draw.rect(screen, BACKGROUND_PANEL ,(55,55,690,490))
	
	#K value
	text_k = font.render("K = " + str(K) ,True, BLACK  )
	screen.blit(text_k, (1050,50))

	# #Error Text
	# text_error = font.render("Error = " + str(Error) ,True, BLACK  )
	# screen.blit(text_error, (850,350))

	# K button +
	pygame.draw.rect(screen , BLACK , (850,50,50,50))
	screen.blit(text_plus , (862,52))

	# K button -
	pygame.draw.rect(screen , BLACK , (950,50,50,50))
	screen.blit(text_minus , (962,52))

	# Run button
	pygame.draw.rect(screen , BLACK , (850,150,150,50))
	screen.blit(text_run, (890,154))

	# Random button
	pygame.draw.rect(screen , BLACK , (850,250,150,50))
	screen.blit(text_random, (850,254))

	# Algorithm button scikit-learn library
	pygame.draw.rect(screen , BLACK , (850,450,200,50))
	screen.blit(text_algorithm, (860,457))
	# Reset button
	pygame.draw.rect(screen , BLACK , (850,550,150,50))
	screen.blit(text_reset, (870,554))

	#Draw mouse position 
	 
	text_mouse = font_small.render("(" + str(mouse_x-55) + "," +str(mouse_y-55) +")", True ,BLACK)
	screen.blit(text_mouse, (mouse_x +10 ,mouse_y))


	######## END DRAW INTERFACE


	# pygame.draw.rect(screen, WHITE, (100,100,100,100))
	# pygame.draw.rect(screen, WHITE, (400,100,100,100))
	# pygame.draw.rect(screen, WHITE, (650,100,250,100)) 
	# pygame.draw.rect(screen, WHITE, (100,300,100,100))
	# pygame.draw.rect(screen, WHITE, (400,300,100,100))
	# pygame.draw.rect(screen, WHITE, (650,300,250,100))
	# pygame.draw.rect(screen, WHITE, (100,50,50,50))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN: 
			# Create point on panel
			if 50  < mouse_x < 750 and 50 < mouse_y <550:
				labels = []
				point =[mouse_x -50, mouse_y-50]
				points.append(point)
				print(points)
				print("Click in panel")




			# Change k buttion +
			if 850 < mouse_x < 900 and 50 < mouse_y < 100:
				print("Press K +")
				K +=1
			# Change k buttion -
			if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
				if K > 0:
					K -=1
					print("Press K -")
			# Run button
			if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
				print("Run press")
				labels = []
				if clusters == []:
					continue
				# Assign point to closet clusters
				for p in points:
					distances_to_cluster = []
					for c in clusters:
						dis_caculator = distance(p,c)
						distances_to_cluster.append(dis_caculator)
					min_distance = min(distances_to_cluster)
					label = distances_to_cluster.index(min_distance)
					labels.append(label)

				#Update clusters
				for i in range(K):
					sum_x = 0
					sum_y = 0
					count = 0
					for j in range(len(points)):
						if labels[j] == i:
							sum_x = sum_x + points[j][0]
							sum_y = sum_y + points[j][1]
							count = count +1;
					if count!=0:
						new_cluster_x = sum_x/count
						new_cluster_y = sum_y/count
						clusters[i] = [new_cluster_x,new_cluster_y]


			# Random button
			if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
				labels=[]
				clusters = []
				for i in range(K):
					random_point = [randint(0,700), randint(0,500)]
					clusters.append(random_point)
					print(clusters)
					print("Random")
			# Reset button
			if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
				print("Reset ")
				K=0
				points = []
				clusters =[]
				labels = []
				Error = 0


			### Algorithm button	
			if 850 < mouse_x < 1050 and 450 < mouse_y < 500:
				try:
					kmeans = KMeans(n_clusters=K).fit(points) 
					labels=kmeans.predict(points)
					clusters = kmeans.cluster_centers_


				except:
					print("error")


				



				print("Use library")
	

	#Draw point
	for i in range(len(points)):
		pygame.draw.circle(screen, BLACK, ( points[i][0]+50, points[i][1] + 50 ) , 6)
		if labels == []:
			pygame.draw.circle(screen, WHITE, ( points[i][0]+50, points[i][1] + 50 ) , 5)
		else:
			pygame.draw.circle(screen, COLORS[labels[i]], ( points[i][0]+50, points[i][1] + 50 ) , 5)
	




	#Draw Clusters
	for i in range(len(clusters)):
		pygame.draw.circle(screen, COLORS[i] , ( int(clusters[i][0] +50) , int(clusters[i][1] + 50)) ,10)


	#Error 
	Error=0


	if clusters != [] and labels != []:
		for i in range(len(points)):
			Error = Error + distance(points[i], clusters[labels[i]])
	text_error = font.render("Error = "+ str(int(Error)), True, BLACK)
	screen.blit(text_error, (850,350))


	






	pygame.display.flip()

	

pygame.quit()




##### BACKEND  