# web_scraping_imdb

1. Imported the necessary libraries, namely `requests` and `BeautifulSoup`.
2. Defined the target URL as "https://www.foxnews.com/entertainment".
3. Executed an HTTP GET request to the specified URL using the `requests.get()` function.
4. Parsed the retrieved HTML content using BeautifulSoup. Created a BeautifulSoup object by instantiating it with the URL and specifying the 'html.parser' as the parsing method.
5. Employed a loop to extract titles from the "Name" column.
6. Similarly, employed another loop to retrieve information from both the "Year" and "Rate" columns.
7. Accounted for the exception where a title, such as "One Piece," lacked a rating. Implemented exception handling for this case.
8. Developed an additional loop to obtain values for the "Rank" column.
9. Managed the list of top 100 movies by introducing a counter variable to keep track of iterations.
10. Finally, constructed a concluding loop to comprehensively retrieve all data from IMDb in one go.
