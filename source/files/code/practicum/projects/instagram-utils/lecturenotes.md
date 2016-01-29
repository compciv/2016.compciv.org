


# What happens when we post a photo

https://www.instagram.com/p/BBFsKzgQi1m

# What happens when we include a location

Is this all of inner mongolia?

https://www.instagram.com/explore/locations/355807906/


What is it that we're missing?
 
- Exact geocoordinates
- Ability to rank
- How many photos are in this location?
- How many are by the same people?
  + How many are by friends?
  + How many are by foreigners?
- What's their favorite filter?  


### The problems of location:

There's no hierarchical taxonomy:

We can't find all the photos

- https://www.instagram.com/explore/locations/1352/
- https://www.instagram.com/explore/locations/262020403/

- only shows that location


## Let's use the search endpoint

https://www.instagram.com/developer/endpoints/media/


- Let's hardcode a latitude/longitude, access token
- Visit the URL in the browser
- Examine the JSON
  - click on each image URL
  - 

## Explore the JSON

- Requests.get(URL)
- Get one data[0]
- Get one data.images.standard_url

### Iterate through it

- print the URLs
- webbrowser
- just return a list of URLs


### let's make a webpage

- Write out HTML
- Paste in img tags
- write out img tags with Sublime
- Write out img tags programmatically
- print it out
- return text

### All together

- location-collage
- get-json-obj
  + people-collage






-------------

# json.utils

## extract_image_urls(thedict)

- print out each url
- 



### Write prepare_media_search_url

- Just return the basic endpoint
- Show of requests.PreparedRequest



## Expanding on this
