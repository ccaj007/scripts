from imdb import Cinemagoer
ia = Cinemagoer()
#print(sorted(the_matrix.keys()))
#print(ia.get_movie_infoset())
#movie = ia.get_movie_parents_guide("1640718")

inp = input("enter movie to search: ")
movie = ia.search_movie(inp)
a = [match for match in movie]
print(a)
movie_id = a[0].movieID
the_movie = ia.get_movie(a[0].movieID)
pg = ia.get_movie_parents_guide(movie_id)
print(pg['data']['advisory votes']['nudity']['status'])
print(pg['data']['advisory nudity'])
