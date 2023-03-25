import sys
from imdb import Cinemagoer
ia = Cinemagoer()
#print(sorted(the_matrix.keys()))
#print(ia.get_movie_infoset())
#movie = ia.get_movie_parents_guide("1640718")

inp = input("enter movie to search: ")
movies = ia.search_movie(inp)
for i in range(len(movies)):
    print(i, movies[i])
inp2 = int(input("enter selection: "))
print(movies[inp2])
movie_id = movies[inp2].movieID
#the_movie = ia.get_movie(movie_id)
movie = ia.get_movie(movie_id)
print(f"rating: {movie.get('rating')}\nyear: {movie.get('year')}")
pg = ia.get_movie_parents_guide(movie_id)
print(pg['data']['advisory votes']['nudity']['status'])
print(pg['data']['advisory nudity'])

sys.exit()

