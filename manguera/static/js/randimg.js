$(document).ready(()=>{
    const settings = {
        "async": true,
        "crossDomain": true,
        "url": "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?q=garden%20plants&pageNumber=1&pageSize=50&autoCorrect=false&safeSearch=true",
        "method": "GET",
        "headers": {
            "X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "84d10e90c4mshaaf697e08d37045p101af1jsnd425fd6134cb"
        }
    };
    $.ajax(settings).done(function (response) {
        $(".imgappend").append(`<img class="img-fluid" 
                                     src= ${response["value"][Math.floor(Math.random()*50)]["url"]}><br><br><hr>`)
    });
})