const $ = window.$;
$.get("https://swapi.co/api/films/?format=json", function(body) {
  let movies = body["results"];
  let list = $("#list_movies");
  movies.forEach(element => {
    list.append("<li>" + element["title"] +"</li\n");
  });
});
