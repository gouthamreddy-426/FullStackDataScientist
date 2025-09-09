class Cinema:
    def __init__(self,movies):
        self.movies = movies
    def book(self,movie,seats):
        if (movie not in self.movies):
            return "Movie Not Available"
        elif self.movies[movie] == 0:
            return "No seats Available for "+movie
        else:
            self.movies[movie] -= seats
            return "Booked "+str(seats)+" tickets for "+movie
    def cancel(self,movie,seats):
        self.movies[movie] += seats
        return "Cancelled "+str(seats)+" tickets for "+movie
    def show_movies(self):
        print(self.movies)
    
cinema = Cinema({"Avatar": 10, "Batman": 5})
 
print(cinema.book("Avatar", 2))
 
print(cinema.cancel("Avatar", 1))

cinema.show_movies()
