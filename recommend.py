destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes,', 'Shanghai, China', ['historical site,' 'art']]

#retrieves destination from list
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index


#retrieves traveler for testing purposes
def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#append destinations for traveler in new array
test_destination_index = get_traveler_location(test_traveler)
attractions = []
for destination in destinations:
  attractions.append([])

#creates function to add attractions
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destinations = attractions[destination_index].append(attraction)
  except SyntaxError:
    return

#adding new attractions
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
#add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
#add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#creates function to recommend attractions
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest


#returns recommendation information to test traveler
def get_attractions_for_traveler(traveler):
  traveler_destinations = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destinations, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destinations +  ": "
  for place in traveler_attractions:
    return interests_string + "The "  + place
